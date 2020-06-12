class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


class Battery():

    def __init__(self, battery_siez=75):

        self.battery_siez = battery_siez

    def describe_battery(self):

        print(
            f"Ten samochód ma akumulator o "
            f"pojemności {self.battery_siez} kWh.")

    def get_range(self):

        if self.battery_siez == 75:
            range = 260
        elif self.battery_siez == 100:
            range = 315

        print(f"Zasieg tego samochodu wynosi około {range} km"
              " po pełnym naładowaniu akumulatora")

    def upgrade_battery(self):
        if self.battery_siez != 100:
            self.battery_siez = 100


class ElectricCar(Car):

    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
