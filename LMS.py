# library.py
# Simple Library Management System
# - A file named "books.txt" exists in the same folder with one book title per line.
# - Issued books are tracked in "issued_books.txt" (created if missing).
# - User inputs are simple text; no authentication included.

import os
import sys
from datetime import datetime

BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued_books.txt"

def clear_screen():
    # cross-platform screen clear
    os.system('cls' if os.name == 'nt' else 'clear')

def ensure_files():
    # make sure required files exist
    if not os.path.exists(BOOKS_FILE):
        open(BOOKS_FILE, 'a', encoding='utf-8').close()
    if not os.path.exists(ISSUED_FILE):
        open(ISSUED_FILE, 'a', encoding='utf-8').close()

def read_books():
    with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
        books = [line.strip() for line in f if line.strip()]
    return books

def read_issued():
    # issued_books.txt format: book_title ||| borrower_name ||| date_issued (ISO)
    issued = []
    with open(ISSUED_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            parts = line.split('|||')
            # tolerate malformed lines
            if len(parts) >= 3:
                title = parts[0].strip()
                borrower = parts[1].strip()
                date = parts[2].strip()
                issued.append((title, borrower, date))
            else:
                # fallback: if only title stored
                issued.append((parts[0].strip(), '', ''))
    return issued

def write_issued(issued_list):
    with open(ISSUED_FILE, 'w', encoding='utf-8') as f:
        for title, borrower, date in issued_list:
            f.write(f"{title} ||| {borrower} ||| {date}\n")

def display_books():
    books = read_books()
    issued = read_issued()
    issued_titles = {title for (title, _, _) in issued}
    if not books:
        print("No books found in the library file.")
        return
    print("Books available in library:")
    for i, b in enumerate(books, start=1):
        status = "ISSUED" if b in issued_titles else "AVAILABLE"
        print(f"{i}. {b}  [{status}]")

def add_book():
    books = read_books()
    print("Enter the title of the book to add:")
    title = input("> ").strip()
    if not title:
        print("Empty title. Aborting.")
        return
    if title in books:
        print("This book already exists in the library file.")
        return
    with open(BOOKS_FILE, 'a', encoding='utf-8') as f:
        f.write(title + "\n")
    print(f"Book '{title}' added successfully.")

def issue_book():
    books = read_books()
    if not books:
        print("No books in library to issue.")
        return
    display_books()
    print("\nType the number (or exact title) of the book you want to issue:")
    choice = input("> ").strip()
    # determine selected title
    selected = None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(books):
            selected = books[idx]
    else:
        # try exact title match
        if choice in books:
            selected = choice
    if not selected:
        print("Invalid selection.")
        return
    issued = read_issued()
    issued_titles = {title for (title, _, _) in issued}
    if selected in issued_titles:
        print(f"'{selected}' is already issued to someone else.")
        return
    print("Enter borrower's name:")
    borrower = input("> ").strip()
    if not borrower:
        print("Empty borrower name. Aborting.")
        return
    date_str = datetime.now().isoformat(timespec='seconds')
    issued.append((selected, borrower, date_str))
    write_issued(issued)
    print(f"Book '{selected}' issued to {borrower} on {date_str}.")

def return_book():
    issued = read_issued()
    if not issued:
        print("No issued books to return.")
        return
    print("Currently issued books:")
    for i, (title, borrower, date) in enumerate(issued, start=1):
        print(f"{i}. {title}  (borrower: {borrower}, issued: {date})")
    print("\nType the number (or exact title) of the book to return:")
    choice = input("> ").strip()
    to_remove_idx = None
    to_remove_title = None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(issued):
            to_remove_idx = idx
            to_remove_title = issued[idx][0]
    else:
        for i, (title, borrower, date) in enumerate(issued):
            if title == choice:
                to_remove_idx = i
                to_remove_title = title
                break
    if to_remove_idx is None:
        print("Invalid selection.")
        return
    # remove it
    removed = issued.pop(to_remove_idx)
    write_issued(issued)
    print(f"Book '{removed[0]}' returned successfully (was borrowed by {removed[1]} on {removed[2]}).")

def show_issued_list():
    issued = read_issued()
    if not issued:
        print("No books issued right now.")
        return
    print("Issued books:")
    for i,(title, borrower, date) in enumerate(issued, start=1):
        print(f"{i}. {title} -- {borrower} (issued: {date})")

def main_menu():
    ensure_files()
    while True:
        print("\n--------------- Library Management System ----------------")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Show issued books")
        print("6. Exit")
        print("Choose an option (1-6):")
        opt = input("> ").strip()
        clear_screen()
        if opt == '1':
            display_books()
        elif opt == '2':
            add_book()
        elif opt == '3':
            issue_book()
        elif opt == '4':
            return_book()
        elif opt == '5':
            show_issued_list()
        elif opt == '6':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Choose 1-6.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
