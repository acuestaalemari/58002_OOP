class TempConversion:
    def __init__(self, temp):
        self.temp = temp

    def FahrenheitToCelsius(self):
        return (self.temp - 32) * 5/9

    def KelvinToCelsius(self):
        return self.temp - 273.15

    def CelsiusToFahrenheit(self):
        return (self.temp * 9/5) + 32

    def KelvinToFahrenheit(self):
        return (self.temp - 273.15) * 9/5 + 32

    def CelsiusToKelvin(self):
        return self.temp + 273.15

    def FahrenheitToKelvin(self):
        return (self.temp - 32) * 5/9 + 273.15

    def get_conversions(self):
        print('Fahrenheit to Celsius:', self.FahrenheitToCelsius(), '°C')
        print('Kelvin to Celsius:', self.KelvinToCelsius(), '°C')
        print('Celsius to Fahrenheit:', self.CelsiusToFahrenheit(), '°F')
        print('Kelvin to Fahrenheit:', self.KelvinToFahrenheit(), '°F')
        print('Celsius to Kelvin:', self.CelsiusToKelvin(), 'K')
        print('Fahrenheit to Kelvin:', self.FahrenheitToKelvin(), 'K')

temp = float(input('Enter the temperature value: '))
temp_conv = TempConversion(temp)
temp_conv.get_conversions()