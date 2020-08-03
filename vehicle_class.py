class Vehicle:
    color = "blue"
    
    #constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def __str__(self):
        return "My vehicle is a %d %s %s %s." % (self.year, self.color, self.make, self.model)

betsy = Vehicle("Nissan", "Murano", 2010)
print(betsy)