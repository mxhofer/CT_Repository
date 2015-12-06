class Person(object):

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(" ") #this breaks the string into a first and last name
            self.lastName = name[lastBlank+1:]
            firstn = name.index(" ")
            self.firstName = name[0:firstn]
        except:
            self.lastName = name
        self.birthday = None #creates .birthday function

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def getFirstName(self): #added this myself!!
        """Returns self's first name"""
        return self.firstName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
                Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self, other):
        """Returns True if self's name is lexicographically less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name

"""
me = Person("Max Hofer")
him = Person("Barack Obama")
her = Person("Anna Schneider")

pList = [me, him, her]
for p in pList:
    print(p)

pList.sort()
for p in pList:
    print(p)
"""
