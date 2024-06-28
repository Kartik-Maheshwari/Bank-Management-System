# 🏦 Banking Management System

A comprehensive banking management system built with Python and MySQL, allowing for user registration, login, account management, transactions, and more.

## 📋 Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## ✨ Features

- 👤 User Registration and Login
- 🏦 Create and Manage Bank Accounts
- 💰 Perform Transactions (Deposit and Withdraw)
- 📄 View Customer Details
- 📜 View Transaction History
- 🗑️ Delete Accounts

## 🛠️ Technologies

- 🐍 Python
- 🗄️ MySQL

## 🛠️ Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/banking-management.git
    ```

2. Navigate to the project directory:
    ```bash
    cd banking-management
    ```

3. Set up the MySQL database:
    - Open MySQL and create a database named `bank`.
    - Run the provided SQL scripts to create the required tables:
      ```sql
      CREATE TABLE customer_details (
          acct_no INT PRIMARY KEY,
          acct_name VARCHAR(25),
          phone_no BIGINT(25) CHECK (phone_no > 11),
          address VARCHAR(25),
          cr_amt FLOAT
      );
      
      CREATE TABLE transactions (
          acct_no INT(11),
          date DATE,
          withdrawal_amt BIGINT(20),
          amount_added BIGINT(20)
      );
      
      CREATE TABLE user_table (
          username VARCHAR(25) PRIMARY KEY,
          passwrd VARCHAR(25) NOT NULL
      );
      ```

4. Install required Python packages:
    ```bash
    pip install mysql-connector-python
    ```

## 🚀 Usage

1. Run `Bank.py` to start the application:
    ```bash
    python Bank.py
    ```

2. Follow the on-screen prompts to register or login, and then navigate through the menu to manage accounts and perform transactions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
