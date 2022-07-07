def menu():
    print("bienvenidos")
    print("este programa brinda herramientas que permiten resolver algunos problemas que infostat no ")
    print("1- unidad 5""\n","2- unidad 6""\n","0-salir ")

### unidad 5
import math
class prob:
    def __init__(self, numero, probabilidad):
        self.numero = numero
        self.probabilidad = probabilidad

def cargar_vector(n):
    vec = [None] * n

    for i in range(len(vec)):
        print('-' * 60)
        numero = float(input("ingrese el numero x: "))
        probabilidad = float(input("ingrese la probabilidad: ")) * numero

        vec[i] = prob(numero,probabilidad)
    return vec

def distribucion_probabilidad(vec):
    esperanza = 0
    for i in range(len(vec)):
        a = vec[i].probabilidad
        esperanza += a

    return esperanza

def varianza(esperanza, vec):
    vari = 0
    for i in range(len(vec)):
        a =  vec[i].probabilidad * vec[i].numero
        vari += a
    varian = vari - (esperanza * esperanza)

    return varian

def desviación(var):
    a = math.sqrt(var)
    return a
#### unidad 6

def menú_modo():
    print("modo de operación:", "\n","1-calcular esperanza, varianza y desviación "
                                     "estandar para modelos: Bipuntual,binomial, hipergeometrica, poisson "," \n"
          "2- distribución para la proporción muestral, su esperanza, varianza y su desviación estandar ", "0- salir del modo")

def menu_1():
    print("1- Bipuntual \n")
    print("2- Binomial \n")
    print("3- Hipergeometrica \n")
    print("4- Poisson \n")


def menu_2():
    print("1- probabilidad con MCR- binomial ")
    print("2- probabilidad con MSR- Hipergeometrica ")


def bipuntual(p, q):
    esperanza = p
    varianza = p*q
    ds= math.sqrt(varianza)
    print("esperanza: ",esperanza, "|", "varianza: ", varianza,"|" , "desviación: ", ds)


def binomial(n, p):
    q = 1-p
    esperanza = n*p
    varianza = n*p*q

    ds = math.sqrt(varianza)
    print("esperanza: ",esperanza, "|", "varianza: ", varianza,"|" , "desviación: ", ds)


def hipergeometica(n1, n, k):
    esperanza = n * (k/n1)
    varianza = ((n1-n)/(n1-1)) * esperanza * (1-(k/n1))


    print("varianza =", varianza)
    ds = math.sqrt(varianza)
    print("esperanza: ",esperanza, "|", "varianza: ", varianza,"|" , "desviación: ", ds)


def poisson(n, p):
    esperanza = n*p

    ds= math.sqrt(esperanza)
    print("esperanza: ",esperanza, "|", "varianza: ", esperanza,"|" , "desviación: ", ds)




class prob:
    def __init__(self, numero, probabilidad):
        self.numero = numero
        self.p_sombrerito = probabilidad


def combinacional (i,n):


    combi = math.factorial(n)/ (math.factorial (i) * math.factorial(n-i))
    return combi


def calcular_p_elevado(w,pro):
    a = 1

    if w == 0:

        return a

    for i in range(w):
        a *= pro

    return a


def calcular_q_elevado(x,pro,n):
    q = 1-pro
    qelevada =1
    if n-x == 0:

        return qelevada

    for i in range(n-x):
        qelevada *= q

    return qelevada


def cargar_vector():
    muestra = int(input("ingrese el tamaño de la muestra "))
    n = int(input("ingrese la cantidad de pruebas (n): "))
    x = muestra+1
    vec = [None] * x

    pro = float(input("ingrese su probabilidad: "))


    for i in range(len(vec)):

        print('-' * 60)


        p = i/n

        p_sombrerito= combinacional(i,n) * calcular_p_elevado(i,pro) * calcular_q_elevado(i, pro, n)


        vec[i] = prob(p ,p_sombrerito)

    return vec, n, pro

