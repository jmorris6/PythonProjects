class Odometer:
    def __init__(self):
        self.milesDriven = 0
        self.fuelEfficiency = 0

    def resetOdomoter(self):
        self.milesDriven = 0

    def setfuelEfficiency(self, fuelEfficiency):
        self.fuelEfficiency = fuelEfficiency

    def addMiles(self, miles):
        self.milesDriven += miles
    
    def gallonsUsed(self):
        return self.milesDriven / self.fuelEfficiency

def info(odometer):
    print("Miles driven: " + str(odometer.milesDriven))
    print("Fuel Efficiency: " + str(odometer.fuelEfficiency))
    print("Gallons of Gas used: " + str(odometer.gallonsUsed()))
odometer = Odometer()
odometer.setfuelEfficiency((300/11))
odometer.addMiles(300)
info(odometer)
odometer.setfuelEfficiency((500/20.5))
odometer.addMiles(500)
info(odometer)
odometer.resetOdomoter()
odometer.setfuelEfficiency(250/5.7)
odometer.addMiles(250)
info(odometer)
