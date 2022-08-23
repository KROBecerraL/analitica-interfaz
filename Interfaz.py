import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

#Carolina Becerra Londoño y Miguel Mateo Mendoza Rojas

plot.clf()
plot.close('all')

archivo='abalone.csv'
abaData = pd.read_csv(archivo)
abaDataOG = pd.read_csv(archivo)
Nombre_columnas=['Sex',
                 'Length',
                 'Diameter',
                 'Height',
                 'Whole weight',
                 'Shucked weight',
                 'Viscera weight',
                 'Shell weight',
                 'Rings',]
abaData.columns=Nombre_columnas
abaDataOG.columns=Nombre_columnas

interfaz = tk.Tk()
interfaz.title("Interfaz - Abalone")
interfaz.geometry("1300x590")

#variables seleccionadas para las graficas
variable1 = ""
variable2 = ""
    
def sel():
    print(var.get())

#Función para buscar cuántos checkboxes están seleccionados en variables
def btnCheck02(varCnt):
    checkCount=0
    global variable1
    global variable2
    if var2.get() == 1:
        checkCount+=1
        variable1 = "Length"
    if var3.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Whole weight"
        elif (variable2 == ""):
            variable2 = "Whole weight"
    if var4.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Shell weight"
        elif (variable2 == ""):
            variable2 = "Shell weight"
    if var5.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Diameter"
        elif (variable2 == ""):
            variable2 = "Diameter"
    if var6.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Shucked weight"
        elif (variable2 == ""):
            variable2 = "Shucked weight"
    if var7.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Rings"
        elif (variable2 == ""):
            variable2 = "Rings"
    if var8.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Height"
        elif (variable2 == ""):
            variable2 = "Height"
    if var9.get() == 1:
        checkCount+=1
        if (variable1 == ""):
            variable1 = "Viscera weight"
        elif (variable2 == ""):
            variable2 = "Viscera weight"
    print(checkCount)
    if (checkCount == varCnt):
        print("Correcto, puede graficarse")
        if (varCnt == 1):
            variable2 == ""
        return 1
    else:
        print("Error, no se escogio el numero correcto de variables")
        messagebox.showerror(title="ERROR", message="No se escogio el número correcto de variables")
        variable1 = ""
        variable2 = ""
        return 0

#Boton de regresiones
def btnRegresion():
    global variable1
    global variable2
    plot.clf()
    plot.close('all')
    if var.get() == "Radio 5":
        print("Regresion Lineal")
        possibleCreation = regresionCheck01()
        possibleCreation2 = regresionCheck02()
        #Si ambas son 1 se grafica, sino no
        print(possibleCreation)
        print(possibleCreation2)
        if (possibleCreation == 1) and (possibleCreation2 == 1):
            print("Puede graficarse")
            x = np.array(abaData[variable1])
            y = np.array(abaData[variable2])
            b = estimate_coef(x, y)
            FIG = plot_regression_line(x, y, b)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
            variable2 = ""
    elif var.get() == "Radio 6":
        print("Regresion Logistica")
        possibleCreation = regresionCheck01()
        possibleCreation2 = regresionCheck02()
        #Si ambas son 1 se grafica, sino no
        print(possibleCreation)
        print(possibleCreation2)
        if (possibleCreation == 1) and (possibleCreation2 == 1):
            print("Puede graficarse")
    else:
        print("No eligió la opción de regresión. No se grafica nada")

#Funcion para buscar qué variables se eligieron para regresiones
def regresionCheck01():
    checkCount=0
    global variable1
    global variable2
    if regEntry1.get() == 1:
        checkCount+=1
        variable1 = "Length"
    if regEntry2.get() == 1:
        checkCount+=1
        variable1 = "Diameter"
    if regEntry3.get() == 1:
        checkCount+=1
        variable1 = "Height"
    if regEntry4.get() == 1:
        checkCount+=1
        variable1 = "Whole weight"
    if regEntry5.get() == 1:
        checkCount+=1
        variable1 = "Shucked weight"
    if regEntry6.get() == 1:
        checkCount+=1
        variable1 = "Viscera weight"
    if regEntry7.get() == 1:
        checkCount+=1
        variable1 = "Shell weight"
    if regEntry8.get() == 1:
        checkCount+=1
        variable1 = "Rings"
    print(checkCount)
    if (checkCount == 1):
        print("Correcto, puede graficarse")
        return 1
    else:
        print("Error, no se escogio el numero correcto de variables")
        messagebox.showerror(title="ERROR", message="No se escogio el número correcto de variables")
        variable1 = ""
        variable2 = ""
        return 0
    
