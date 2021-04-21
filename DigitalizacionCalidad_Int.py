import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor


stack = ['-FC-','-FCFC-','-FCFCFC-','-FCFCFCFC-'] # Configuracion de las capas
tt = 503 # Tipo de herramienta
cuadrante = 'Upper' #En la versión v900 se pone en inglés y en la v1000, en español. Revisar linea 68 y 107.

main_root = r'C:\Users\cdomi\Desktop\Doctorado UC3M-Airbus\PYTHON'
xlsxFiles = os.listdir(main_root)
nombresxlsx = 'BibliaV900.xlsx'
rutaFicheroxlsx = os.path.join(main_root, nombresxlsx)
df = pd.read_excel(rutaFicheroxlsx)

# Se seleccionan únicamente los archivos donde se taladre FCFC
matchers = ['-FC-','-FCFC-','-FCFCFC-','-FCFCFCFC-']
fileName_FCFC = [s for s in df['Process Feature Name'] if any(xs in s for xs in matchers)]
idx = []
idx_2 = []
Name_XLSX = []
Description = []
Description_2 = []
Zona = []
Parts_1 = []
Parts_2 = []
Parts_3 = []
Parts_4 = []
Cuadrante = []
ID = []
Name = []
X = []
Y = []
Z = []
for i, n in enumerate(df['Process Feature Name']):
    for k in fileName_FCFC:
        if n == k and df['Tool 1'][i] == tt and (df['Tdrill/adh/230/ninguno'][i] == 'ADH' or df['Tdrill/adh/230/ninguno'][i] == 'TDRILL') and df['CUADRANTE TEORICO'][i] == cuadrante:
            idx.append(i)
            Parts_1.append(df['Parts_To_Tight_1'][i])
            Parts_2.append(df['Parts_To_Tight_2'][i])
            Parts_3.append(df['Parts_To_Tight_3'][i])
            Parts_4.append(df['Parts_To_Tight_4'][i])
            Description.append(df['DESCRIPCION'][i])
            ID.append(df['ID'][i])
            Name.append(df['Process Feature Name'][i])

for i, n in enumerate(df['CUADRANTE TEORICO']):
    if n == cuadrante:
        X.append(df['Xe'][i])
        Y.append(df['Ye'][i])
        Z.append(df['Ze'][i])

Xe_FC = []
Ye_FC = []
Ze_FC = []

for i in idx:
    Xe_FC.append(df['Xe'][i])
    Ye_FC.append(df['Ye'][i])
    Ze_FC.append(df['Ze'][i])

