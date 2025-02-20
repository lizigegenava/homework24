def calculate_average(grades):
    average = sum(grades) / len(grades)
    return average

def is_passing(average):
    if average >= 70:
        return True
    else:
        return False

def grade_to_letter(average):
    if average >= 91 and average <= 100:
        return "A"
    elif average >= 81 and average <= 90:
        return "B"
    elif average >= 71 and average <= 80:
        return "C"
    elif average >= 61 and average <= 70:
        return "D"
    else:
        return "F"