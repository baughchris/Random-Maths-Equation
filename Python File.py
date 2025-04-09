import tkinter as tk
import random

#Setting Up Quiz
class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("What Is The Value Of 'x'?")

        self.score = 0
        self.question_count = 0
        self.total_questions = 10
        self.correct_answer = None

#Customizing Font And Font Size
        self.question_label = tk.Label(root, text="", font=("Aptos", 24))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Aptos", 16))
        self.answer_entry.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Aptos", 16))
        self.feedback_label.pack(pady=20)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.generate_equation()

#Generation Of Questions
    def generate_equation(self):
        if self.question_count < self.total_questions:
            a = random.randint(1, 10)
            x = random.randint(1, 10)
            b = a * x
            self.correct_answer = x
            self.question_label.config(text=f"{a} × x = {b}")
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
            self.question_count += 1
        else:
            self.end_quiz()

#Response To Answers
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.score += 1
                self.feedback_label.config(text="That's Correct, Well Done!", fg="green")
            else:
                self.feedback_label.config(
                    text=f"Incorrect! The correct answer is {self.correct_answer}", fg="red"
                )
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number", fg="orange")
            return

        self.root.after(1000, self.generate_equation)

#Quiz Results
    def end_quiz(self):
        self.question_label.config(text=f"Quiz Complete! Your score Was: {self.score}/{self.total_questions}")
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.feedback_label.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

    
