lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):
    total = sum(numbers)
    total = float(total)
    average = total/len(numbers)
    return average

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    get_average = 0.1*homework + 0.3*quizzes + 0.6*tests
    return get_average
    
def get_letter_grade(score):
    if score >= 90:
        print "A"
        return "A"
    elif score >= 80:
        print "B"
        return "B"
    elif score >= 70:
        print "C"
        return "C"
    elif score >= 60:
        print "D"
        return "D"
    else:
        print "F"
        return "F"

get_letter_grade(get_average(alice))
get_letter_grade(get_average(lloyd))
get_letter_grade(get_average(tyler))

results = []

def get_class_average(students):
    for student in students:
        results.append(get_average(student))
    print results
    return average(results)

students = [lloyd, alice, tyler]
print get_class_average(students)

print get_letter_grade(average(results))
