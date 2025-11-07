class employee:
    def __init__(self,employee,brange,salary):
        self.employee=employee
        self.__salary =salary
        self.brange =brange
    def set_salary (self,salary):
        if salary >= self.__salary:
            self.__salary=salary
            print(f"employee brange {self.brange} \nmaneger setted salary {self.__salary}")
        else:
            print(f"not setted salary")
    def get_salary(self):
        return print(f"salry of employee {self.__salary:,.2f}")
employe =employee("8071252","kVB",4000)
employe.set_salary(5000)
employe.get_salary()