def mostrar_vector(vec):
    for i in range(len(vec)):
        print("para ", vec[i].numero, "tenemos la probabilidad de ",vec[i].p_sombrerito )


def calcular_cosas_binomial(p,n):
    esperanza = p
    varianza = (p*(1-p))/n
    ds = math.sqrt(varianza)
    print("esperanza: ",esperanza, "|", "varianza: ", varianza,"|" , "desviación: ", ds)


def hipergeometrica():
    n = int(input("ingrese el tamaño de la muestra "))
    n1 = int(input("ingrese la población (N): "))
    x = n+1
    vec = [None] * x
    pro = float(input("ingrese su probabilidad: "))
    k = int(input("ingrese su k"))

    for i in range(len(vec)):

        print('-' * 60)


        p = i/n

        p_sombrerito1= combinacional(i,k) *  combinacional((n-i), (n1-k)) / combinacional(n,n1)
        stepper = 10.0 ** 4
        p_sombrerito=math.trunc (stepper*p_sombrerito1)/stepper


        vec[i] = prob(p ,p_sombrerito)

    return vec,n,pro,n1


def calcular_cosas_hipergeometrica(n,pro,n1):
    esperanza= pro
    varianza1 = ((pro*(1-pro))/n) * ((n1-n)/(n1-1))
    stepper = 10.0 **4
    varianza = math.trunc(stepper*varianza1)/stepper
    ds = math.sqrt(varianza)
    print("esperanza: ",esperanza, "|", "varianza: ", varianza,"|" , "desviación: ", ds)





def principal():
    menu()
    unidad = int(input("ingrese la unidad a trabajar "))
    while unidad!=0:
        if unidad ==5 or unidad == 1:
            l = int(input("ingrese la cantidad de variables: "))
            vec = cargar_vector()
            a = distribucion_probabilidad(vec)
            varrr= varianza(a,vec)
            desv = desviación(varrr)
            print("esperanza: ",a, "|", "varianza: ", varrr,"|" , "desviación: ", desv)
        elif unidad == 2 or unidad == 6:
            def princ():
                menú_modo()
                modo = int(input("ingrese el modo que quiere trabajar: "))
                while modo !=0:
                    if modo ==1:
                        menu_1()
                        mood = int(input("ingrese que modelo quiere utilizar: "))
                        if mood ==1:
                            p = float(input("ingrese su P: "))
                            q = 1-p
                            bipuntual(p,q)
                        elif mood ==2:
                            n = float(input("ingrese su n: "))
                            p = float(input("ingrese su P: "))
                            binomial(n,p)
                        elif mood == 3:
                            n1 = int(input("ingrese su población (N): "))
                            n= int(input("ingrese su muestra (n): "))
                            k = int(input("ingrese su cantidad de exitos en la población (k): "))
                            hipergeometica(n1,n,k)
                        elif mood == 4:
                            n = float(input("ingrese su n: "))
                            p = float(input("ingrese su P: "))
                            poisson(n,p)
                        else:
                            int(input("ingrese una opción valida"))
                    elif modo ==2:
                        menu_2()
                        b = int(input("ingrese su opción: "))
                        if b == 1:
                            vector, n, p = cargar_vector()
                            mostrar_vector(vector)
                            calcular_cosas_binomial(p,n)
                        if b ==2:
                            vector,n,k,n1= hipergeometrica()
                            mostrar_vector(vector)
                            calcular_cosas_hipergeometrica(n,k,n1)


                    else:
                        print("ingrese una opción vailda")

                    print()
                    print(("-*")*60)
                    menú_modo()
                    modo = int(input("ingrese el modo a operar: "))

            princ()
        else:
            print("elija una de las opciones de unidad entre las permitidas")

        print()
        print(("-*")*60)
        menu()
        unidad = int(input("ingrese la unidad a trabajar "))
    print("buena suerte")

principal()
