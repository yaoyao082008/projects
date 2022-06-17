class Stuff:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@company.com'
    def print_info(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print('$',self.pay)
    def get_first(self):
        return self.first
        


employee_1=Stuff('YaoYao','Xiong',100000)

print(employee_1.get_first())