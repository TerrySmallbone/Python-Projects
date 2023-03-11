student_scores = {
    'Alex': 75,
    'Beth': 81,
    'Caroline': 34
    'Dave': 98,
    'Freddie': 56
}
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

