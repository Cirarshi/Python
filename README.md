# Cirarshi / Python

A collection of Python-based projects and experiments — web apps, utilities, and learning code — maintained by Cirarshi.

---

## 📂 Structure

| Folder | Purpose |
|---|---|
| **Basics/** | Core Python scripts and foundational learning — small utilities, simple exercises. |
| **Flask/** | A web application (or apps) built using the Flask framework. |
| **tryQue/** | Experimental or “sandbox” code — trying out new ideas, queueing tasks, proofs of concepts. |

---

## ⚙️ Getting Started

These instructions will help you run the projects locally for development and testing.

### Prerequisites

- Python 3.8+ installed  
- `pip` or `venv` to manage dependencies  
- (Optional) virtual environment for isolating dependencies

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Cirarshi/Python.git
   cd Python
   ```
2. Create and activate a virtual environment (recommended):
  ```bash
  python3 -m venv venv
  source venv/bin/activate      # On Windows: venv\Scripts\activate
  ```
3. Install any required packages. If there's a requirements.txt in the specific project folder:
  ```bash
  pip install -r <project_folder>/requirements.txt
  ```

---

### 🚀 Running the Projects

Here are example commands depending on which project you want to run:
  - For Basics/
    Navigate into the folder, then run the python script:
    ```bash
    cd Basics
    python example_script.py
    ```
  - For Flask/
  If there’s a app.py or similar:
  ```bash
  cd Flask
  export FLASK_APP=app.py
  flask run
  ```
  - For tryQue/
  Go into the folder and run or test whatever experiment code is inside:
  ```bash
  cd tryQue
  python experiment.py
  ```

---

### 🧪 Tests

If there are test files (for example using pytest), you can run:
```bash
pytest
```

Make sure you’re in the root of the folder or set up correctly so it can find tests.

---

### 🔧 Future Enhancements

Here are some ideas for what you might want to add later:
  - CI/CD pipeline (GitHub Actions) to automatically run tests and maybe auto-deploy
  - Dockerization of the Flask app for easier deployment
  - More detailed documentation per project
  - A unified requirements.txt per project or one for the whole repo

---
