# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
        
        
#     def info(self):
#         print(f"Модель - {self.model}, Год выпуска - {self.year}")
        
# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self,model, year)
#         self.battery = battery
        
        
#     def drive(self):
#         print(f"Мишина - {self.model} едет на электричестве")
        
        
# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self,model, year)
#         self.fuel_bank = fuel_bank
        
        
#     def drive(self):
#         print(f"Мишина - {self.model} едет на топливе")
        
        
        
# class HybridCar(ElectricCar,FuelCar):
#     def __init__(self, model, year, battery, fuel_bank, speed):
#         super().__init__(model, year, battery)
#         FuelCar.__init__(self,model, year, fuel_bank)
#         self.speed = speed
        
        
#     def drive(self):
#         if self.speed > 60:
#             FuelCar.drive(self)
#         else:
#             ElectricCar.drive(self)
                


# tesla = ElectricCar("Tesla - Model X", 2024, 90)
# tesla.info()
# tesla.drive()


# matiz = FuelCar("Matiz - 3 ", 2020, 30)
# matiz.info()
# matiz.drive()


# lexus = HybridCar("Lexus - es300 ", 2020, 40, 60, 50)
# lexus.info()
# lexus.drive()


## МАГИЧЕСКИЙ МЕТОД


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year          
        
    def __str__(self):
        return f"Модель - {self.model}, Год выпуска - {self.year}"
    
    
    def __add__(self, other):
        res = self.year + other.year
        return Car(self.model, res)
    
        
    def __sub__(self, other):
        res = self.year - other.year
        return Car(self.model, res)
    
            
    def __mul__(self, other):
        res = self.year * other.year
        return Car(self.model, res)
    
    
    def __call__(self):
        print("hello call")
        
                
    def __floordiv__(self, other):
        res = self.year // other.year
        return Car(self.model, res)
    
    def __truediv__(self, other):
        res = self.year / other.year
        return Car(self.model, res)
    
    def __gt__(self, other):
        return self.year > other.year
    
        
    def __lt__(self, other):
        return self.year < other.year
    
            
    def __eq__(self, other):
        return self.year == other.year
    
    def __ne__(self, other):
        return self.year != other.year
    
        
    def __ge__(self, other):
        return self.year >= other.year
    
    def __le__(self, other):
        return self.year <= other.year
    
   
        
bmw = Car("BMW - m5", 2022)
mers = Car("BMW - m5", 2022)

# print(bmw * mers)
# print( bmw + mers)
# print( bmw // mers)
# print( bmw / mers)
# print( bmw > mers)
# print( bmw < mers)
# print( bmw == mers)
# print( bmw != mers)
print( bmw >= mers)
print( bmw <= mers)


