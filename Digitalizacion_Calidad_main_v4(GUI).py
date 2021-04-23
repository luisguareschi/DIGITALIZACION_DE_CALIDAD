import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
from POINT import Point
from PART import Part
import tkinter as tk


class App:
    def __init__(self):
        # Initial Settings
        self.a = 0
        self.c = 0
        self.state = 'MENU'
        self.plane_type = '-'  # VARIABLE A ESCOGER (v900/v1000)
        self.configuration = '-'  # VARIABLE A ESCOGER (part/quadrant)
        self.selected_quadrant = '-'  # VARIABLE A ESCOGER (Upper/Lower/Right/Left)
        self.selected_part = ''  # VARIABLE A ESCOGER (nombre de la parte)

        self.main = tk.Tk()
        self.canvas = tk.Canvas(self.main, height=600, width=800)
        self.canvas.pack()

        # Main Menu Window
        self.window1 = tk.Frame(self.main, bg='#00284d')
        self.window1.place(relwidth=1, relheight=1)
        self.label1 = tk.Label(self.window1, text='DIGITALIZACION DE CALIDAD', font=("Arial", "24"), bg='#00284d',
                               fg='white')
        self.label1.place(rely=.1, relwidth=1)
        self.label2 = tk.Label(self.window1, text='Selecciona tipo de avion:', font=("Arial", "18"), bg='#00284d',
                               fg='white')
        self.label2.place(rely=.3, relwidth=1)
        self.button1 = tk.Button(self.window1, text='v900', font=("Arial", "40"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window6), self.set_planetype('v900')])
        self.button1.place(relx=.55 - .025, rely=.45)
        self.button2 = tk.Button(self.window1, text='v1000', font=("Arial", "40"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window6), self.set_planetype('v1000')])
        self.button2.place(relx=.30 - .025, rely=.45)

        # Visualization type Window
        self.window6 = tk.Frame(self.main, bg='#00284d')
        self.window6.place(relwidth=1, relheight=1)
        self.label2 = tk.Label(self.window6, text='Selecciona tipo de visualizacion:', font=("Arial", "18"),
                               bg='#00284d',
                               fg='white')
        self.label2.place(rely=.3, relwidth=1)
        self.button1 = tk.Button(self.window6, text='CUADRANTE', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window7),
                                                  self.set_visualizationtype('Quadrant')])
        self.button1.place(relx=.55 - .025, rely=.45)
        self.button2 = tk.Button(self.window6, text='PARTE', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window4),
                                                  self.set_visualizationtype('Part'),
                                                  self.change_state('LOADING')])
        self.button2.place(relx=.30 - .025, rely=.45)

        # Quadrant settings window
        self.window7 = tk.Frame(self.main, bg='#00284d')
        self.window7.place(relwidth=1, relheight=1)
        self.label2 = tk.Label(self.window7, text='Selecciona el cuadrante que quieres ver:', font=("Arial", "18"),
                               bg='#00284d',
                               fg='white')
        self.label2.place(rely=.3, relwidth=1)
        self.button1 = tk.Button(self.window7, text='Upper', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window4),
                                                  self.set_quadrant('Upper'),
                                                  self.change_state('LOADING')])
        self.button1.place(relx=.55 - .025, rely=.45)
        self.button2 = tk.Button(self.window7, text='Lower', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window4),
                                                  self.set_quadrant('Lower'),
                                                  self.change_state('LOADING')])
        self.button2.place(relx=.30 - .025, rely=.45)
        self.label2.place(rely=.3, relwidth=1)
        self.button1 = tk.Button(self.window7, text='Right', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window4),
                                                  self.set_quadrant('Right'),
                                                  self.change_state('LOADING')])
        self.button1.place(relx=.55 - .025, rely=.60)
        self.button2 = tk.Button(self.window7, text='Left', font=("Arial", "20"), bd=0, activebackground='grey',
                                 command=lambda: [self.change_window(self.window4),
                                                  self.set_quadrant('Left'),
                                                  self.change_state('LOADING')])
        self.button2.place(relx=.30 - .025, rely=.60)

        # Loading window
        self.window4 = tk.Frame(self.main, bg='#00284d')
        self.window4.place(relwidth=1, relheight=1)
        self.label1 = tk.Label(self.window4, text='LOADING...', font=("Arial", "24"), bg='#00284d', fg='white')
        self.label1.place(rely=.1, relwidth=1)

        # Display points window
        self.window5 = tk.Frame(self.main, bg='#00284d')
        self.window5.place(relwidth=1, relheight=1)
        self.label1 = tk.Label(self.window5, text='SUCCESS! LOADING COMPLETE', font=("Arial", "24"), bg='#00284d',
                               fg='white')
        self.label1.place(rely=.1, relwidth=1)

        # Show main menu window
        self.window1.tkraise()

        while True:
            # Run back_end code
            self.update_code()
            # print(self.state, self.plane_type, self.configuration, self.selected_quadrant, self.selected_part)

            # Run main loop
            self.main.update_idletasks()
            self.main.update()

    def update_code(self):
        # Intial settings
        if self.state == 'MENU':
            self.matchers = ['-FC-', '-FCFC-', '-FCFCFC-', '-FCFCFCFC-']
            self.selected_tool_types_1 = [503]
            self.selected_tool_types = ['ADH', 'TDRILL']

        if self.state == 'LOADING':
            print('loading')
            # Abrir y Leer archivo .xlsx
            self.main_root = os.path.dirname(os.path.abspath(__file__))
            if self.plane_type == 'v900':
                self.xlsx_name = 'v900.xlsx'
            if self.plane_type == 'v1000':
                self.xlsx_name = 'v1000.xlsx'
            self.file_root = os.path.join(self.main_root, self.xlsx_name)
            self.df = pd.read_excel(self.file_root)

            # Leer cada columna y crear una lista de cada una
            self.ids = self.df['ID']
            self.process_feature_names = self.df['Process Feature Name']
            self.diameters = self.df['Diameter']
            self.xes = self.df['Xe']
            self.yes = self.df['Ye']
            self.zes = self.df['Ze']
            self.tool_1s = self.df['Tool 1']
            self.tools = self.df['Tdrill/adh/230/ninguno']
            self.parts_1 = self.df['Parts_To_Tight_1']
            self.parts_2 = self.df['Parts_To_Tight_2']
            self.parts_3 = self.df['Parts_To_Tight_3']
            self.parts_4 = self.df['Parts_To_Tight_4']
            self.parts_5 = self.df['Parts_To_Tight_5']
            self.parts_6 = self.df['Parts_To_Tight_6']
            self.quadrants = self.df['CUADRANTE TEORICO']

            self.all_points = []  # Todos lo puntos que hay en el excel
            # Crear una lista con todos los objetos point
            for i in range(len(self.ids)):
                id = self.ids[i]
                process_f_name = self.process_feature_names[i]
                diameter = self.diameters[i]
                xe = self.xes[i]
                ye = self.yes[i]
                ze = self.zes[i]
                tool_1 = self.tool_1s[i]
                tool = self.tools[i]
                part_1 = self.parts_1[i]
                part_2 = self.parts_2[i]
                part_3 = self.parts_3[i]
                part_4 = self.parts_4[i]
                part_5 = self.parts_5[i]
                part_6 = self.parts_6[i]
                quadrant = self.quadrants[i]
                point = Point(id, process_f_name, diameter, xe, ye, ze, tool_1,
                              tool, part_1, part_2, part_3, part_4, part_5,
                              part_6, quadrant)
                self.all_points.append(point)

            # Crear todas las partes
            self.all_parts = []
            self.part1_names = []
            self.part2_names = []
            self.part3_names = []
            self.part4_names = []
            self.part5_names = []
            self.part6_names = []
            for point in self.all_points:
                if point.part_1 not in self.part1_names:
                    self.part1_names.append(point.part_1)
                if point.part_2 not in self.part2_names:
                    self.part2_names.append(point.part_2)
                if point.part_3 not in self.part3_names:
                    self.part3_names.append(point.part_3)
                if point.part_4 not in self.part4_names:
                    self.part4_names.append(point.part_4)
                if point.part_5 not in self.part5_names:
                    self.part5_names.append(point.part_5)
                if point.part_6 not in self.part6_names:
                    self.part6_names.append(point.part_6)

            self.part_names = [self.part1_names, self.part2_names, self.part3_names,
                               self.part4_names, self.part5_names, self.part6_names]
            for parti_names in self.part_names:
                for name in parti_names:
                    x = []
                    y = []
                    z = []
                    for point in self.all_points:
                        if point.part_1 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                        elif point.part_2 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                        elif point.part_3 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                        elif point.part_4 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                        elif point.part_5 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                        elif point.part_6 == name:
                            x.append(point.xe)
                            y.append(point.ye)
                            z.append(point.ze)
                    p = Part(name, x, y, z)
                    self.all_parts.append(p)

            print('Se han creado {} puntos'.format(len(self.all_points)))
            print('Se han creado {} partes'.format(len(self.all_parts)))

            if self.configuration == 'Quadrant':
                self.state = 'DISPLAY POINT'
            if self.configuration == 'Part':
                self.state = 'SELECT PART'

        if self.state == 'SELECT PART':
            if self.a == 0:
                # Part config window
                self.window8 = tk.Frame(self.main, bg='#00284d')
                self.window8.place(relwidth=1, relheight=1)
                self.label2 = tk.Label(self.window8, text='Selecciona la parte que quieres ver:', font=("Arial", "18"),
                                       bg='#00284d',
                                       fg='white')
                self.label2.place(rely=.3, relwidth=1)
                self.button1 = tk.Button(self.window8, text='START', font=("Arial", "20"), bd=0,
                                         activebackground='grey',
                                         command=lambda: [self.change_window(self.window5),
                                                          self.set_part(),
                                                          self.change_state('DISPLAY POINT')])
                self.button1.place(relx=.8, rely=.80)

                self.list1 = tk.Listbox(self.window8, font=("Arial", "20"), bd=0)
                self.index = 0
                for parts_list in self.part_names:
                    for part_name in parts_list:
                        self.list1.insert(self.index, part_name)
                        self.index += 1
                self.list1.place(rely=.4, relx=.3)

                self.scroll = tk.Scrollbar(self.window8, orient='vertical')
                self.scroll.config(command=self.list1.yview)
                self.scroll.place(rely=.4, relx=.67, relheight=.55)

                self.list1.config(yscrollcommand=self.scroll.set)
            self.a += 1

        if self.state == 'DISPLAY POINT':
            if self.c == 0:
                print('Loading complete')
                self.window5.tkraise()
                if self.configuration == 'Quadrant':
                    # Lista con puntos que unicamente cumplen todos los criterios de herramienta, cuadrante etc
                    self.selected_points = []
                    for point in self.all_points:
                        if any(x in point.process_f_name for x in self.matchers):
                            if point.tool_1 in self.selected_tool_types_1:
                                if point.tool in self.selected_tool_types:
                                    if point.quadrant == self.selected_quadrant:
                                        self.selected_points.append(point)

                    # Lista con todos los puntos del cuadrante
                    self.quadrant_points = []
                    for point in self.all_points:
                        if point.quadrant == self.selected_quadrant:
                            self.quadrant_points.append(point)

                    self.X_quadrant, self.Y_quadrant, self.Z_quadrant = self.get_cords(self.quadrant_points)

                    self.X_selected, self.Y_selected, self.Z_selected = self.get_cords(self.selected_points)

                    self.fig = plt.figure(dpi=100, frameon=False)
                    self.figure = self.fig.add_subplot()
                    self.figure.set_title(self.selected_quadrant)
                    self.cursor = Cursor(self.figure, horizOn=True, vertOn=True, color='b', linewidth=1)
                    if self.selected_quadrant == 'Upper' or self.selected_quadrant == 'Lower' or self.selected_quadrant == 'Superior' or self.selected_quadrant == 'Inferior':
                        self.figure.plot(self.X_quadrant, self.Y_quadrant, 'o', markersize=1, color='black')
                        self.figure.plot(self.X_selected, self.Y_selected, 'o', markersize=2, color='red', picker=5)
                    elif self.selected_quadrant == 'Right' or self.selected_quadrant == 'Left' or self.selected_quadrant == 'Derecho' or self.selected_quadrant == 'Izquierdo':
                        self.figure.plot(self.X_quadrant, self.Z_quadrant, 'o', markersize=1, color='black')
                        self.figure.plot(self.X_selected, self.Z_selected, 'o', markersize=2, color='red', picker=5)
                    self.annot = self.figure.annotate("", xy=(0, 0), xytext=(-40, 40), textcoords="offset points",
                                                      bbox=dict(boxstyle='round', fc='linen', ec='k', lw=1),
                                                      arrowprops=dict(arrowstyle='-|>'))
                    self.annot.set_visible(False)

                    self.fig.canvas.mpl_connect('pick_event', self.on_pick_point)

                    plt.show()
                if self.configuration == 'Part':
                    self.plot_part(self.all_parts, self.selected_part)
                    plt.show()

            self.c = self.c + 1

    # GUI Functions
    def set_planetype(self, value):
        self.plane_type = value

    def set_visualizationtype(self, value):
        self.configuration = value

    def set_quadrant(self, value):
        self.selected_quadrant = value
        if self.plane_type == 'v1000':
            if self.selected_quadrant == 'Left':
                self.selected_quadrant = 'Izquierdo'
            elif self.selected_quadrant == 'Right':
                self.selected_quadrant = 'Derecho'
            elif self.selected_quadrant == 'Upper':
                self.selected_quadrant = 'Superior'
            elif self.selected_quadrant == 'Lower':
                self.selected_quadrant = 'Inferior'

    def set_part(self):
        index = self.list1.curselection()
        self.selected_part = self.list1.get(index[0])
        print(self.selected_part)

    def change_window(self, window):
        window.tkraise()

    def change_state(self, value):
        self.state = value

    # Methods
    def on_pick_point(self, event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        xvalue = np.take(xdata, ind)
        yvalue = np.take(ydata, ind)
        if self.selected_quadrant == 'Upper' or self.selected_quadrant == 'Lower' or self.selected_quadrant == 'Superior' or self.selected_quadrant == 'Inferior':
            if xvalue[0] in self.X_selected and yvalue[0] in self.Y_selected:
                self.clicked_point = self.find_pointXY(self.selected_points, xvalue[0], yvalue[0])
        if self.selected_quadrant == 'Right' or self.selected_quadrant == 'Left' or self.selected_quadrant == 'Derecho' or self.selected_quadrant == 'Izquierdo':
            if xvalue[0] in self.X_selected and yvalue[0] in self.Z_selected:
                self.clicked_point = self.find_pointXZ(self.selected_points, xvalue[0], yvalue[0])
        print('XY location', xvalue[0], yvalue[0])
        print('Name', self.clicked_point.process_f_name)
        print('ID point', self.clicked_point.id)
        print('Parts: \n{}\n{}\n{}\n{}'.format(self.clicked_point.part_1, self.clicked_point.part_2,
                                               self.clicked_point.part_3,
                                               self.clicked_point.part_4))
        text = "Location: ({},{})\nName: {} \nID: {} \nParts: \n{}\n{}\n{}\n{}".format(xvalue[0], yvalue[0],
                                                                                       self.clicked_point.process_f_name,
                                                                                       self.clicked_point.id,
                                                                                       self.clicked_point.part_1,
                                                                                       self.clicked_point.part_2,
                                                                                       self.clicked_point.part_3,
                                                                                       self.clicked_point.part_4)
        self.annot.xy = (xvalue[0], yvalue[0])
        self.annot.set_text(text)
        self.annot.set_visible(True)
        self.fig.canvas.draw()

        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_1, self.clicked_point)
        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_2, self.clicked_point)
        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_3, self.clicked_point)
        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_4, self.clicked_point)
        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_5, self.clicked_point)
        self.plot_partANDpoint(self.all_parts, self.clicked_point.part_6, self.clicked_point)

    def get_cords(self, points_list):
        Xs = []
        Ys = []
        Zs = []
        for point in points_list:
            Xs.append(point.xe)
            Ys.append(point.ye)
            Zs.append(point.ze)

        return Xs, Ys, Zs

    def find_pointXY(self, point_list, x, y):
        for point in point_list:
            if point.xe == x and point.ye == y:
                return point

    def find_pointXZ(self, point_list, x, z):
        for point in point_list:
            if point.xe == x and point.ze == z:
                return point

    def plot_partANDpoint(self, all_parts, part_name, clicked_point):
        for part in all_parts:
            if part.name == part_name and part_name != '-':
                x = part.x
                y = part.y
                z = part.z
                x.remove(clicked_point.xe)
                y.remove(clicked_point.ye)
                z.remove(clicked_point.ze)
                fig_2 = plt.figure()
                ax_2 = fig_2.add_subplot(projection='3d')
                ax_2.scatter(x, y, z, color='blue')
                ax_2.scatter(clicked_point.xe, clicked_point.ye, clicked_point.ze, color='red')
                ax_2.set_title(part_name)

                fig_3 = plt.figure()
                ax_3 = fig_3.add_subplot()
                ax_3.plot(x, y, 'o', markersize=2, color='blue')
                ax_3.plot(clicked_point.xe, clicked_point.ye, 'o', markersize=2, color='red')
                ax_3.set_title('X|Y plane')

                fig_4 = plt.figure()
                ax_4 = fig_4.add_subplot()
                ax_4.plot(x, z, 'o', markersize=2, color='blue')
                ax_4.plot(clicked_point.xe, clicked_point.ze, 'o', markersize=2, color='red')
                ax_4.set_title('X|Z plane')

                fig_5 = plt.figure()
                ax_5 = fig_5.add_subplot()
                ax_5.plot(y, z, 'o', markersize=2, color='blue')
                ax_5.plot(clicked_point.ye, clicked_point.ze, 'o', markersize=2, color='red')
                ax_5.set_title('Y|Z plane')
                plt.show()
                break

    def plot_part(self, all_parts, part_name):
        for part in all_parts:
            if part.name == part_name and part_name != '-':
                fig_2 = plt.figure()
                fig_2ax_2 = fig_2.add_subplot(projection='3d')
                fig_2ax_2.scatter(part.x, part.y, part.z, color='blue')
                fig_2ax_2.set_title(part_name)

                fig_3 = plt.figure()
                ax_3 = fig_3.add_subplot()
                ax_3.plot(part.x, part.y, 'o', markersize=2, color='blue')
                ax_3.set_title('X|Y plane')

                fig_4 = plt.figure()
                ax_4 = fig_4.add_subplot()
                ax_4.plot(part.x, part.z, 'o', markersize=2, color='blue')
                ax_4.set_title('X|Z plane')

                fig_5 = plt.figure()
                ax_5 = fig_5.add_subplot()
                ax_5.plot(part.y, part.z, 'o', markersize=2, color='blue')
                ax_5.set_title('Y|Z plane')

                break
        print('Part not found')


app = App()
