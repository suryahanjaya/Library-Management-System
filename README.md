# Library Management System

A Python-based project implementing a **Library Management System** using object-oriented programming (OOP) concepts and web frontend integration with **Eel**.

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
2. Navigate to the project directory:
   ```bash
   cd Library-Management-System-main
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Start the application:
   ```bash
   python main.py


## 🛠 Technologies Used

- **Programming Language**: Python
- **Database**: MongoDB
- **Web Framework**: Eel

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
