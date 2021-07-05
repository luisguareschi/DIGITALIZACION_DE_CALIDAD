import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
from POINT import Point
from PART import Part
import tkinter as tk
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import cursors


class App:
    def __init__(self):
        self.draw_start_gui()
        # Initial Settings
        self.a = 0
        self.c = 0
        self.state = 'MENU'
        self.plane_type = '-'  # VARIABLE A ESCOGER (v900/v1000)
        self.configuration = '-'  # VARIABLE A ESCOGER (Part/Quadrant)
        self.selected_quadrant = '-'  # VARIABLE A ESCOGER (Upper/Lower/Right/Left)
        self.selected_part = '-'  # VARIABLE A ESCOGER (nombre de la parte)
        self.matchers = ['-FC-', '-FCFC-', '-FCFCFC-', '-FCFCFCFC-']  # Variable a escoger
        self.selected_tool_types_1 = [503]  # VARIABLEA ESCOGER
        self.selected_tool_types = ['ADH', 'TDRILL']  # VARIABLE A ESCOGER

        while True:  # Main loop
            # Run back_end code
            self.update_code()
            # print(self.state, self.plane_type, self.configuration, self.selected_quadrant, self.selected_part)

    def update_code(self):
        # Intial settings
        if self.state == 'MENU':
            self.start_screen.update_idletasks()
            self.start_screen.update()

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
            self.part_names = []
            for point in self.all_points:
                if point.part_1 not in self.part_names:
                    self.part_names.append(point.part_1)
                if point.part_2 not in self.part_names:
                    self.part_names.append(point.part_2)
                if point.part_3 not in self.part_names:
                    self.part_names.append(point.part_3)
                if point.part_4 not in self.part_names:
                    self.part_names.append(point.part_4)
                if point.part_5 not in self.part_names:
                    self.part_names.append(point.part_5)
                if point.part_6 not in self.part_names:
                    self.part_names.append(point.part_6)
            if self.plane_type == 'v900':
                self.part_names.remove('V5358001700000-CUT01')
            if self.plane_type == 'v1000':
                self.part_names.remove('V5358501600400-CUT01')
            for name in self.part_names:
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
            self.state = 'SETTINGS'

        if self.state == 'SETTINGS':
            if self.a == 0:
                self.start_screen.destroy()
                self.draw_main_gui()
                self.frame2.tkraise()
            self.main.update()
            self.main.update_idletasks()
            self.a += 1

        if self.state == 'DISPLAY POINT':
            if self.c == 0:
                print('Loading complete')
                if self.configuration == 'Quadrant':
                    # Lista con puntos que unicamente cumplen todos los criterios de herramienta, cuadrante etc (color rojo)
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

                    self.X_quadrant, self.Y_quadrant, self.Z_quadrant = self.get_cords(
                        self.quadrant_points)  # Puntos que se ven de color negro

                    self.X_selected, self.Y_selected, self.Z_selected = self.get_cords(
                        self.selected_points)  # Puntos que se ven de color rojo

                    # Hacer plot de cuadrante
                    self.plot_quadrant()

            self.c = self.c + 1
            self.main.update()
            self.main.update_idletasks()

    # Main displays functions
    def draw_start_gui(self):
        # Start TKinter
        self.start_screen = tk.Tk()
        # Create a style
        style = ttk.Style(self.start_screen)
        self.start_screen.tk.call('source', 'azure.tcl')
        style.theme_use('azure')

        # Screen settings
        windowWidth = 300
        windowHeight = 200
        screenWidth = self.start_screen.winfo_screenwidth()
        screenHeight = self.start_screen.winfo_screenheight()
        xCordinate = int((screenWidth / 2) - (windowWidth / 2))
        yCordinate = int((screenHeight / 2) - (windowHeight / 2))
        self.start_screen.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))

        # Creating a Font object of "TkDefaultFont"
        self.defaultFont = font.nametofont("TkDefaultFont")

        # Overriding default-font with custom settings
        # i.e changing font-family, size and weight
        self.defaultFont.configure(family=None,
                                   size=12,
                                   weight=font.NORMAL)

        # Main Menu Window
        self.frame = ttk.LabelFrame(self.start_screen, text='Tipo de avion')
        self.frame.pack(fill='both', expand=True, padx=15, pady=15)
        for i in range(0, 2):
            self.frame.columnconfigure(i, weight=1)
        for i in range(0, 2):
            self.frame.rowconfigure(i, weight=1)

        self.label1 = ttk.Label(self.frame, text='\nSelecciona el tipo de avion:')
        self.label1.grid(row=0, column=0, columnspan=2, padx=10)
        self.button1 = ttk.Button(self.frame, text='v900', style='AccentButton',
                                  command=lambda: [self.set_planetype('v900'),
                                                   self.change_state('LOADING')])
        self.button1.grid(row=1, column=0)
        self.button2 = ttk.Button(self.frame, text='v1000', style='AccentButton',
                                  command=lambda: [self.set_planetype('v1000'),
                                                   self.change_state('LOADING')])
        self.button2.grid(row=1, column=1, ipady=0, padx=0)

    def draw_main_gui(self):
        self.main = tk.Tk()
        # Create a style
        style = ttk.Style(self.main)
        self.main.tk.call('source', 'azure.tcl')
        style.theme_use('azure')
        self.main.state('zoomed')
        style.configure('TNotebook.Tab', font=('Arial', '11', 'normal'))

        # Cambiar letra
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial",
                                   size=30,
                                   weight=font.NORMAL)
        # Menu de configuracion de parte
        self.part_window()

        # Menu de configuracion de cuadrante
        self.quadrant_window()

        # Menu de visualizacion de parte
        self.plot_quadrant_window()

    # GUI Functions
    def plot_quadrant_window(self):
        # Marco global de Cuadrante
        self.frame3 = ttk.Frame(self.main)
        self.frame3.place(relwidth=1, relheight=1)
        # Titulo
        title = 'VISTA DE CUADRANTE'
        self.label4 = ttk.Label(self.frame3, text=title)
        self.label4.place(relx=.01, rely=.01)
        # Separator
        self.separator = ttk.Separator(self.frame3)
        self.separator.place(relx=.01, rely=.08, relwidth=.8)

        # Caja de informacion
        self.infobox = tk.LabelFrame(self.frame3, text='Datos del punto', width=600, height=300)
        self.infobox.place(relx=.45, rely=.65)
        self.infobox.pack_propagate(0)
        self.infolabel = tk.Label(self.infobox, text='', font=('Arial', '14'))
        self.infolabel.pack(fill='both')

        # Visualizador de partes
        self.part_window = ttk.Notebook(self.frame3)
        self.part_window.place(relx=.45, rely=.1)

    def quadrant_window(self):
        # Marco global de Cuadrante
        self.frame2 = ttk.Frame(self.main)
        self.frame2.place(relwidth=1, relheight=1)
        # Titulo
        title = 'Ajustes de Visualizacion-' + str(self.plane_type)
        self.label2 = ttk.Label(self.frame2, text=title)
        self.label2.place(relx=.01, rely=.01)
        # Separator
        self.separator = ttk.Separator(self.frame2)
        self.separator.place(relx=.01, rely=.08, relwidth=.8)
        # Button de pieza/cuadrante
        self.button3 = ttk.Combobox(self.frame2, state='readonly', values=['Part', 'Quadrant'])
        self.button3.place(relx=.01, rely=.1)
        self.button3.bind("<<ComboboxSelected>>", self.set_config2)
        # Boton start
        self.button2 = ttk.Button(self.frame2, text='Start', style='AccentButton',
                                  command=lambda: [self.change_state('DISPLAY POINT'), self.change_window(self.frame3)])
        self.button2.place(relx=.7, rely=.1)
        # Cuadro de configuracion
        self.q = tk.StringVar()
        self.labelframe2 = tk.LabelFrame(self.frame2, text='Ajustes de Cuadrante', width=400, height=250)
        self.labelframe2.place(relx=.01, rely=.2)
        self.radio1 = ttk.Radiobutton(self.labelframe2, text='Upper', variable=self.q, value='Upper',
                                      command=self.select_quadrant)
        self.radio1.place(relx=.02, rely=.2)
        self.radio2 = ttk.Radiobutton(self.labelframe2, text='Lower', variable=self.q, value='Lower',
                                      command=self.select_quadrant)
        self.radio2.place(relx=.02, rely=.45)
        self.radio3 = ttk.Radiobutton(self.labelframe2, text='Right', variable=self.q, value='Right',
                                      command=self.select_quadrant)
        self.radio3.place(relx=.55, rely=.2)
        self.radio4 = ttk.Radiobutton(self.labelframe2, text='Left', variable=self.q, value='Left',
                                      command=self.select_quadrant)
        self.radio4.place(relx=.55, rely=.45)
        # Boton de seleccionar cuadrante
        self.button4 = ttk.Combobox(self.frame2, state='readonly', values=['Upper', 'Lower', 'Right', 'Left'])
        self.button4.place(relx=.3, rely=.1)
        self.button4.bind("<<ComboboxSelected>>", self.set_quadrant)


    def part_window(self):
        # Marco global de Parte
        self.frame = ttk.Frame(self.main)
        self.frame.place(relwidth=1, relheight=1)

        # Titulo
        title = 'Ajustes de Visualizacion-' + str(self.plane_type)
        self.label2 = ttk.Label(self.frame, text=title)
        self.label2.place(relx=.01, rely=.01)
        # Separator
        self.separator = ttk.Separator(self.frame)
        self.separator.place(relx=.01, rely=.08, relwidth=.8)
        # Cuadro de ajustes
        self.labelframe1 = tk.LabelFrame(self.frame, text='Ajustes de Parte', width=1000, height=700)
        self.labelframe1.place(relx=.01, rely=.2)
        self.label3 = ttk.Label(self.labelframe1, text='Nombre de parte')
        self.label3.place(relx=.02, rely=.02)
        # Entrada de texto
        self.entry1 = ttk.Entry(self.labelframe1, width=20)
        self.entry1.bind("<KeyRelease>", self.check_part_name)
        self.entry1.place(relx=.4, rely=.02)
        # Lista de partes
        self.list_frame = tk.Frame(self.labelframe1)
        self.list_frame.place(relx=.02, rely=.15)
        self.list1 = tk.Listbox(self.list_frame, bd=0, width=40, bg='#737373', selectbackground='#007fff')
        self.update_parts_list(self.part_names)
        self.list1.pack(side='left')
        # Scrollbar
        self.scroll = tk.Scrollbar(self.list_frame, orient='vertical', width=25)
        self.scroll.config(command=self.list1.yview)
        self.scroll.pack(side='right', fill='y')
        self.list1.config(yscrollcommand=self.scroll.set)
        # Boton start
        self.button2 = ttk.Button(self.frame, text='VER PARTE', style='AccentButton',
                                  command=lambda: [self.set_part(),
                                                   self.plot_part(self.all_parts, self.selected_part)])
        self.button2.place(relx=.7, rely=.1)
        # Button de pieza/cuadrante
        self.button1 = ttk.Combobox(self.frame, state='readonly', values=['Part', 'Quadrant'])
        self.button1.place(relx=.01, rely=.1)
        self.button1.bind("<<ComboboxSelected>>", self.set_config1)

    def select_quadrant(self):
        self.selected_quadrant = self.q.get()
        if self.plane_type == 'v1000':
            if self.selected_quadrant == 'Left':
                self.selected_quadrant = 'Izquierdo'
            elif self.selected_quadrant == 'Right':
                self.selected_quadrant = 'Derecho'
            elif self.selected_quadrant == 'Upper':
                self.selected_quadrant = 'Superior'
            elif self.selected_quadrant == 'Lower':
                self.selected_quadrant = 'Inferior'

    def set_config1(self, event):
        print(self.button1.get())
        if self.button1.get() == 'Part':
            self.configuration = 'Part'
            self.frame.tkraise()
            self.button3.current(0)
        if self.button1.get() == 'Quadrant':
            self.configuration = 'Quadrant'
            self.frame2.tkraise()
            self.button3.current(1)

    def set_config2(self, event):
        print(self.button3.get())
        if self.button3.get() == 'Part':
            self.configuration = 'Part'
            self.frame.tkraise()
            self.button1.current(0)
        if self.button3.get() == 'Quadrant':
            self.configuration = 'Quadrant'
            self.frame2.tkraise()
            self.button1.current(1)

    def set_quadrant(self, event):
        self.selected_quadrant = self.button4.get()
        if self.plane_type == 'v1000':
            if self.selected_quadrant == 'Left':
                self.selected_quadrant = 'Izquierdo'
            elif self.selected_quadrant == 'Right':
                self.selected_quadrant = 'Derecho'
            elif self.selected_quadrant == 'Upper':
                self.selected_quadrant = 'Superior'
            elif self.selected_quadrant == 'Lower':
                self.selected_quadrant = 'Inferior'

    def set_planetype(self, value):
        self.plane_type = value

    def set_part(self):
        index = self.list1.curselection()
        self.selected_part = self.list1.get(index[0])
        print(self.selected_part)

    def change_window(self, window):
        window.tkraise()

    def change_state(self, value):
        self.state = value

    def update_parts_list(self, list):
        self.list1.delete(0, tk.END)
        for name in list:
            self.list1.insert(tk.END, name)

    def check_part_name(self, event):
        text = self.entry1.get()
        if text == '':
            data = self.part_names
        else:
            data = []
            for name in self.part_names:
                if text.lower() in name.lower():
                    data.append(name)
        self.update_parts_list(data)

    def delete_part_text_info(self):
        self.infolabel.config(text='')

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
        self.point_info_text = "Location: ({},{})\nName: {} \nID: {} \nParts: \n{}\n{}\n{}\n{}\n{}\n{}".format(
            xvalue[0], yvalue[0],
            self.clicked_point.process_f_name,
            self.clicked_point.id,
            self.clicked_point.part_1,
            self.clicked_point.part_2,
            self.clicked_point.part_3,
            self.clicked_point.part_4,
            self.clicked_point.part_5,
            self.clicked_point.part_6)
        self.infolabel.config(text=self.point_info_text)

        for part_name in self.clicked_point.part_names:
            if self.part_names != '-':
                self.plot_partANDpoint(self.all_parts, part_name, self.clicked_point)

    def on_pick_point_from_part(self, event, part):  # WIP
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        zdata = thisline.get_zdata()
        ind = event.ind
        xvalue = np.take(xdata, ind)
        yvalue = np.take(ydata, ind)
        zvalue = np.take(zdata, ind)
        if xvalue[0] in part.x and yvalue[0] in part.y and zvalue[0] in part.z:
            self.clicked_point = self.find_pointXYZ(self.all_points, xvalue[0],
                                                    yvalue[0], zvalue[0])
        print('XYZ location', xvalue[0], yvalue[0], zvalue[0])
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
        self.annot.xyz = (xvalue[0], yvalue[0], zvalue[0])
        self.annot.set_text(text)
        self.annot.set_visible(True)
        self.fig_2.canvas.draw()

    def get_cords(self, points_list):
        Xs = []
        Ys = []
        Zs = []
        for point in points_list:
            Xs.append(point.xe)
            Ys.append(point.ye)
            Zs.append(point.ze)

        return Xs, Ys, Zs

    def find_pointXYZ(self, point_list, x, y, z):
        for point in point_list:
            if point.xe == x and point.ye == y and point.ze == z:
                return point

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
                fig2 = plt.figure()
                ax_2 = fig2.add_subplot(projection='3d')
                ax_2.scatter(x, y, z, color='blue')
                ax_2.scatter(clicked_point.xe, clicked_point.ye, clicked_point.ze, color='red')
                ax_2.set_title(part_name)

                # Create widget
                miniframe = tk.Frame(self.part_window, height=500, width=600)
                self.part_window.add(miniframe, text=part_name)
                canvas_plot = FigureCanvasTkAgg(fig2, miniframe)
                canvas_plot.get_tk_widget().pack(fill='both', side='top')

                # Close part button
                button = ttk.Button(miniframe, text='X', style='AccentButton',
                                    command=lambda: [miniframe.destroy(), button.destroy(),
                                                     self.delete_part_text_info()])
                button.place(relx=.9, rely=0, width=60, height=60)
                break

    def plot_part(self, all_parts, part_name):
        for part in all_parts:
            if part.name == part_name and part_name != '-':
                fig_2 = plt.figure()
                fig_2ax_2 = fig_2.add_subplot(projection='3d')
                fig_2ax_2.scatter(part.x, part.y, part.z, color='blue')
                fig_2ax_2.set_title(part_name)

                # Crear el widget
                miniframe = tk.LabelFrame(self.frame, height=800, width=900, text=part_name)
                miniframe.place(relx=.6, rely=.2)

                self.canvas_part = FigureCanvasTkAgg(fig_2, miniframe)
                self.canvas_part.get_tk_widget().pack(fill='both', side='top')
                break

    def plot_quadrant(self):
        self.fig = plt.figure(dpi=100, frameon=False, figsize=(7, 7))
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

        # Comando para seleccionar parte
        self.fig.canvas.mpl_connect('pick_event', self.on_pick_point)

        # Crear el widget
        miniframe = tk.LabelFrame(self.frame3, height=800, width=900, text='Cuadrante')
        miniframe.place(relx=.03, rely=.10)

        self.canvas_plot = FigureCanvasTkAgg(self.fig, miniframe)
        self.canvas_plot.get_tk_widget().pack(fill='both', side='top')
        toolbar = NavigationToolbar2Tk(self.canvas_plot, miniframe)


app = App()
