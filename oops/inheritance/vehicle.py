class Vehicles:
    def __init__(self,cc):
        self.cc =cc
      
    def information (self):
        if self.cc <= 125:
            print(f"lowest cc vehicle")
        elif(self.cc <= 250):
            print(f"medium level vehicle")
        else:
            print("high level vehicle")
class cc(Vehicles):
    def __init__(self, brand, cc, milage, speed):
        super().__init__(cc)    
        self.brand =brand
        self.milage=milage
        self.speed =speed   
    def display(self):
        print(f"brand {self.brand}")
        print(f"bike milage {self.milage}")
        print(f"speed of bike {self.speed}")
        self.information()
bike =cc("honda",180,60,180)
bike.display()
        
          

