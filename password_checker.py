import tkinter as tk
from tkinter import messagebox
import re
import random
import string

try:
    from nltk.corpus import words
except ImportError:
    words = None

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Strength Checker")
        self.root.geometry("500x470")
        self.root.config(bg="#f4f6f9")

        # Title
        tk.Label(root, text="🔐 Password Strength Checker", font=("Helvetica", 17, "bold"),
                 bg="#f4f6f9", fg="#333").pack(pady=10)

        # Entry Label
        tk.Label(root, text="Enter Your Password:", font=("Helvetica", 11, "bold"), bg="#f4f6f9").pack()
        self.entry = tk.Entry(root, show="*", font=("Helvetica", 11), width=30, bd=2, relief="groove")
        self.entry.pack(pady=5)

        # Show/hide password
        self.show_password = False
        self.toggle_btn = tk.Button(root, text="Show Password", font=("Helvetica", 9), command=self.toggle_visibility)
        self.toggle_btn.pack()

        # Strength Bar Canvas
        self.canvas = tk.Canvas(root, height=50, width=400, bg="#f4f6f9", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Strength Label
        self.strength_label = tk.Label(root, text="Strength: None", font=("Helvetica", 12, "bold"),
                                       bg="#f4f6f9", fg="black")
        self.strength_label.pack(pady=5)

        # Suggestion Label
        self.suggestion_label = tk.Label(root, text="", font=("Helvetica", 10), fg="#e63946",
                                         bg="#f4f6f9", justify="left", wraplength=440)
        self.suggestion_label.pack(pady=(0, 10))

        # Buttons
        tk.Button(root, text="Check Strength", font=("Helvetica", 11), bg="#4287f5", fg="white",
                  command=self.check_strength).pack(pady=5, ipadx=5, ipady=3)

        tk.Button(root, text="Generate Strong Password", font=("Helvetica", 10),
                  command=self.generate_password).pack(pady=5)

    def toggle_visibility(self):
        self.show_password = not self.show_password
        self.entry.config(show="" if self.show_password else "*")
        self.toggle_btn.config(text="Hide Password" if self.show_password else "Show Password")

    def generate_password(self):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(random.choice(chars) for _ in range(16))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)
        self.check_strength()

    def check_strength(self):
        password = self.entry.get()
        if password == "":
            messagebox.showinfo("Error", "Password cannot be empty.")
            return

        self.canvas.delete("all")
        strength, score, suggestions = self.evaluate_password(password)

        # Draw Strength Bar
        if score == 5:
            self.canvas.create_rectangle(50, 10, 350, 40, fill="#27cf54", outline="white")  # Green
        elif 3 <= score < 5:
            self.canvas.create_rectangle(50, 10, 350, 40, fill="#f0f007", outline="white")  # Yellow
        else:
            self.canvas.create_rectangle(50, 10, 350, 40, fill="#de3c3c", outline="white")  # Red

        # Update Labels
        self.strength_label.config(text=f"Strength: {strength}",
                                   fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")
        self.suggestion_label.config(text=suggestions)

    def evaluate_password(self, pw):
        feedback = []
        score = 0

        if len(pw) >= 8:
            score += 1
        else:
            feedback.append("⚠️ Use at least 8 characters.")

        if re.search(r"[a-z]", pw):
            score += 1
        else:
            feedback.append("⚠️ Include at least one lowercase letter.")

        if re.search(r"[A-Z]", pw):
            score += 1
        else:
            feedback.append("⚠️ Include at least one uppercase letter.")

        if re.search(r"\d", pw):
            score += 1
        else:
            feedback.append("⚠️ Include at least one digit.")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
            score += 1
        else:
            feedback.append("⚠️ Add at least one special character (!@#...).")

        # Weak patterns
        weak_patterns = ["123", "password", "qwerty", "admin", "welcome"]
        if any(pattern in pw.lower() for pattern in weak_patterns):
            feedback.append("⚠️ Avoid common patterns like '123', 'password', etc.")

        # Dictionary check
        if words and pw.lower() in words.words():
            feedback.append("⚠️ Avoid full dictionary words.")

        if score == 5 and not feedback:
            return "Strong", score, "✅ Excellent password!"
        elif score >= 3:
            return "Moderate", score, "\n".join(feedback)
        else:
            return "Weak", score, "\n".join(feedback)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()
