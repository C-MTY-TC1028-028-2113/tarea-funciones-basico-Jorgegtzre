def area(base,altura):
    a = base * altura
    return a

def area_prisma(base,altura,profundidad):
    ap = area(base,altura)*2+area(altura,profundidad)*2+area(base,profundidad)*2
    return ap


def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = area_prisma(b,a,p)

    print("El área total del prisma es:",r)

if __name__=='__main__':
    main()