# Python

# 🐍 Basic Python Programs + Flask Web Applications

Welcome to my collection of basic Python scripts and beginner-friendly Flask web applications! This repository includes simple Python programs to practice fundamental programming concepts, as well as Flask-based web applications to explore web development and database integration.

## 📂 What’s Inside

The repository is divided into two major sections:

  🧠 Basic Python Programs
  The programs cover a range of beginner-level topics, including:
  - File handling (read/write)
  - Dictionary operations
  - Conditional statements
  - Loops (for, while)
  - Input/output operations
  - Menu-driven programs

  🌐 Flask Web Applications
  This section includes two simple Flask projects to demonstrate web development concepts:
  - REST API with file-backed JSON response
  - Web form + frontend with data submission to MongoDB Atlas

## 🧾 List of Programs

🔸 Python Scripts
Here are a few examples of the programs included:
- `gradChecker.py` - To get a students score and assign a grade accordingly.
- `stuGrade.py` – Add, update, and display student grades using a dictionary.
- `writeFile.py` – Create a text file and write multiple lines to it.
- `readFile.py` – Read content from a text file and display it.

🔸 Flask Apps
Folder/File	Description
- app.py	Simple Flask app with a /api route returning data from a local JSON file.
- Flask/FormSubmit/	Flask app with an HTML form that submits data to MongoDB Atlas and displays success/error feedback. Includes:
  • app.py – Flask backend
  • templates/form.html – Frontend form
  • templates/success.html – Success message page


## 🛠 Requirements

- Python 3.x
- Flask
- pymongo (for MongoDB integration)

  To install dependencies: pip install flask pymongo

No external libraries are required – all programs use only standard Python features.

## 🚀 How to Run

Clone the repository and run any Python file using the terminal or your preferred IDE:

```bash
git clone https://github.com/Cirarshi/Python.git
cd Python
```

Run a python script / Flask API app

python <scriptName>


🌍 MongoDB Integration

The Flask form app uses MongoDB Atlas to store submitted data securely in the cloud. Make sure you:

- Set up your Atlas account
- Whitelist your IP
- Create a database and user
- Update your MongoDB URI in the Flask app

💡 Contribution

Feel free to fork the repo and add your own beginner Python scripts or small Flask experiments.

📜 License

This project is open-source and available

