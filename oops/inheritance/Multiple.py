class boy:
    def __init__(self,name):
        self.name =name
class ag:
    def __init__(self,age):
        self.age =age        
class parent(boy,ag):
    def __init__(self, name,age,student):
        self.student =student
        boy.__init__(self,name)
        ag.__init__(self,age)
    def info(self):
        print(f"name {self.name} age {self.age} student {self.student}")
obj = parent("prasanth",20,"yes")
obj.info()
