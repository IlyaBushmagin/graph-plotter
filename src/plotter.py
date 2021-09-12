from math import *
from tkinter import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Set initial values
print("y = a * sin(b * x + c) - d * cos(g * x ** 2 + f * x + h)")
print("a = 1")
print("b = 1")
print("c = 3.14")
print("d = -1")
print("g = 1")
print("f = 0")
print("h = 0")
a = 1
b = 1
c = 3.14
d = -1
g = 1
f = 0
h = 0

print("X = [-10 ... 10]")
x_min = -10
x_max = 10

print("Number of points: 1000")
cnt_dots = 1000

print("Drawing type (points - 1, line - 0): 0")
tp = 0

print("Line thickness: 1")
thkns = 1

print("Background color: white")
bg_clr = "white"

print("Graph color: red")
plt_clr = "red"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculating function values
x_vals = []
y_vals = []
x = x_min
x_delta = x_max - x_min
x_step = x_delta / (cnt_dots - 1)
for i in range(cnt_dots):
	x_vals.append(x)
	y_vals.append(a * sin(b * x + c) - d * cos(g * x ** 2 + f * x + h))
	x += x_step

y_min = min(y_vals)
y_max = max(y_vals)

y_delta = y_max - y_min

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Axis shift
if x_delta > y_delta:
	axis_size = x_delta
	OY_val = (y_max + y_min) / 2 + axis_size / 2
	OY_shift = OY_val - y_max
	OX_shift = 0
	OX_val = x_min
elif y_delta > x_delta:
	axis_size = y_delta
	OX_val = (x_min + x_max) / 2 - axis_size / 2
	OX_shift = x_min - OX_val
	OY_shift = 0
	OY_val = y_max
else:
	axis_size = x_delta
	OX_val = x_min
	OY_val = y_max
	OX_shift = 0
	OY_shift = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Start drawing
root = Tk()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Setting the drawing area
canv = Canvas(root, width = 601, height = 601, bg = bg_clr)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Draw axis
canv.create_line(302, 2, 302, 602, width = 1)
canv.create_line(2, 302, 602, 302, width = 1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Marking axis
cord = 2
step = axis_size / 8
for i in range(9):
	canv.create_line(298, cord, 307, cord, width = 1)
	canv.create_text(340, cord, text = str(round(OY_val, 5)), font=("Consolas", "8"))
	canv.create_line(cord, 298, cord, 307, width = 1)
	canv.create_text(cord, 290, text = str(round(OX_val, 5)), font=("Consolas", "8"))
	OX_val += step
	OY_val -= step
	cord += 75

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Drawing a graph
k = axis_size / 600
if tp == 1:
	for i in range(cnt_dots):
		x = (x_vals[i] - x_min + OX_shift) / k
		y = (y_max + OY_shift - y_vals[i]) / k
		canv.create_oval(x + 1, y + 1, x + 3, y + 3, outline = plt_clr, fill = plt_clr)
else:
	for i in range(cnt_dots - 1):
		x1 = (x_vals[i] - x_min + OX_shift) / k
		y1 = (y_max + OY_shift - y_vals[i]) / k
		x2 = (x_vals[i + 1] - x_min + OX_shift) / k
		y2 = (y_max + OY_shift - y_vals[i + 1]) / k
		canv.create_line(x1 + 2, y1 + 2, x2 + 2, y2 + 2, width = thkns, fill = plt_clr)

canv.pack()
root.mainloop()
