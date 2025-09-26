# A function that recives value as Celsius and returns the value as Fahrenheit

def convert_temp_to_fahrenheit(temp):
    return temp + 32

# User input message
print("\n Write a temperature in Celsius and recieve it back in Fahrenheit: \n")
temp = int(input())

print(f"{temp} Celsius in Fahrenheit will be {convert_temp_to_fahrenheit(temp)} 🥸")