from tkinter import filedialog as fd
from itertools import product
from random import choices
from tkinter import ttk
from os import getcwd
import tkinter as tk

from questions import load_questions


class Oppu(tk.Tk):
    def __init__(self):
        super(Oppu, self).__init__()

        # Setup:
        self.eval('tk::PlaceWindow . center')
        self.title('Oppu-Chan')
        self.geometry('240x240')
        self.minsize(240, 240)
        self._set_icon()

        # Style:
        self.style = ttk.Style()

        # Menu Bar:
        self.menu_bar = tk.Menu(self)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open...', command=self.load_question, accelerator='Ctrl+O')
        self.file_menu.add_command(label='Difficulty', command=self.select_difficulty)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.quit, accelerator='Ctrl+E')

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # Variables:
        self.questions = load_questions('questions/katakana.ans')
        self.current_question = ''.join(choices(list(self.questions.keys()), k=1))
        self.streak, self.difficulty = 0, 1

        # Widgets:
        self.streak_label, self.correct_label, self.question_label, self.answer_button, self.text_input = [None] * 5
        self.streak_separator = None
        self._create_widgets()

    # Button Commands:
    def answer_command(self, event=None):
        string_answer, answer = '', []
        for character in self.current_question:
            answer.append(self.questions[character])

        answers = [''.join(x) for x in list(product(*answer))]

        if self.text_input.get().upper() in answers:
            self.correct_label.config(text=f"Correct!", foreground='#228B22')

            self.streak += self.difficulty
            self.streak_label.config(text=f"Streak: {self.streak}")

        else:
            self.correct_label.config(text=f"Incorrect... That was {''.join(answers[0]).title()}.",
                                      foreground='#ff3232')

            self.streak = 0
            self.streak_label.config(text=f"Streak: 0")

        self.correct_label.pack(side=tk.TOP, pady=1)
        self.text_input.delete(0, tk.END)

        self.change_question()

    def change_question(self):
        self.current_question = ''.join(choices(list(self.questions.keys()), k=self.difficulty))
        self.question_label.config(text=f"{self.current_question}")

    # Menu Commands:
    def load_question(self):
        filetypes = (('Question Files', '*.ans'),)

        filename = fd.askopenfilename(title='Open a file', initialdir=getcwd(), filetypes=filetypes)
        self.questions = load_questions(filename)
        self.change_question()

    def select_difficulty(self):
        selector = tk.Toplevel()
        selector.geometry("300x100")
        selector.minsize(300, 100)
        selector.focus()

        self.eval(f'tk::PlaceWindow {str(selector)} center')

        difficulty_label = ttk.Label(selector, text=f"{self.difficulty}")

        def control_difficulty(value=None):
            self.difficulty = round(float(value))
            difficulty_label.config(text=f"{self.difficulty}")

        scale = ttk.Scale(selector, from_=1, to=5, value=self.difficulty, orient=tk.HORIZONTAL,
                          command=control_difficulty)

        def on_ok():
            self.change_question()
            selector.destroy()

        ok_button = ttk.Button(selector, text='Ok', command=on_ok)

        scale.pack(fill='x', padx=10, pady=10)
        difficulty_label.pack()
        ok_button.pack()

        self.difficulty = scale.get()

    # Helpers:
    def _set_icon(self):
        try:
            self.iconbitmap('icon.ico')
        except tk.TclError:
            print(f"[Error]: The icon file could not be file within the project's directory.")

    def _create_widgets(self):
        self.streak_label = ttk.Label(self, text=f"Streak: {self.streak}")
        self.streak_label.pack(side=tk.TOP, pady=3)

        self.streak_separator = tk.Frame(self, bg='#bababa', height=1, bd=0)
        self.streak_separator.pack(fill='x')

        self.correct_label = ttk.Label(self)

        self.question_label = ttk.Label(self, text=f"{self.current_question}")
        self.question_label.config(font=("Consolas", 32))
        self.question_label.pack(pady=30)

        self.answer_button = ttk.Button(self, text="Answer", command=self.answer_command)
        self.answer_button.pack(side=tk.BOTTOM, pady=5)

        self.text_input = ttk.Entry(self)
        self.text_input.bind('<Return>', self.answer_command)
        self.text_input.pack(side=tk.BOTTOM, pady=5)
        self.text_input.focus()


if __name__ == '__main__':
    app = Oppu()
    app.mainloop()
