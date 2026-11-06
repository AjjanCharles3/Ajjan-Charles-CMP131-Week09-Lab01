#charles Ajjan
#cmp-131
#week09
#lab01
#Kinetic Energy
#date - 11/06/2026
def kinetic_energy(m,v):
        ke=0.5*m*v*v 
        return ke
def display (ke):
        print("the value of kinetic energy is", ke)

def main():
        m=float(input("enter mass"))
        v=float(input("enter velocity"))
        ke= kinetic_energy (m,v)
        display(ke)
main()
