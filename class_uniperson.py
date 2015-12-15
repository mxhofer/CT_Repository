class MyAppObject(object):
    objects = []
    def __init__(self):
        MyAppObject.objects.append(self)

class UniversityPerson(MyAppObject):
    def __init__(self, name, email=""):  # so name has no default value and needs to be passed one. email is optional parameter
        MyAppObject.__init__(self)
        self.name = name
        self.email = email
        self.modules = []
    def __repr__(self):  # returns the person's name
        return self.name

class Student(UniversityPerson):
    objects = []
    def __init__(self, name, email="", studentID=""):
        UniversityPerson.__init__(self,name,email)
        self.studentID = studentID
        Student.objects.append(self)
    def addModule(self, module, call1=True):  # call1 is control parameter to avoid infinite loops
        self.modules.append(module)
        if call1 == True: module.addStudent(self, call1=False)

class UG_Student(Student):
    pass

class PG_Student(Student):
    pass

class Lecturer(UniversityPerson):
    objects = []
    def __init__(self, name, email="", staffID=""):
        UniversityPerson.__init__(self,name,email)
        self.staffID = staffID
        Lecturer.objects.append(self)
    def addModule(self, module, call1=True): #assign a module to a lecturer
        self.modules.append(module) #defined in class UniversityPerson
        if call1 == True: module.addLecturer(self, call1=False)

class Module(MyAppObject):
    objects = []
    def __init__(self, code="",title=""):
        MyAppObject.__init__(self)
        self.code = code
        self.title = title
        self.students = []
        self.lecturers = []
        Module.objects.append(self)
    def addStudent(self,student, call1=True): #assign a student to a module
        self.students.append(student)
        if call1==True: student.addModule(self, call1=False)
    def addLecturer(self,lecturer, call1=True):  # assign a lecturer to a module
        self.lecturers.append(lecturer)
        if call1==True: lecturer.addModule(self, call1=False)
    def __repr__(self):  # returns the modules code and title
        return "Module {}: {}".format(self.code, self.title)


################################finished here in class####################################
# From the book: a mapping from students to a list of grades        

class Grades(object):
    def __init__(self, students, grades):  # create empty grade book
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        # assumes that student is of type student. it adds student to the grade book.
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.getIdNum()] = []  # need to define getIdNum earlier!!!!!!!!!!!!!
        self.isSorted = False

    def addGrade(self, student, grade):
        #assumes that grade is a float. adds grade to the list of grades for a student.
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError("Student not in dictionary")

    def getStudents(self):
        #returns a list of the students in the grade book
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #returns copy of list of students

