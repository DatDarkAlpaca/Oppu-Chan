def load_questions(filepath):
    if not filepath:
        return

    questions = {}
    with open(filepath, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            attributes = line.split()
            letter = attributes[0]
            questions[letter] = [attributes[x].upper() for x in range(1, len(attributes))]

    return questions
