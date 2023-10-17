class Temperature:
    def __init__(self, fahrenheit=0.0):
        self.__fahrenheit = fahrenheit

    def get_fahrenheit(self):
        return self.__fahrenheit

    def set_fahrenheit(self, fahrenheit):
        if fahrenheit < -459.67:  # Absolute zero in Fahrenheit
            raise ValueError("Temperature cannot go below absolute zero in Fahrenheit.")
        self.__fahrenheit = fahrenheit

    def get_celsius(self):
        celsius = (self.__fahrenheit - 32) * 5/9
        return celsius

    def set_celsius(self, celsius):
        if celsius < -273.15:  # Absolute zero in Celsius
            raise ValueError("Temperature cannot go below absolute zero in Celsius.")
        self.__fahrenheit = (celsius * 9/5) + 32

    def __str__(self):
        return f"{self.__fahrenheit}°F ({self.get_celsius()}°C)"

# Example usage:
temp = Temperature(32)  # Initialize with 32°F
print(temp)  # Output: "32.0°F (0.0°C)"

temp.set_celsius(25)  # Set temperature to 25°C
print(temp)  # Output: "77.0°F (25.0°C)"

temp.set_celsius(30)
print(temp)
