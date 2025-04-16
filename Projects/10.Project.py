class Student():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores
    
    def RunningAverage(self):
        sum = 0
        for i in len(self.Grades):
            sum += self.Grades[i]

        sum = sum / len(self.Grades)
        return sum;

    def TotalAverage(self):

    
    def LetterGrade(self):