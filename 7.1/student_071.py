class Student:
    def __init__(self, last, first, sid, modlist=[]):
        self.last = last
        self.first = first
        self.sid = sid
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def print_details(self):
        print('ID: {}'.format(self.sid))
        print('Surname: {}'.format(self.last))
        print('Forename: {}'.format(self.first))
        self.modlist = " ".join(self.modlist)
        print('Modules: {}'.format(self.modlist))
def main():

    student1 = Student('Murphy', 'Jimmy', 15234654)
    student1.add_module('CA117')
    student1.add_module('CA116')
    student1.add_module('CA114')
    student1.print_details()

    student2 = Student('Lannister', 'Cersei', 15876123, ['CA115', 'CA216'])
    student2.del_module('CA216')
    student2.del_module('CA117')
    student2.del_module('CA216')
    student2.add_module('CA117')
    student2.print_details()

if __name__ == '__main__':
    main()
