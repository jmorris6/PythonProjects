class student:

    def __init__(self, quiz1S, quiz2S, midtermS, finalS):
        self.quiz1 = quiz1S
        self.quiz2 = quiz2S
        self.midterm = midtermS
        self.final = finalS
        self.getAverage()
        self.getLetterGrade()
    
    def getAverage(self):
        quizAverage = ((self.quiz1 + self.quiz2) * .25) / 2
        midtermWeight = self.midterm * .25
        finalWeight = self.final * .50
        self.average = quizAverage + midtermWeight + finalWeight
    
    def getLetterGrade(self):
        if self.average >= 90:
            self.letterGrade = 'A'
        elif (self.average >= 80):
            self.letterGrade = 'B'
        elif (self.average >= 70):
            self.letterGrade = 'C'    
        elif (self.average >= 60):
            self.letterGrade = 'D'
        else:
            self.letterGrade = 'F'
def createStudents():
    students = []
    with open("INprog1.dat", "r") as grades:
        studGrades = grades.readline().split()
        while (studGrades != []):
            temp = student(int(studGrades[0]), int(studGrades[1]), int(studGrades[2]), int(studGrades[3]))
            students.append(temp)
            studGrades = grades.readline().split()
        return students
def writeStudents(student):
    with open("OUTprog1.dat", "a") as grades:
        grades.write(str(student.quiz1) + " " + str(student.quiz2) + " " + str(student.midterm) + " " + str(student.final) + " " + str(student.average) + " " + str(student.letterGrade) + "\n")
    
students = createStudents()
for x in range(len(students)):
    writeStudents(students[x])
    