def regresionCheck02():
    checkCount=0
    global variable1
    global variable2
    if regOut1.get() == 1:
        checkCount+=1
        variable2 = "Length"
    if regOut2.get() == 1:
        checkCount+=1
        variable2 = "Diameter"
    if regOut3.get() == 1:
        checkCount+=1
        variable2 = "Height"
    if regOut4.get() == 1:
        checkCount+=1
        variable2 = "Whole weight"
    if regOut5.get() == 1:
        checkCount+=1
        variable2 = "Shucked weight"
    if regOut6.get() == 1:
        checkCount+=1
        variable2 = "Viscera weight"
    if regOut7.get() == 1:
        checkCount+=1
        variable2 = "Shell weight"
    if regOut8.get() == 1:
        checkCount+=1
        variable2 = "Rings"
    print(checkCount)
    if (checkCount == 1):
        print("Correcto, puede graficarse")
        return 1
    else:
        print("Error, no se escogio el numero correcto de variables")
        messagebox.showerror(title="ERROR", message="No se escogio el número correcto de variables")
        variable1 = ""
        variable2 = ""
        return 0

#Función para buscar cuál de las opciones escogió en los RadioButton de tipo de gráfica
#varCount es el número de Checkboxes que podrá seleccionar en  la siguiente categoría de variables
def btnCheck00():
    global variable1
    global variable2
    plot.clf()
    plot.close('all')
    if var.get() == "Radio 1":
        print("Histograma")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            histograAtipicos(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 2":
        print("Cajas y bigotes")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            cajasbigotesAtipicos(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 3":
        print("Normalizacion")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = normalizacionAtipicos(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 4":
        print("Scatter")
        varCount=2
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            scatterAtipicos(variable1, variable2)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
            variable2 = ""
    else:
        messagebox.showerror(title="ERROR", message="No escogio ninguna gráfica valida para este botón.")
    
def btnCheck01():
    global variable1
    global variable2
    plot.clf()
    plot.close('all')
    if var.get() == "Radio 1":
        print("Histograma")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            histogra(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 2":
        print("Cajas y bigotes")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            cajasbigotes(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 3":
        print("Normalizacion")
        varCount=1
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            normalizacion(variable1)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
    elif var.get() == "Radio 4":
        print("Scatter")
        varCount=2
        print(varCount)
        possibleCreation = btnCheck02(varCount)
        #Si es 1 se grafica, sino no
        print(possibleCreation)
        if (possibleCreation == 1):
            FIG = plot.figure()
            FIG.add_subplot(111)
            scatter(variable1, variable2)
            canva = FigureCanvasTkAgg(FIG,master=interfaz)
            canva.draw()
            canva.get_tk_widget().place(x=700,y=100)
            variable1 = ""
            variable2 = ""
    else:
        messagebox.showerror(title="ERROR", message="No escogió ninguna gráfica valida para este botón.")
        
#Función mostrar ventana de histograma
def histogra(varColumn):
    finalPlot = plot.hist(x=abaDataOG[varColumn])
    plot.title('HISTOGRAMA - ' +varColumn)
    plot.xlabel('Datos')
    plot.ylabel('Frecuencia')
    variable1 = ""
    variable2 = ""
    #La variable finalPlot almacena la gráfica
    
def histograAtipicos(varColumn):
    values = abaData[varColumn]
    cuartil1 = np.percentile(values,25)
    cuartil3 = np.percentile(values,75)
    iqr = cuartil3 - cuartil1
    li = cuartil1 - (float(alfa.get())*iqr)
    liS = cuartil3 + (float(alfa.get())*iqr)
    noAtipicos = abaData.loc[(abaData[varColumn] > li) & (abaData[varColumn] < liS)]
    finalPlot = plot.hist(x=noAtipicos[varColumn])
    plot.title('HISTOGRAMA SIN OUTLIERS- ' +varColumn)
    plot.xlabel('Datos')
    plot.ylabel('Frecuencia')
    variable1 = ""
    variable2 = ""
    
#Función mostrar ventana de cajas y bigotes
def cajasbigotes(varColumn):
    finalPlot = plot.boxplot(x=abaDataOG[varColumn])
    plot.title('Cajas y Bigotes - ' +varColumn)
    #La variable finalPlot almacena la gráfica
    
def cajasbigotesAtipicos(varColumn):
    values = abaData[varColumn]
    cuartil1 = np.percentile(values,25)
    cuartil3 = np.percentile(values,75)
    iqr = cuartil3 - cuartil1
    li = cuartil1 - (float(alfa.get())*iqr)
    liS = cuartil3 + (float(alfa.get())*iqr)
    noAtipicos = abaData.loc[(abaData[varColumn] > li) & (abaData[varColumn] < liS)]
    finalPlot = plot.boxplot(x=noAtipicos[varColumn])
    plot.title('Cajas de Bigotes SIN OUTLIERS- ' +varColumn)
    variable1 = ""
    variable2 = ""    
    
#Función mostrar ventana de normalización
def normalizacion(varColumn):
    finalPlot = stats.probplot(abaDataOG[varColumn],dist=stats.norm,plot=plot)
    plot.title('Normalizacion - ' +varColumn)
    #La variable finalPlot almacena la gráfica
    
def normalizacionAtipicos(varColumn):
    values = abaData[varColumn]
    cuartil1 = np.percentile(values,25)
    cuartil3 = np.percentile(values,75)
    iqr = cuartil3 - cuartil1
    li = cuartil1 - (float(alfa.get())*iqr)
    liS = cuartil3 + (float(alfa.get())*iqr)
    noAtipicos = abaData.loc[(abaData[varColumn] > li) & (abaData[varColumn] < liS)]
    fig=plot.figure()
    ax=fig.add_subplot(111)
    stats.probplot(noAtipicos[varColumn],dist=stats.norm,plot=ax)
    return fig

def scatter(varColumn1, varColumn2):
    finalPlot = plot.scatter(abaDataOG[varColumn1],abaDataOG[varColumn2])
    plot.title('Distorsión - ' +varColumn1 + ' y ' + varColumn2)
    variable1 = ""
    variable2 = ""
    
def scatterAtipicos(varColumn1, varColumn2):
    values = abaData[varColumn1]
    cuartil1 = np.percentile(values,25)
    cuartil3 = np.percentile(values,75)
    iqr = cuartil3 - cuartil1
    li = cuartil1 - (float(alfa.get())*iqr)
    liS = cuartil3 + (float(alfa.get())*iqr)
    noAtipicos = abaData.loc[(abaData[varColumn1] > li) & (abaData[varColumn1] < liS)]
    values = abaData[varColumn2]
    cuartil1 = np.percentile(values,25)
    cuartil3 = np.percentile(values,75)
    iqr = cuartil3 - cuartil1
    li = cuartil1 - (float(alfa.get())*iqr)
    liS = cuartil3 + (float(alfa.get())*iqr)
    noAtipicos2 = abaData.loc[(abaData[varColumn2] > li) & (abaData[varColumn2] < liS)]
    finalPlot = plot.scatter(noAtipicos[varColumn1], noAtipicos[varColumn2])
    plot.title('Distorsión sin outliers - ' +varColumn1+ ' y ' + varColumn2)
    
def estimate_coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    b1 = SS_xy / SS_xx
    b0 = m_y - b1*m_x
    return (b0, b1)
  
def plot_regression_line(x, y, b):
    FIG = plot.figure()
    FIG.add_subplot(111)
    plot.scatter(x, y, color = "m",
               marker = "o", s = 30)
    y_pred = b[0] + b[1]*x
  
    plot.plot(x, y_pred, color = "g")
  
    plot.xlabel('x')
    plot.ylabel('y')
    return FIG

#Etiquetas - Solo texto
etiqueta1 = Label(interfaz, text="Grafica con atípicos")
etiqueta1.place(x= 20, y= 20)

etiqueta2 = Label(interfaz, text="Tipo de grafico")
etiqueta2.place(x= 200, y= 20)

etiqueta3 = Label(interfaz, text="Variables de entrada")
etiqueta3.place(x= 200, y= 95)

etiqueta4 = Label(interfaz, text="Grafica sin atípicos")
etiqueta4.place(x= 20, y= 230)

etiqueta5 = Label(interfaz, text="Valor del factor de alfa para los atípicos")
etiqueta5.place(x= 130, y= 230)

etiqueta6 = Label(interfaz, text="REGRESIÓN")
etiqueta6.place(x= 35, y= 260)

etiqueta6 = Label(interfaz, text="ENTRADA")
etiqueta6.place(x= 200, y= 260)

etiqueta6 = Label(interfaz, text="SALIDA")
etiqueta6.place(x=390, y= 260)

#Variable RadioButton
var = StringVar(value="Radio 1")

#Variable CheckButton
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()

#Botones
boton1 = Button(interfaz,text="Graficar los datos originales", command = btnCheck01)
boton1.place(x=465, y=200)

boton2 = Button(interfaz,text="Eliminar atípicos", command = btnCheck00)
boton2.place(x=494, y=230)

boton3 = Button(interfaz,text="Obtener regresión", command = btnRegresion)
boton3.place(x=375, y=530)


#Cajas
alfa = tk.StringVar()
caja1 = tk.Entry(interfaz, textvariable=alfa).place(x=350, y=230)


#RadioButton
radio1 = Radiobutton(interfaz, text="Histograma", variable=var, value = "Radio 1", command=sel)
radio1.place(x=200, y=40)

radio2 = Radiobutton(interfaz, text="Cajas y bigotes", variable=var, value = "Radio 2", command = sel)
radio2.place(x=200, y=65)

radio3 = Radiobutton(interfaz, text="Normalización", variable=var, value = "Radio 3", command=sel)
radio3.place(x=350, y=40)

radio4 = Radiobutton(interfaz, text="Scatter", variable=var, value = "Radio 4", command=sel)
radio4.place(x=350, y=65)

radio5 = Radiobutton(interfaz, text="Regresión-Lineal", variable=var, value = "Radio 5", command=sel)
radio5.place(x=500, y=40)

radio6 = Radiobutton(interfaz, text="Regresión-Logistica", variable=var, value = "Radio 6", command=sel)
radio6.place(x=500, y=65)


#Checkbutton -parte arriba
check = Checkbutton(interfaz, text="Longitud", variable = var2)
check.place(x=210, y=120)

check1 = Checkbutton(interfaz, text="Peso entero", variable = var3)
check1.place(x=210, y=150)

check2 = Checkbutton(interfaz, text="Peso Caparazon", variable = var4)
check2.place(x=210, y=180)


check3 = Checkbutton(interfaz, text="Diametro", variable = var5)
check3.place(x=350, y=120)

check4 = Checkbutton(interfaz, text="Peso cascara", variable = var6)
check4.place(x=350, y=150)

check5 = Checkbutton(interfaz, text="# de anillos", variable = var7)
check5.place(x=350, y=180)

check6 = Checkbutton(interfaz, text="Altura", variable = var8)
check6.place(x=500, y=135)

check7 = Checkbutton(interfaz, text="Peso viseras", variable = var9)
check7.place(x=500, y=168)

#Checkbutton -parte abajo

#Variable CheckButton2
regEntry1 = IntVar()
regEntry2 = IntVar()
regEntry3 = IntVar()
regEntry4 = IntVar()
regEntry5 = IntVar()
regEntry6 = IntVar()
regEntry7 = IntVar()
regEntry8 = IntVar()

#Variable CheckButton2 Salida
regOut1 = IntVar()
regOut2 = IntVar()
regOut3 = IntVar()
regOut4 = IntVar()
regOut5 = IntVar()
regOut6 = IntVar()
regOut7 = IntVar()
regOut8 = IntVar()

#ENTRADA
check8 = Checkbutton(interfaz, text="Longitud", variable=regEntry1)
check8.place(x=190, y=290)

check9 = Checkbutton(interfaz, text="Diametro", variable=regEntry2)
check9.place(x=190, y=320)

check10 = Checkbutton(interfaz, text="Altura", variable=regEntry3)
check10.place(x=190, y=350)

check11 = Checkbutton(interfaz, text="Peso entero", variable=regEntry4)
check11.place(x=190, y=380)

check12 = Checkbutton(interfaz, text="Peso Cascara", variable=regEntry5)
check12.place(x=190, y=410)

check13 = Checkbutton(interfaz, text="Peso viseras", variable=regEntry6)
check13.place(x=190, y=440)

check14 = Checkbutton(interfaz, text="Peso caparazon", variable=regEntry7)
check14.place(x=190, y=470)

check12 = Checkbutton(interfaz, text="# de anillos", variable=regEntry8)
check12.place(x=190, y=500)

#SALIDA
check13 = Checkbutton(interfaz, text="Longitud", variable=regOut1)
check13.place(x=380, y=290)

check14 = Checkbutton(interfaz, text="Diametro", variable=regOut2)
check14.place(x=380, y=320)

check16 = Checkbutton(interfaz, text="Altura", variable=regOut3)
check16.place(x=380, y=350)

check17 = Checkbutton(interfaz, text="Peso entero", variable=regOut4)
check17.place(x=380, y=380)

check18 = Checkbutton(interfaz, text="Peso Cascara", variable=regOut5)
check18.place(x=380, y=410)

check19 = Checkbutton(interfaz, text="Peso viseras", variable=regOut6)
check19.place(x=380, y=440)

check20 = Checkbutton(interfaz, text="Peso caparazon", variable=regOut7)
check20.place(x=380, y=470)

check21 = Checkbutton(interfaz, text="# de anillos", variable=regOut8)
check21.place(x=380, y=500)

interfaz.mainloop()
