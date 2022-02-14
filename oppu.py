from random import choice
import tkinter as tk


# Loading Katakana:
answers = {}
with open('katakana.ans', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        letter, answer = line.split()
        answers[letter] = answer

# Current Question & Streak:
current_question = choice(list(answers.keys()))
streak = 0

# Answer Command:
correct_label, question, text_input, streak_label = [None] * 4


def answer_command(event=None):
    global answer, streak, streak_label, correct_label

    def change_question():
        global current_question
        current_question = choice(list(answers.keys()))
        question.config(text=f"{current_question}")

    if text_input.get().upper() == answers[current_question]:
        correct_label.config(text=f"Correct!", fg='#228B22')
        streak += 1
        streak_label.config(text=f"Streak: {streak}")
        
    else:
        correct = answers[current_question].title()
        correct_label.config(text=f"Incorrect... That was {correct}.",
                             fg='#ff3232')
       
        streak = 0
        streak_label.config(text=f"Streak: 0")

    correct_label.pack(side=tk.TOP, pady=1)
    text_input.delete(0, tk.END)
    change_question()


# GUI:
root = tk.Tk()
root.iconbitmap('icon.ico')
root.geometry("240x240")
root.title("Oppu-Chan")
root.minsize(240, 240)

# Streak Label:
streak_label = tk.Label(root, text=f"Streak: {streak}")
streak_label.pack(side=tk.TOP, pady=3)

# Correct | Wrong Label:
correct_label = tk.Label(root)

# Question Label:
question = tk.Label(root, text=f"{current_question}")
question.config(font=("Consolas", 32))
question.pack(pady=30)

# Answer Button:
answer_button = tk.Button(root, text="Answer", command=answer_command)
answer_button.pack(side=tk.BOTTOM, pady=5)

# Entry:
text_input = tk.Entry(root)
text_input.pack(side=tk.BOTTOM, pady=5)
text_input.focus()
text_input.bind('<Return>', answer_command)

# Main:
tk.mainloop()
