def load_questions(filepath):
    questions = {}
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            letter, answer = line.split()
            questions[letter] = answer

    return questions
