import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from pril1 import *
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow1 = QtWidgets.QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(MainWindow1)
MainWindow1.show()
def read_f():
    with open("C:\РАботы Урфу\геометрическое моделирование\геом\LB2_KVADR.txt", "r") as file:
        list_cord = file.read().split()
        cord_count = int(list_cord[0])
    cord2 = []
    for i in range(1,cord_count*3+1):
        cord2.append(float(list_cord[i]))
    sw = []
    for i in range(cord_count*3+2,len(list_cord)):
        sw.append(int(list_cord[i]))
    mmx = max(cord2)
    return sw,cord2,mmx

sw,cord2,mmx = read_f()

print('крдинаты-',cord2)
print('связи-',sw)
for i in range(len(cord2)):
    cord2[i] = cord2[i]+mmx/2
from itertools import zip_longest

def rasd_sw(sw):
    n = len(sw) // (len(sw) // 2)
    sw_l = [list(x) for x in zip_longest(*[iter(sw)] * n)]
    swstart = [i[0] for i in sw_l]
    swcon = [i[1] for i in sw_l]
    return (swstart,swcon)
swstart,swcon = rasd_sw(sw)

def Matrixs_preobr(cord):
    global cord3
    n = len(cord) // (len(cord)//3)
    cord = [list(x) for x in zip_longest(*[iter(cord)] * n)]
    for i in range(len(cord)):
        cord[i].append(1)
    cord2 = np.array(cord)
    cord3 = cord2
    return(cord2)
cord2 = Matrixs_preobr(cord2)

def plott(cord2,mmx):
    global ax , fig, sets1, sets2
    plt.close()
    x = [i[0] for i in cord2]
    y = [i[1] for i in cord2]
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()
    ax.set(xlim=(0,25), ylim=(0,25))

    for i, k in zip(swstart, swcon):
        l = Line2D([x[i], x[k]], [y[i], y[k]], color='green')
        ax.add_line(l)
    plt.show()
    print(cord2)
    return (cord2)

def ret_x(rtx, cord2):
    a = rtx * np.pi / 180
    rx = np.array([[1, 0, 0, 0], [0, np.cos(a), np.sin(a), 0], [0, -np.sin(a), np.cos(a), 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rx)
    return (cord2)


def ret_y(rty, cord2):
    a = rty * np.pi / 180
    ry = np.array([[np.cos(a), 0, -np.sin(a), 0], [0, 1, 0, 0], [np.sin(a), 0, np.cos(a), 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(ry)
    return (cord2)

def ret_z(rtz, cord2):
    a = rtz * np.pi / 180
    rz = np.array([[np.cos(a), np.sin(a), 0, 0], [-np.sin(a), np.cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def machx(kx, cord2):
    rz = np.array([[kx, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def machy(ky, cord2):
    rz = np.array([[1, 0, 0, 0], [0, ky, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def machz(kz, cord2):
    rz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, kz, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)
def machoo(koo, cord2):
    rz = np.array([[koo, 0, 0, 0], [0, koo, 0, 0], [0, 0, koo, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cossxy(kxy, cord2):
    rz = np.array([[1, 0, 0, 0], [kxy, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cossxz(kxz, cord2):
    rz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [kxz, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cossyx(kyx, cord2):
    rz = np.array([[1, kyx, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cossyz(kyz, cord2):
    rz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, kyz, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cosszx(kzx, cord2):
    rz = np.array([[1, 0, kzx, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def cosszy(kzy, cord2):
    rz = np.array([[1, 0, 0, 0], [0, 1, kzy, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    return (cord2)

def go (x, y, z, cord2):
    rg = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]])
    cord2 = cord2.dot(rg)
    return (cord2)

def clic_r ():
    global cord2
    x = ui.doubleSpinBox.value()
    y = ui.doubleSpinBox_2.value()
    z = ui.doubleSpinBox_3.value()
    cord2 = ret_x(x, cord2)
    cord2 = ret_y(y, cord2)
    cord2 = ret_z(z, cord2)
    plott(cord2, mmx)
    return cord2

def clic_m ():
    global cord2
    koo = ui.doubleSpinBox_7.value()
    ox_2 = ui.doubleSpinBox_4.value()
    oy_2 = ui.doubleSpinBox_5.value()
    oz_2 = ui.doubleSpinBox_6.value()
    cord2 = machx(ox_2, cord2)
    cord2 = machy(oy_2, cord2)
    cord2 = machz(oz_2, cord2)
    cord2 = machoo(koo, cord2)
    plott(cord2, mmx)
    return cord2

def clic_cos ():
    global cord2
    kxy = ui.doubleSpinBox_9.value()
    kxz = ui.doubleSpinBox_10.value()
    kyx = ui.doubleSpinBox_8.value()
    kyz = ui.doubleSpinBox_11.value()
    kzy = ui.doubleSpinBox_12.value()
    kzx = ui.doubleSpinBox_13.value()
    cord2 = cossxy(kxy, cord2)
    cord2 = cossxz(kxz, cord2)
    cord2 = cossyx(kyx, cord2)
    cord2 = cossyz(kyz, cord2)
    cord2 = cosszy(kzy, cord2)
    cord2 = cosszx(kzx, cord2)
    plott(cord2, mmx)
    return cord2

def clic_sd():
    global cord2
    ox = ui.doubleSpinBox_14.value()
    oy = ui.doubleSpinBox_15.value()
    oz = ui.doubleSpinBox_16.value()
    cord2 = go(ox, oy, oz, cord2)
    plott(cord2, mmx)
    return cord2

def clic_opp():
    global cord2
    okz = 1/ui.doubleSpinBox_17.value()
    rz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, (okz)], [0, 0, 0, 1]])
    cord2 = cord2.dot(rz)
    b = []
    for i in cord2:
        b.append(i[-1])
    bm = np.array([b])
    print(bm)
    cord2 = cord2 / bm[0][:, None]

def postr():
    global cord3, cord2
    plt.close()
    x = [i[0] for i in cord3]
    y = [i[1] for i in cord3]
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()
    ax.set(xlim=(-50,50), ylim=(-50,50))
    for i, k in zip(swstart, swcon):
        l = Line2D([x[i], x[k]], [y[i], y[k]], color='green')
        ax.add_line(l)
    plt.show()
    cord2 = cord3

def vpis():
    global ax, fig, cord2, sets1, sets2
    plt.close()
    x = [i[0] for i in cord2]
    y = [i[1] for i in cord2]
    z = [i[2] for i in cord2]
    x1 = min(x)
    y1 = min(y)
    z1 = min(z)
    x2 = max(x)
    y2 = max(y)
    cord2 = go(-x1, -y1, -z1, cord2)
    kk = [25/(x2-x1),25 / (y2-y1)]
    cord2 = machoo(min(kk), cord2)
    x = [i[0] for i in cord2]
    y = [i[1] for i in cord2]
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot()
    for i, k in zip(swstart, swcon):
        l = Line2D([x[i], x[k]], [y[i], y[k]], color='green')
        ax.add_line(l)
    ax.set(xlim=(0,25),ylim=(0,25))
    plt.show(block=False)

ui.pushButton_7.clicked.connect(postr)
ui.pushButton.clicked.connect(clic_r)
ui.pushButton_2.clicked.connect(clic_m)
ui.pushButton_3.clicked.connect(clic_cos)
ui.pushButton_4.clicked.connect(clic_sd)
ui.pushButton_5.clicked.connect(clic_opp)
ui.pushButton_6.clicked.connect(vpis)
sys.exit(app.exec_())




