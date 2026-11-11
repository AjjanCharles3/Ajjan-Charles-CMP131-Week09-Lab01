#charles Ajjan
#cmp-131
#week09
#lab01
#celsius temperature table
#start date - 11/06/2026
def celsius(fahrenheit):
    cel = (fahrenheit - 32) * 0.5555556
    return cel
def display (cel,fahrenheit):
    print("Fahrenheit",fahrenheit,"The converted Temperature is:","Celsius", cel)

def main():
    for fahrenheit in range(21):
        celsius(fahrenheit)
    fahrenheit = float(input("Enter Temperature in Fahrenheit"))
   # celsius = (fahrenheit - 32) * 0.55555556
    cel=celsius(fahrenheit)
    display(cel,fahrenheit)
main() 