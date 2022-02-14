from random import choice
import tkinter as tk

from questions import load_questions


class Oppu(tk.Tk):
    def __init__(self):
        super(Oppu, self).__init__()

        # Setup:
        self.title('Oppu-Chan')
        self.geometry('240x240')
        self._set_icon()

        # Variables:
        self.questions = load_questions('questions/katakana.ans')
        self.current_question = choice(list(self.questions.keys()))
        self.streak = 0

        # Widgets:
        self.streak_label, self.correct_label, self.question_label, self.answer_button, self.text_input = [None] * 5
        self._create_widgets()

    def answer_command(self, event=None):
        if self.text_input.get().upper() == self.questions[self.current_question]:
            self.correct_label.config(text=f"Correct!", fg='#228B22')

            self.streak += 1
            self.streak_label.config(text=f"Streak: {self.streak}")

        else:
            correct = self.questions[self.current_question].title()
            self.correct_label.config(text=f"Incorrect... That was {correct}.",
                                      fg='#ff3232')

            self.streak = 0
            self.streak_label.config(text=f"Streak: 0")

        self.correct_label.pack(side=tk.TOP, pady=1)
        self.text_input.delete(0, tk.END)

        self.change_question()

    def change_question(self):
        self.current_question = choice(list(self.questions.keys()))
        self.question_label.config(text=f"{self.current_question}")

    # Helpers:
    def _set_icon(self):
        try:
            self.iconbitmap('icon.ico')
        except tk.TclError:
            print(f"[Error]: The icon file could not be file within the project's directory.")

    def _create_widgets(self):
        self.streak_label = tk.Label(self, text=f"Streak: {self.streak}")
        self.streak_label.pack(side=tk.TOP, pady=3)

        self.correct_label = tk.Label(self)

        self.question_label = tk.Label(self, text=f"{self.current_question}")
        self.question_label.config(font=("Consolas", 32))
        self.question_label.pack(pady=30)

        self.answer_button = tk.Button(self, text="Answer", command=self.answer_command)
        self.answer_button.pack(side=tk.BOTTOM, pady=5)

        self.text_input = tk.Entry(self)
        self.text_input.bind('<Return>', self.answer_command)
        self.text_input.pack(side=tk.BOTTOM, pady=5)
        self.text_input.focus()


if __name__ == '__main__':
    app = Oppu()
    app.mainloop()
