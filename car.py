"""
Zestaw klas przeznaczonych do zaprezentowania samochodu,
zarówno o napędzie rtadycyjnym, jak i elektrycznym.
"""


class Car():

    "Prosta prośba zaprezentowania samochodu"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu"""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """
        Przypisanie podanej wartości licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu")

    def increment_odometer(self, kilometers):
        """Inkrementracja wartości licznika przebiegu samochodu o podaną
        wartość."""
        self.odometer_reading += kilometers


class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego"""

    def __init__(self, battery_siez=75):
        """Inicjalizacja atrybutów akumulatora."""
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
