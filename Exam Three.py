from math import acos, degrees, sqrt

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isocelese"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        a = self.s1
        b = self.s2
        c = self.s3

        angleA = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angleB = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angleC = degrees(acos((a**2 + b**2 - c**2) / (2 * a * b)))

        return [round(angleA, 3), round(angleB, 3), round(angleC, 3)]



TriangleList = []

with open("TextFiles/Exam Three Triangle.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            triangle = Triangle(parts[0], parts[1], parts[2])
            TriangleList.append(triangle)


print(f"{'Type':>13} {'Side 1':>10} {'Side 2':>10} {'Side 3':>10} {'Perimeter':>10} {'Area':>10} {'Angle 1':>10} {'Angle 2':>10} {'Angle 3':>10}")


for t in TriangleList:
    t_type = t.type()
    s1 = f"{t.s1:.3f}"
    s2 = f"{t.s2:.3f}"
    s3 = f"{t.s3:.3f}"
    perimeter = f"{t.perimeter():.3f}"
    area = f"{t.area():.3f}"
    angles = t.angles()
    angle1 = f"{angles[0]:.3f}"
    angle2 = f"{angles[1]:.3f}"
    angle3 = f"{angles[2]:.3f}"

    print(f"{t_type:>13} {s1:>10} {s2:>10} {s3:>10} {perimeter:>10} {area:>10} {angle1:>10} {angle2:>10} {angle3:>10}")
