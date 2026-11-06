#charles Ajjan
#cmp-131
#week09
#lab01
#celsius temperature table
#start date - 11/06/2026
def celsius(fahrenheit):
    cel = (fahrenheit - 32) * 0.5555556
    return cel
def display (cel):
    print("The converted Temperature is:", cel)

def main():
    fahrenheit=float(input("enter temperature in fahrenheit"))
   # celsius = (fahrenheit - 32) * 0.55555556
    cel=celsius(fahrenheit)
    display(cel)
main() 