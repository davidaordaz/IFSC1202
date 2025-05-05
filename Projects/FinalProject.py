class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  
        self.pen = 'U'        
        self.canvas = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(' ')
            self.canvas.append(row)

    def printsketch(self):
        print('+' + '-' * self.size + '+')
        i = self.size - 1
        while i >= 0:
            print('|', end='')
            for j in range(self.size):
                print(self.canvas[i][j], end='')
            print('|')
            i = i - 1
        print('+' + '-' * self.size + '+')
        print('X =', self.xpos, ' Y =', self.ypos, ' Direction =', self.direction)

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'

    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'

    def move(self, steps):
        count = 0
        while count < steps:
            if self.pen == 'D':
                self.canvas[self.ypos][self.xpos] = '*'

            if self.direction == 'U':
                if self.ypos < self.size - 1:
                    self.ypos += 1
            elif self.direction == 'D':
                if self.ypos > 0:
                    self.ypos -= 1
            elif self.direction == 'R':
                if self.xpos < self.size - 1:
                    self.xpos += 1
            elif self.direction == 'L':
                if self.xpos > 0:
                    self.xpos -= 1

            count = count + 1

        if self.pen == 'D':
            self.canvas[self.ypos][self.xpos] = '*'


def runFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    new_lines = []
    for line in lines:
        line = line.strip()
        if line != '':
            new_lines.append(line)

    size = int(new_lines[0])
    mysketch = Sketch(size)

    for command in new_lines[1:]:
        if command == '1':
            mysketch.penup()
        elif command == '2':
            mysketch.pendown()
        elif command == '3':
            mysketch.turnright()
        elif command == '4':
            mysketch.turnleft()
        elif command == '6':
            mysketch.printsketch()
        elif command.startswith('5,'):
            parts = command.split(',')
            num = int(parts[1])
            mysketch.move(num)



runFile("TextFiles/Cshape.txt")
