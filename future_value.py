#charles Ajjan
#cmp-131
#week09
#lab01
#Future Value
#date - 11/06/2026
def future_value (P,i,t):
    F = P * (1 + i)**t
    return (F)
def display (F):
    print("The future value is",F)

def main():
    P=(int(input("Enter Present Value")))
    i=(float(input("Enter Monthly Interest Rate")))
    t=(int(input("Enter Number of Months")))
    F=future_value(P,i,t,)
    display (F)
main()