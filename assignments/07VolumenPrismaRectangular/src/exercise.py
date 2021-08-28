# Escribe aquí tus funciones...
def area_rectangulo(largo, ancho):
    a = largo * ancho
    return a


def volumen_prisma(largo, ancho, altura):
    v = area_rectangulo(largo, ancho) * altura
    return v

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = volumen_prisma(b,a,p)

    print("El volumen del prisma es:",r)

if __name__=='__main__':
    main()