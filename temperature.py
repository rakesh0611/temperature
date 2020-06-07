#celsius to farenheit
temp = int(input("Enter Temperature in celsius :"))
def calculate(C):
    fahrenheit = 9/5 * C + 32
    print("F = {:.1f} °F".format(fahrenheit))
calculate(temp)