# 🔐 SQL Injection Detection System

## 📌 Overview

This project is a basic security system that detects and prevents SQL injection attempts during user login.

## 🎯 Objective

To enhance application security by identifying malicious input patterns and blocking unauthorized access.

## 🚀 Features

* Accepts username and password input
* Detects common SQL injection patterns
* Blocks unsafe input
* Allows safe login attempts
* Demonstrates basic cybersecurity concepts

## 🛠 Technologies Used

* Python 3

## 🧠 Working Principle

1. User enters username and password
2. Inputs are checked against known SQL injection patterns such as:

   * ' (single quote)
   * -- (comment)
   * OR, AND
   * DROP, SELECT
3. If any pattern is found → access denied
4. Otherwise → login successful

## ▶️ How to Run

1. Open terminal
2. Run:
   python secure_login.py
3. Enter credentials

## 📊 Example

### ✅ Safe Input

Username: user
Password: 1234
Output: Login Successful

### ❌ Injection Attempt

Username: admin' OR 1=1 --
Output: SQL Injection Detected

## 📂 Project Structure

CodeAlpha_SQLSecurity/
│
└── secure_login.py

## 💡 Applications

* Web application security basics
* Input validation systems
* Learning cybersecurity concepts

## ⚠️ Limitations

* Basic pattern matching only
* Not suitable for production use

## 🔮 Future Improvements

* Implement AES encryption
* Connect with database
* Build web-based login system

## 🙌 Acknowledgement

Developed as part of CodeAlpha Internship.
