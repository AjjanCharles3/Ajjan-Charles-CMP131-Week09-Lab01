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