fig = plt.figure(dpi=100, frameon=False)
figure = fig.add_subplot()
figure.set_title(cuadrante)
cursor = Cursor(figure, horizOn=True, vertOn = True, color ='b', linewidth =1)
if cuadrante == 'Upper' or cuadrante == 'Lower' or cuadrante == 'Superior' or cuadrante == 'Inferior':
    figure.plot(X, Y, 'o', markersize = 1, color = 'black')
    figure.plot(Xe_FC, Ye_FC, 'o', markersize = 2, color = 'red', picker = 5)
    annot = figure.annotate("",xy = (0,0), xytext = (-40,40), textcoords = "offset points", bbox=dict(boxstyle='round',fc='linen',ec ='k', lw=1), arrowprops=dict(arrowstyle = '-|>'))
    annot.set_visible(False)
    def onpick1(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        xvalue = np.take(xdata, ind)
        yvalue = np.take(ydata, ind)
        X_P2 = []
        Y_P2 = []
        Z_P2 = []
        X_Value = []
        Y_Value = []
        Z_Value = []
        for i, n in enumerate(Xe_FC):
            if n == xvalue[0] and Ye_FC[i] == yvalue[0]:
                x = n
                y = Ye_FC[i]
                print('XY location', xvalue, yvalue)
                print('Name', Name[i])
                Nombre = Name[i]
                print('ID point', ID[i])
                Identificador = ID[i]
                print('Descripcion', Description[i])
                Descriptor = Description[i]
                print('Parts', Parts_1[i], Parts_2[i], Parts_3[i], Parts_4[i], '\n')
                P1 = Parts_1[i]
                P2 = Parts_2[i]
                P3 = Parts_3[i]
                P4 = Parts_4[i]
        for i, n in enumerate(df['Parts_To_Tight_2']):
            if n == P2 and df['ID'][i] != Identificador:
                X_P2.append(df['Xe'][i])
                Y_P2.append(df['Ye'][i])
                Z_P2.append(df['Ze'][i])
        for i, n in enumerate(df['ID']):
            if n == Identificador:
                X_Value.append(df['Xe'][i])
                Y_Value.append(df['Ye'][i])
                Z_Value.append(df['Ze'][i])


        annot.xy = (xvalue, yvalue)
        text = "Location: ({},{})\nName: {} \nID: {} \nZone: {} \nParts: \n{}\n{}\n{}\n{}".format(x, y, Nombre, Identificador, Descriptor, P1, P2, P3, P4)
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw()

        fig_2 = plt.figure()
        ax_2 = fig_2.add_subplot(projection='3d')
        ax_2.scatter(X_P2,Y_P2,Z_P2, color = 'blue')
        ax_2.scatter(X_Value, Y_Value, Z_Value, color = 'red')
        ax_2.set_title(P2)

        fig_3 = plt.figure()
        ax_3 = fig_3.add_subplot()
        ax_3.plot(X_P2, Y_P2, 'o', markersize = 2, color = 'blue')
        ax_3.plot(X_Value, Y_Value, 'o', markersize = 2, color = 'red')
        ax_3.set_title('X|Y plane')

        fig_4 = plt.figure()
        ax_4 = fig_4.add_subplot()
        ax_4.plot(X_P2, Z_P2, 'o', markersize=2, color='blue')
        ax_4.plot(X_Value, Z_Value, 'o', markersize=2, color='red')
        ax_4.set_title('X|Z plane')

        fig_5 = plt.figure()
        ax_5 = fig_5.add_subplot()
        ax_5.plot(Y_P2, Z_P2, 'o', markersize=2, color='blue')
        ax_5.plot(Y_Value, Z_Value, 'o', markersize=2, color='red')
        ax_5.set_title('Y|Z plane')
        plt.show()


    fig.canvas.mpl_connect('pick_event', onpick1)

    plt.show()

elif cuadrante == 'Left' or cuadrante == 'Right' or cuadrante == 'Izquierdo' or cuadrante == 'Derecho':
    figure.plot(X, Z, 'o', markersize=1, color='black')
    figure.plot(Xe_FC, Ze_FC, 'o', markersize=2, color='red', picker=5)
    annot = figure.annotate("", xy=(0, 0), xytext=(-40, 40), textcoords="offset points",
                            bbox=dict(boxstyle='round', fc='linen', ec='k', lw=1), arrowprops=dict(arrowstyle='-|>'))
    annot.set_visible(False)


    def onpick1(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        xvalue = np.take(xdata, ind)
        yvalue = np.take(ydata, ind)
        X_P2 = []
        Y_P2 = []
        Z_P2 = []
        X_Value = []
        Y_Value = []
        Z_Value = []
        for i, n in enumerate(Xe_FC):
            if n == xvalue[0] and Ze_FC[i] == yvalue[0]:
                x = n
                y = Ze_FC[i]
                print('XY location', xvalue, yvalue)
                print('Name', Name[i])
                Nombre = Name[i]
                print('ID point', ID[i])
                Identificador = ID[i]
                print('Descripcion', Description[i])
                Descriptor = Description[i]
                print('Parts', Parts_1[i], Parts_2[i], Parts_3[i], Parts_4[i], '\n')
                P1 = Parts_1[i]
                P2 = Parts_2[i]
                P3 = Parts_3[i]
                P4 = Parts_4[i]

        for i, n in enumerate(df['Parts_To_Tight_2']):
            if n == P2 and df['ID'][i] != Identificador:
                X_P2.append(df['Xe'][i])
                Y_P2.append(df['Ye'][i])
                Z_P2.append(df['Ze'][i])
        for i, n in enumerate(df['ID']):
            if n == Identificador:
                X_Value.append(df['Xe'][i])
                Y_Value.append(df['Ye'][i])
                Z_Value.append(df['Ze'][i])

        annot.xy = (xvalue, yvalue)
        text = "Location: ({},{})\nName: {} \nID: {} \nZone: {} \nParts: \n{}\n{}\n{}\n{}".format(x, y, Nombre, Identificador, Descriptor, P1, P2, P3, P4)
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw()

        fig_2 = plt.figure()
        ax_2 = fig_2.add_subplot(projection='3d')
        ax_2.scatter(X_P2, Y_P2, Z_P2, color='blue')
        ax_2.scatter(X_Value, Y_Value, Z_Value, color='red')
        ax_2.set_title(P2)

        fig_3 = plt.figure()
        ax_3 = fig_3.add_subplot()
        ax_3.plot(X_P2, Y_P2, 'o', markersize=2, color='blue')
        ax_3.plot(X_Value, Y_Value, 'o', markersize=2, color='red')
        ax_3.set_title('X|Y plane')

        fig_4 = plt.figure()
        ax_4 = fig_4.add_subplot()
        ax_4.plot(X_P2, Z_P2, 'o', markersize=2, color='blue')
        ax_4.plot(X_Value, Z_Value, 'o', markersize=2, color='red')
        ax_4.set_title('X|Z plane')

        fig_5 = plt.figure()
        ax_5 = fig_5.add_subplot()
        ax_5.plot(Y_P2, Z_P2, 'o', markersize=2, color='blue')
        ax_5.plot(Y_Value, Z_Value, 'o', markersize=2, color='red')
        ax_5.set_title('Y|Z plane')
        plt.show()


    fig.canvas.mpl_connect('pick_event', onpick1)

    plt.show()

