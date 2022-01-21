from enum import Enum
from typing import Union


class Scale(Enum):
    CELSIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'


class TemperatureScaleException(Exception):
    pass


def _check_limit(degrees, scale):
    return not (scale == 'K' and degrees < 0) or \
           (scale == 'C' and degrees < -273.15) or (scale == 'F' and degrees < -459.67)


class TemperatureScale:

    def __init__(self, degrees: Union[float, int], scale: str):
        if not (isinstance(degrees, float) or isinstance(degrees, int)):
            raise TemperatureScaleException("Degrees should be float type")

        try:
            self.scale = Scale(scale)
        except ValueError:
            raise TemperatureScaleException("Your scale is wrong. Can be: C, F, K")
        if _check_limit(degrees, scale):
            self.degrees = degrees
        else:
            raise TemperatureScaleException("You have reached absolute zero. Impossible.")

    def to_kelvin(self):
        k_degrees = self.degrees
        if self.scale == Scale.CELSIUS:
            k_degrees = self.degrees + 273.15
        elif self.scale == Scale.FAHRENHEIT:
            k_degrees = (self.degrees - 32) * 5/9 + 273.15
        if _check_limit(k_degrees, 'K'):
            self.scale = Scale.KELVIN
            self.degrees = k_degrees
            return self.degrees
        else:
            raise TemperatureScaleException("You have reached absolute zero. Impossible.")

    def to_fahrenheit(self):
        f_degrees = self.degrees
        if self.scale == Scale.KELVIN:
            f_degrees = (self.degrees - 273.15) * 9/5 + 32
        elif self.scale == Scale.CELSIUS:
            f_degrees = (self.degrees * 9/5) + 32
        if _check_limit(f_degrees, 'F'):
            self.scale = Scale.FAHRENHEIT
            self.degrees = f_degrees
            return self.degrees
        else:
            raise TemperatureScaleException("You have reached absolute zero. Impossible.")

    def to_celsius(self):
        c_degrees = self.degrees
        if self.scale == Scale.KELVIN:
            c_degrees = self.degrees - 273.15
        elif self.scale == Scale.FAHRENHEIT:
            c_degrees = (self.degrees - 32) * 5/9
        if _check_limit(c_degrees, 'C'):
            self.scale = Scale.CELSIUS
            self.degrees = c_degrees
            return self.degrees
        else:
            raise TemperatureScaleException("You have reached absolute zero. Impossible.")

    def __str__(self):
        return f"Scale: {self.scale.name}, Degrees: {self.degrees}"


if __name__ == '__main__':
    temperature = TemperatureScale(0, 'C')
    temperature.to_fahrenheit()
    print(temperature)  # >>> Scale: FAHRENHEIT, Degrees: 32.0
    temperature.to_kelvin()
    print(temperature)  # >>> Scale: KELVIN, Degrees: 273.15
    wrong_temperature = TemperatureScale(-1, 'K')  # >>> You have reached absolute zero. Impossible.
