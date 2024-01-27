
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