class Binusmaya:
    def __init__(self):
        self.Lecturers = ['zhandos', 'scientific computing', 'A2005']
        self.Classes = ['L1AC', 'L1BC', 'L1CC']
        self.Schedules = []

# add lecturers
def add_lecturer(self, name, subject, lecturerID):
    for lecturer in self.Lecturers:
        if lecturer['subject'] == subject:
            print('a lecturer for this subject already exists')
            return
    self.Lecturers.append({'name': name, 'subject': subject, 'lecturerID': lecturerID})
    print('this lecturer has been sucessfully added')

# remove lecturer
def remove_lecturer(self, lecturerID):
    for lecturer in self.Lecturers:
        if lecturer['lecturerID'] == lecturerID:
            self.Lecturers.remove(lecturer)
            print('this lecturer has been successfully removed')
            return
    print('this lecturer does not exist')

# add class
def add_class(self, class_code):
    if class_code in self.Classes:
        print('this class code already exists')
    else:
        self.Classes.append(class_code)
        print('this class code has been sucessfully added')

#remove class
def remove_class(self, class_code):
    if class_code in self.Classes:
        self.Classes.remove(class_code)
        print('this class code has been sucessfully removed')
    else:
        print('this class code does not exist')

# add schedule
def add_schedule(self, class_code, time, subject):
    for lecturer in self.Lecturers:
            if lecturer['subject'] == subject:
                lecturer_name = lecturer['name']
                break
    if not lecturer_name:
        print('no lecturer found')
        return
    for schedule in self.Schedules:
        if schedule[2] == subject:
            print('this subject already has a schedule')
            return
    self.Schedules.append((time, class_code, subject, lecturer_name))
    print('this schedule has been successfully added')