class Solider:
    def __init__(self,fullname:str,gender:str,age:int,height:int,weight:int):
        self.fullname=fullname
        self.gender=gender
        self.age=age
        self.height=height
        self.weight=weight
    def getinfo(self):
        return f"""
Fullname:{self.fullname}
Gender:  {self.gender}
Age:     {self.age}
Height:  {self.height}
Weight:  {self.weight}
"""
class Army(Solider):
    def __init__(self, fullname: str, gender: str, age: int, height: int, weight: int):
        super().__init__(fullname, gender, age, height, weight)
    def __str__(self):
        if self.age>18 and self.gender=="Male" or self.gender=="male":
            return super().getinfo()
    def sep(self):
        if self.height<150 and self.weight<75:
            return super().getinfo()
    def sep1(self):
        if self.height>150 and self.weight>75:
            return super().getinfo()
list=[]
n=int(input("Nechta askar ma'lumotini kiritmoqchisiz: "))
for i in range(n):
    name=input("\nFullname: ")
    gender=input("Gender: ")
    age=int(input("Age: "))
    height=int(input("Height"))
    weight=int(input("weight"))
    s1=Army(name,gender,age,height,weight)
    list.append(s1)
print("List of Male Soliders who are older than 18")
for i in list:    
    print(i.__str__())
print("Piyoda qo'shinlari ga tavsiya etildi")
for i in list:
    print(i.sep())
print("Tank qo'shin lariga tavsiya etildi")
for i in list:
    print(i.sep1())