def area(base,altura):
    a = base*altura
    return a

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))

    r = area(b,a)

    print("El área del rectángulo es:",r)

if __name__=='__main__':
    main()