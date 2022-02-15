def load_questions(filepath):
    if not filepath:
        return

    questions = {}
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            letter, answer = line.split()
            questions[letter] = answer.upper()

    return questions
