
class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = [float(score) if score.strip() != '' else None for score in scores]

    def RunningAverage(self):
        non_blank_scores = [score for score in self.Grades if score is not None]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        return 0.0

    def TotalAverage(self):
        full_scores = [score if score is not None else 0 for score in self.Grades]
        return sum(full_scores) / len(full_scores) if full_scores else 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


students = []
with open("TextFiles/10.Project Student Scores.txt") as file:
    for line in file:
        parts = line.strip().split(',')
        firstname, lastname, tnumber, *scores = parts
        student = Student(firstname, lastname, tnumber, scores)
        students.append(student)


print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
print(f"{'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")

for student in students:
    print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
          f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")
