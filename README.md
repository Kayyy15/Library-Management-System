# Library Management System 📚

A console-based **Library Management System** built with Python, leveraging **Data Structures and Algorithms (DSA)** for efficient operations. This project serves as a practical demonstration of core DSA concepts applied to a real-world problem.

---

## Features

* **Book Management**: Add, remove, and update book information with ease.
* **User Management**: Register and manage library members.
* **Borrowing & Returning**:
    * **Borrowing**: Seamlessly issue books to members.
    * **Returning**: Members can quickly return books to the system.
* **Search Functionality**: Efficiently locate books or members by various criteria (e.g., title, author, ID) using optimized search algorithms.

---

## Key Data Structures & Algorithms

This project is built on a foundation of efficient data structures and algorithms (DSA) to ensure high performance and scalability.

* **Linked List**: Manages the collection of books, allowing for **efficient insertion and deletion** without the need to shift elements. This is particularly useful when books are added or removed from the library's collection.
* **Hash Map (Dictionary)**: Used for rapid lookups of books or users by their unique IDs. This provides an average-case **O(1)** time complexity for search operations, making the system incredibly fast.
* **Queue**: Implements a waitlist for books that are currently borrowed. This ensures a **First-In, First-Out (FIFO)** order, so members who requested a book first get it first.
* **Stack**: Tracks the history of borrowed books for each user. This allows for easy retrieval of recent borrowing actions and can be used to implement features like "undoing" a borrow or return.

---

## Installation & Usage

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd your-repository-name
    ```
3.  **Run the application**:
    ```bash
    python main.py
    ```
