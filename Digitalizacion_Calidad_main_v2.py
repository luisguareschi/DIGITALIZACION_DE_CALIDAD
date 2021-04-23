import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
from POINT import Point
from PART import Part



# Functions
def get_cords(points_list):
    Xs = []
    Ys = []
    Zs = []
    for point in points_list:
        Xs.append(point.xe)
        Ys.append(point.ye)
        Zs.append(point.ze)

    return Xs, Ys, Zs


def find_pointXY(point_list, x, y):
    for point in point_list:
        if point.xe == x and point.ye == y:
            return point


def find_pointXZ(point_list, x, z):
    for point in point_list:
        if point.xe == x and point.ze == z:
            return point


def plot_partANDpoint(all_parts, part_name, clicked_point):
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


def plot_part(all_parts, part_name):
    for part in all_parts:
        if part.name == part_name and part_name != '-':
            fig_2 = plt.figure()
            ax_2 = fig_2.add_subplot(projection='3d')
            ax_2.scatter(part.x, part.y, part.z, color='blue')
            ax_2.set_title(part_name)

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
            plt.show()
            break \
 \
 \
# Intial settings


plane_type = 'v1000'
configuration = 'Quadrant'
if configuration == 'Quadrant':
    selected_quadrant = 'Upper'
    if plane_type == 'v1000':
        if selected_quadrant == 'Left':
            selected_quadrant = 'Izquierdo'
        elif selected_quadrant == 'Right':
            selected_quadrant = 'Derecho'
        elif selected_quadrant == 'Upper':
            selected_quadrant = 'Superior'
        elif selected_quadrant == 'Lower':
            selected_quadrant = 'Inferior'
elif configuration == 'Part':
    selected_part = 'V5358002520600'
matchers = ['-FC-', '-FCFC-', '-FCFCFC-', '-FCFCFCFC-']
selected_tool_types_1 = [503]
selected_tool_types = ['ADH', 'TDRILL']

# Abrir y Leer archivo .xlsx
main_root = os.path.dirname(os.path.abspath(__file__))
if plane_type == 'v900':
    xlsx_name = 'v900.xlsx'
if plane_type == 'v1000':
    xlsx_name = 'v1000.xlsx'
file_root = os.path.join(main_root, xlsx_name)
df = pd.read_excel(file_root)

# Leer cada columna y crear una lista de cada una
ids = df['ID']
process_feature_names = df['Process Feature Name']
diameters = df['Diameter']
xes = df['Xe']
yes = df['Ye']
zes = df['Ze']
tool_1s = df['Tool 1']
tools = df['Tdrill/adh/230/ninguno']
parts_1 = df['Parts_To_Tight_1']
parts_2 = df['Parts_To_Tight_2']
parts_3 = df['Parts_To_Tight_3']
parts_4 = df['Parts_To_Tight_4']
parts_5 = df['Parts_To_Tight_5']
parts_6 = df['Parts_To_Tight_6']
quadrants = df['CUADRANTE TEORICO']

all_points = []  # Todos lo puntos que hay en el excel
# Crear una lista con todos los objetos point
for i in range(len(ids)):
    id = ids[i]
    process_f_name = process_feature_names[i]
    diameter = diameters[i]
    xe = xes[i]
    ye = yes[i]
    ze = zes[i]
    tool_1 = tool_1s[i]
    tool = tools[i]
    part_1 = parts_1[i]
    part_2 = parts_2[i]
    part_3 = parts_3[i]
    part_4 = parts_4[i]
    part_5 = parts_5[i]
    part_6 = parts_6[i]
    quadrant = quadrants[i]
    point = Point(id, process_f_name, diameter, xe, ye, ze, tool_1, tool, part_1, part_2, part_3, part_4, part_5,
                  part_6, quadrant)
    all_points.append(point)

# Crear todas las partes
all_parts = []
part1_names = []
part2_names = []
part3_names = []
part4_names = []
part5_names = []
part6_names = []
for point in all_points:
    if point.part_1 not in part1_names:
        part1_names.append(point.part_1)
    if point.part_2 not in part2_names:
        part2_names.append(point.part_2)
    if point.part_3 not in part3_names:
        part3_names.append(point.part_3)
    if point.part_4 not in part4_names:
        part4_names.append(point.part_4)
    if point.part_5 not in part5_names:
        part5_names.append(point.part_5)
    if point.part_6 not in part6_names:
        part6_names.append(point.part_6)

part_names = [part1_names, part2_names, part3_names,
              part4_names, part5_names, part6_names]
