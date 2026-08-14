#take inptu in celsius and print its equivalent in Fahrenheit and Kelvin.
#(Use explicit type conversion and arithmetic operators)

C=input("Enter the Temperature in Celsius")
convertedValue=float(C)

Fahrenheit = (convertedValue * (9/5)) + 32
print("Fahrenheit", Fahrenheit)

Kelvin= convertedValue + 273.15
print("Kelvin", Kelvin)
