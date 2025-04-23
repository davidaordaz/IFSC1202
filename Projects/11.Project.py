class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        valid_grades = [float(g) for g in self.Grades if g != '']
        return sum(valid_grades) / len(valid_grades) if valid_grades else 0.0

    def TotalAverage(self):
        total = sum(float(g) if g != '' else 0.0 for g in self.Grades)
        return total / len(self.Grades) if self.Grades else 0.0

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


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        self.Studentlist.append(Student(firstname, lastname, tnumber))

    def find_student(self, tnumber):
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
        print(f"{'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
        for student in self.Studentlist:
            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(',')
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                tnumber, score = line.strip().split(',') if ',' in line else (line.strip(), '')
                idx = self.find_student(tnumber)
                if idx != -1:
                    self.Studentlist[idx].Grades.append(score)


def main():
    students_file = 'TextFiles/11.Project Students.txt'
    scores_file = 'TextFiles/11.Project Scores.txt'

    sl = StudentList()
    sl.add_student_from_file(students_file)
    sl.add_scores_from_file(scores_file)
    sl.print_student_list()

if __name__ == "__main__":
    main()
