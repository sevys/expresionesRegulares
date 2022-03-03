from tkinter import *
import re
import os

#192.168.1.69

def ip():
    # aqui ponemos el metodo que va a llamar a los otros
    cadenaEntrante = entrada.get()

    if cadenaEntrante[1] == '0': 
        a()
    elif cadenaEntrante[1] == '7':
        b()
    elif cadenaEntrante[1] == '9':
        c()


def a():
     candenaA = re.compile("(^(10)(\.([2]([0-5][0-5]|[01234][6-9])|[1][0-9][0-9]|[1-9][0-9]|[0-9])){3})")
     result = re.fullmatch(candenaA, entrada.get())

     if result == None:
        print('Su IP no corresponde con el rango')
     else:
        print('''
        ---------------------------------------------------------
                        SU IP CORRESPONDE
                    CLASE: A
        ---------------------------------------------------------''')
        os.system(f'ping {entrada.get()}')



def b():
    cadenaB = re.compile("(^(172)\.(1[6-9]|2[0-9]|3[0-1])(\.(2[0-4][0-9]|25[0-5]|[1][0-9][0-9]|[1-9][0-9]|[0-9])){2})")
    result = re.fullmatch(cadenaB, entrada.get())

    if result == None:
        print('Su IP no corresponde con el rango')
    else:
        print('''
        ---------------------------------------------------------
                        SU IP CORRESPONDE
                    CLASE: A
        ---------------------------------------------------------

        ''')
        os.system(f'ping {entrada.get()}')


def c():
    cadenaC = re.compile("(^(192)\.(168)(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2})")
    result = re.fullmatch(cadenaC, entrada.get())

    if result == None:
        print('Su IP no corresponde con el rango')
    else:
        print('''
        ---------------------------------------------------------
                        SU IP CORRESPONDE
                    CLASE: A
        ---------------------------------------------------------

        ''')
        os.system(f'ping {entrada.get()}')


ventana = Tk()
ventana.geometry('400x300')


#declaramos variables para obtener los datos 
entrada = StringVar()
salida = StringVar()



#declaramos un label para poner halgo
labe1 = Label(ventana, text='Valida tu IP')
labe1.place(x= 110, y= 20)
labelResultado = Label(ventana, textvariable=salida)
labelResultado.place(x = 100, y = 160)


#declaramos el cuadro de texto
cuadro = Entry(ventana, textvariable=entrada)
cuadro.place(x= 110, y= 40)


#declaramos el boton
boton = Button(ventana, text='calcular', command=ip)
boton.place(x=160, y=80)



def main():
    ventana.mainloop()


if __name__ == '__main__':
    main()
#las devdependencias, se utilizan cuando se esta desarollando el proyecto, 
#las dependence: se utilizan para que el proyecto funcione
