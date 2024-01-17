class transport:
    def __init__(self,brand:str,model:str,color:str):
        self.brand=brand
        self.model=model
        self.color=color
    def getinfo(self):
        return f"""
Brand:{self.brand}
Model:{self.model}
Color:{self.color}
"""
class car(transport):
    def __init__(self,brand:str, model:str, color:str,speed:int,seatcount:int,manfacturedate:int):
        super().__init__(brand, model, color)
        self.speed=speed
        self.seatcount=seatcount
        self.manfacturedate=manfacturedate
    def info(self):
        s=super().getinfo()+f"""Top speed:{self.speed} km \nSeats:{self.seatcount}\nManufactured Date:{self.manfacturedate}\n"""
        print(s)
class truck(transport):
    def __init__(self, brand: str, model: str, color: str,weightc:int):
        super().__init__(brand, model, color)
        self.weightc=weightc
    def info(self):
        a=super().getinfo()+f"""Weight Capacity:{self.weightc}Tone
"""
        print(a)
v=transport("Volvo","VNL","White")
car1=car("Volvo","VNL","White",330,2,2018)
car1.info()
t=truck("Volvo","VNL","White",5)
t.info()