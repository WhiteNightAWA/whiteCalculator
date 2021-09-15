import math

pi = math.pi
log = math.log10
ln = math.log
sqrt = math.sqrt
sinh = math.sinh
cosh = math.cosh
tanh = math.tanh
power = math.pow


def sin(num):
    return round(math.sin(math.radians(num)), 15)


def asin(num):
    return round(math.degrees(math.atan(num)), 15)


def cos(num):
    return round(math.cos(math.radians(num)), 15)


def acos(num):
    return round(math.degrees(math.acos(num)), 15)


def tan(num):
    return round(math.tan(math.radians(num)), 15)


def atan(num):
    return round(math.degrees(math.atan(num)), 15)
