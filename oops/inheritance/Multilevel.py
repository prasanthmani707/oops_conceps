class person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def info(self):
        print(f"name {self.name} age {self.age}")
class teacher(person):
    def __init__(self, name, age,subject):
        self.subject =subject
        super().__init__(name, age)
    def tech(self):
        print(f"name {self.name} subject {self.subject}")
class classteacher(teacher):
    def __init__(self, name, age, subject,room):
        self.room =room
        super().__init__(name, age, subject)        
    def ron(self):
        print(f"name {self.name} classroom {self.room}")
obj =classteacher("prasanth",20,"math","10-g")
obj.info()
obj.tech()
obj.ron()
