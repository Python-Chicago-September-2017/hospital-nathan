class Patient(object):
    id_number = 1
    def __init__(self,name,allergies,bed_number = None):
        self.id_number = Patient.id_number
        Patient.id_number += 1
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

class Hospital(object):
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = range(1,capacity+1)
    def admit(self,new_person):
        if len(self.patients) == self.capacity:
            print str(self.name) + " is full"
        else:
            self.patients.append(new_person)
            new_person.bed_number = min(self.beds)
            self.beds.remove(new_person.bed_number)
            print str(new_person.name) + " was admitted to " + str(self.name)
            # print new_person.bed_number
            # print self.beds
        return self
    def discarge(self,discarge_person):
        for person in self.patients:
            if person.name == discarge_person.name:
                self.beds.append(person.bed_number)
                self.patients.remove(person)
                person.bed_number = None
                print str(discarge_person.name) + " was discarged from " + str(self.name)
                # print person.bed_number
                # print self.beds
            else:
                print "No one by the name of " + str(discarge_person.name) + " is at " + str(self.name)
        return self

nathan = Patient("Nathan","Milk")
sarah = Patient("Sarah","Cats")
tyler = Patient("Tyler","Grass")

Hospital("Saint Someone Hospital",2).admit(nathan).admit(sarah).discarge(nathan).admit(tyler).admit(nathan)