class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def __init__(self, name):
        Lecturer.__init__(self, name)
        self.name = "Prof. " + name
        self.temp = name

    def say(self, stuff):
        return self.name + ' says: ' + Lecturer.lecture(Lecturer(self.temp), stuff)

    def lecture(self, stuff):
        return 'I believe that ' + self.temp + ' says: ' + stuff


class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + " says: It is obvious that " + Lecturer.lecture(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


# Prof. eric says: I believe that eric says: the sky is blue
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue
e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

print pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue

print ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue
