# Library Management System

BOOKTOPIA is a library management system designed to facilitate the management of books, users, and borrowing transactions. The application allows administrators to manage books, add new users, and track borrowing activities, while users can browse available books, borrow them, and manage their profiles. The system is built using Python and MongoDB, providing a robust backend for data management and a user-friendly interface for interaction.

## 🎯 Goals

- **Design Classes**: Manage books, members, and the library system.
- **Implement Functionalities**: Streamlined borrowing, returning, and tracking of library books.
- **Apply OOP Principles**: 
  - Classes & Objects
  - Attributes & Methods
  - Constructor
  - Setter & Getter
  - Encapsulation
  - Inheritance
  - Overriding
  - Access Modifier
  - Abstraction
  - Polymorphism

## ✨ Features

### 📚 Book Management
- Add new books (title, author, ISBN, etc.).
- Edit book information.
- Delete books from the system.
- Search for books by title, author, or ISBN.

### 👥 User Management
- Register new members (name, address, contact information).
- Edit member details.
- Delete member accounts.
- Search for members by name or ID.

### 📖 Loan Management
- Borrow books (including due date tracking).
- Return borrowed books.
- Extend loan period (optional).
- Calculate fines for late returns (optional).

### 📊 Reporting
- Generate reports on:
  - Available books.
  - Borrowed books.
  - Member borrowing history (optional).


## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository or download the project files.
   ```bash
   git clone https://github.com/suryahanjaya/Library-Management-System
   cd BOOKTOPIA
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Set Up MongoDB:
   Ensure you have MongoDB installed and running on your local machine. The default connection string used in the project is mongodb://localhost:27017/.
4. Start the application:
   ```bash
   python main.py

## 🛠 Technologies Used

- **Python**      : The primary programming language used for backend development.
- **MongoDB**     : A NoSQL database used for storing user and book data.
- **Eel**         : A Python library for creating simple Electron-like desktop apps with HTML/JS frontends.
- **HTML/CSS**    : For structuring and styling the web interface.
- **JavaScript**  : For client-side scripting and interactivity.
- **Bootstrap**   : A CSS framework for responsive design.

## 🧩 Object-Oriented Programming Concepts
## Key Classes
1. `DatabaseConnection`: Abstract class defining a contract for database connection.
2. `Database: Implements` connection for MongoDB.
3. `UserHandler`: Manages user authentication and data.

## Concepts
1. **Encapsulation**:
- Private attributes in classes like `Database` to hide implementation details `(_client)`.
2. Inheritance:
- `Database` inherits from `DatabaseConnection`.
3. Polymorphism:
- Abstract method `connect` in `DatabaseConnection`, overridden by `Database`.
4. Abstraction:
- Using `ABC` (Abstract Base Class) for defining the structure of database-related classes.
5. Attributes & Methods:
- Attributes like `self.host`, `self.clien`t.
- Methods like `connect` for database connections.

## 👩‍💻 Authors
*TI A 2023*
- **23051204007 SURYA HANJAYAA**
- **23051204016 DEA PRIMATAMA**
- **23051204023NATASYAH SALSABILLAH WIBISONO**