for parti_names in part_names:
    for name in parti_names:
        x = []
        y = []
        z = []
        for point in all_points:
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
        all_parts.append(p)

print('Se han creado {} puntos'.format(len(all_points)))
print('Se han creado {} partes'.format(len(all_parts)))
######

if configuration == 'Quadrant':
    # Lista con puntos que unicamente cumplen todos los criterios de herramienta, cuadrante etc
    selected_points = []
    for point in all_points:
        if any(x in point.process_f_name for x in matchers):
            if point.tool_1 in selected_tool_types_1:
                if point.tool in selected_tool_types:
                    if point.quadrant == selected_quadrant:
                        selected_points.append(point)

    # Lista con todos los puntos del cuadrante
    quadrant_points = []
    for point in all_points:
        if point.quadrant == selected_quadrant:
            quadrant_points.append(point)

    X_quadrant, Y_quadrant, Z_quadrant = get_cords(quadrant_points)

    X_selected, Y_selected, Z_selected = get_cords(selected_points)

    fig = plt.figure(dpi=100, frameon=False)
    figure = fig.add_subplot()
    figure.set_title(selected_quadrant)
    cursor = Cursor(figure, horizOn=True, vertOn=True, color='b', linewidth=1)
    if selected_quadrant == 'Upper' or selected_quadrant == 'Lower' or selected_quadrant == 'Superior' or selected_quadrant == 'Inferior':
        figure.plot(X_quadrant, Y_quadrant, 'o', markersize=1, color='black')
        figure.plot(X_selected, Y_selected, 'o', markersize=2, color='red', picker=5)
    elif selected_quadrant == 'Right' or selected_quadrant == 'Left' or selected_quadrant == 'Derecho' or selected_quadrant == 'Izquierdo':
        figure.plot(X_quadrant, Z_quadrant, 'o', markersize=1, color='black')
        figure.plot(X_selected, Z_selected, 'o', markersize=2, color='red', picker=5)
    annot = figure.annotate("", xy=(0, 0), xytext=(-40, 40), textcoords="offset points",
                            bbox=dict(boxstyle='round', fc='linen', ec='k', lw=1), arrowprops=dict(arrowstyle='-|>'))
    annot.set_visible(False)


    def on_pick_point(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        xvalue = np.take(xdata, ind)
        yvalue = np.take(ydata, ind)
        if selected_quadrant == 'Upper' or selected_quadrant == 'Lower' or selected_quadrant == 'Superior' or selected_quadrant == 'Inferior':
            if xvalue[0] in X_selected and yvalue[0] in Y_selected:
                clicked_point = find_pointXY(selected_points, xvalue[0], yvalue[0])
        elif selected_quadrant == 'Right' or selected_quadrant == 'Left' or selected_quadrant == 'Derecho' or selected_quadrant == 'Izquierdo':
            if xvalue[0] in X_selected and yvalue[0] in Z_selected:
                clicked_point = find_pointXZ(selected_points, xvalue[0], yvalue[0])
            print('XY location', xvalue[0], yvalue[0])
            print('Name', clicked_point.process_f_name)
            print('ID point', clicked_point.id)
            print('Parts: \n{}\n{}\n{}\n{}'.format(clicked_point.part_1, clicked_point.part_2, clicked_point.part_3,
                                                   clicked_point.part_4))
        text = "Location: ({},{})\nName: {} \nID: {} \nParts: \n{}\n{}\n{}\n{}".format(xvalue[0], yvalue[0],
                                                                                       clicked_point.process_f_name,
                                                                                       clicked_point.id,
                                                                                       clicked_point.part_1,
                                                                                       clicked_point.part_2,
                                                                                       clicked_point.part_3,
                                                                                       clicked_point.part_4)
        annot.xy = (xvalue[0], yvalue[0])
        annot.set_text(text)
        annot.set_visible(True)
        fig.canvas.draw()

        plot_partANDpoint(all_parts, clicked_point.part_1, clicked_point)
        plot_partANDpoint(all_parts, clicked_point.part_2, clicked_point)
        plot_partANDpoint(all_parts, clicked_point.part_3, clicked_point)
        plot_partANDpoint(all_parts, clicked_point.part_4, clicked_point)
        plot_partANDpoint(all_parts, clicked_point.part_5, clicked_point)
        plot_partANDpoint(all_parts, clicked_point.part_6, clicked_point)


    fig.canvas.mpl_connect('pick_event', on_pick_point)

    plt.show()

elif configuration == 'Part':
    plot_part(all_parts, selected_part)
