import tkinter
from tkinter import *
from tkinter import ttk


c0 = '#444466' #Preto
c1 = '#FEFFFF' #Branco
c2 = '#6F9FBD' #Azul
c3 = '#38576B' #Valor
c4 = '#403D3D' #Letra
c5 = '#E89613' #Laranja


janela = Tk()
janela.title('Conversor de Bases Numéricas')
janela.geometry('400x310')
janela.configure(bg=c1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190) #Linha no meio do projeto


#Dividir frames (Baixo/Cima)

frame_cima = Frame(janela, width=400, height=70, background=c2, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, background=c1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

#Config frame de cima

convert = Label(frame_cima, text= "Conversor de Base Numérica", relief=FLAT, anchor='center', font=('System 20'), bg=c2, fg=c1)
convert.place(x=10, y=15)


def converter():
    

    def num_to_dec(num, base):
        decimal = int(num, base)

        binario = bin(decimal)
        octal = oct(decimal)
        hexdecimal = hex(decimal)

        label_decimal['text'] = str(decimal)
        label_binario['text'] = str(binario[2:])
        label_octal['text'] = str(octal[2:])
        label_hexdecimal['text'] = str(hexdecimal[2:].upper())

    num = input_valor.get()
    base = combo.get()

    if base == 'BINÁRIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    elif base == 'HEXDECIMAL':
        base = 16
    
    num_to_dec(num, base)

#Config frame de baixo

#input

bases = ['BINÁRIO', 'OCTAL', 'DECIMAL', 'HEXDECIMAL']

combo = ttk.Combobox(frame_baixo, width=12, justify='center', font=('Ivy 12 bold'))
combo['values'] = (bases)           #combobox serve pra criar a caixinha de opções
combo.place(x=35, y=10)

input_valor = Entry(frame_baixo, width=9, justify='center', font=('',13), highlightthickness=1, relief='solid')
input_valor.place(x=160, y=10)

button_convert = Button(frame_baixo, command=converter, text= "CONVERTER", relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=c1, fg=c4)
button_convert.place(x=247, y=10)

#output

label_binario = Label(frame_baixo, text= "BINÁRIO", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=c5, fg=c1)
label_binario.place(x=35, y=60)
label_binario = Label(frame_baixo, text= "", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=c4)
label_binario.place(x=170, y=60)

label_octal = Label(frame_baixo, text= "OCTAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=c5, fg=c1)
label_octal.place(x=35, y=100)
label_octal = Label(frame_baixo, text= "", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=c4)
label_octal.place(x=170, y=100)

label_decimal = Label(frame_baixo, text= "DECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=c5, fg=c1)
label_decimal.place(x=35, y=140)
label_decimal = Label(frame_baixo, text= "", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=c4)
label_decimal.place(x=170, y=140)

label_hexdecimal = Label(frame_baixo, text= "HEXDECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=c5, fg=c1)
label_hexdecimal.place(x=35, y=180)
label_hexdecimal = Label(frame_baixo, text= "", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=c4)
label_hexdecimal.place(x=170, y=180)


janela.mainloop()