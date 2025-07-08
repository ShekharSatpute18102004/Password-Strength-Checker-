# 🔐 Password Strength Checker

## 📌 Problem Statement
Weak passwords are among the most common causes of data breaches and unauthorized access. Many users create passwords that are short, predictable, or based on dictionary words, making them vulnerable to brute-force and dictionary attacks.

## 🎯 Objective
To build a **GUI-based tool** that evaluates the strength of user-entered passwords and provides:
- Real-time feedback
- Suggestions to improve password security
- Optional dictionary word detection

---

## 🛠️ Requirements

- Python 3.x
- `Tkinter` (for GUI)
- `re` (Regex for pattern matching)
- `nltk` *(optional, for dictionary word detection)*

Install NLTK if using dictionary word detection:
```
pip install nltk
```
### 🧰 Features

- ✅ Checks for: 
  - Minimum length
  - Uppercase and lowercase letters
  - Digits and special characters
  - Repetition patterns
  - Dictionary word usage (optional with NLTK)

- ✅ Provides strength rating:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong

- ✅ Gives recommendations:
  - Add more special characters
  - Avoid dictionary words
  - Increase length
  - Use mix of character types

## 🖥️ GUI Preview
The app uses Tkinter to provide a simple and intuitive interface:
```
+-------------------------------------------+
|     🔐 Password Strength Checker          |
+-------------------------------------------+
| [ Enter your password here:          ]    |
|                                           |
| ➤ Strength: Weak                         |
| ➤ Suggestions:                           |
|    - Add more characters                  |
|    - Use at 
least one special character   |
+-------------------------------------------+
```
### 📂 Project Structure
```
password-strength-checker/
├── password_checker.py         # Main Python GUI application
├── README.md                   # Project documentation
```

## 🧠 How It Works
- The app uses Regex to validate password patterns.
- Optionally, it uses NLTK's English word corpus to flag dictionary words.
- Password strength is scored based on entropy and best practices.
- Suggestions are generated dynamically based on missing elements.

## 🚀 How to Run the Project
1. Clone the repository
```
git clone https://github.com/ShekharSatpute18102004/Password-Strength-Checker-.git
cd password-strength-checker
```
2. Install dependencies
```
pip install nltk
```
3. Run the script
```
python password_checker.py
```
## 📸 Screenshots
<img width="375" alt="output" src="https://github.com/user-attachments/assets/84a08771-b454-4ef8-82c9-c7bafcfa3130" />

### 📄 License
MIT License — Open to contributions and modifications.
