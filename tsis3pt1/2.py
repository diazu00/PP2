def fahrenheit_to_celsius(fahrenheit):
   
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Example usage:
fahrenheit_temperature = float(input("Enter the Fahrenheit temperature: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_result:.2f} Celsius.")
