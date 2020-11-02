class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('name deleted')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp1 = Employee('jno', 'dzbno', 69)
print(emp1.email)
emp1.first = 'jano'
print(emp1.email)

emp1.fullname = 'jano dzbano'
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)

'''
TEST ZONE


dev_1 = Developer('Corey', 'Schafer', 50, 'Python')
dev_2 = Developer('Test', 'Employee', 60, 'Java')


print(repr(dev_1))
print(str(dev_1))


mgr_1 = Manager('Sue', 'Carry', 100, [dev_1, dev_2])
mgr_1.add_emp(dev_2)
mgr_1.print_emp()

emp_str1 = 'johnnie-duo-70'
emp_str2 = 'mary-jane-90'
emp_str3 = 'abudl-ahmed-20'

new_emp1 = Employee.from_string(emp_str2)
print(new_emp1.__dict__)

import datetime
my_date = datetime.date(2020, 11, 2)
print(Employee.is_workday(my_date))

print(help(Manager))

'''
