from scipy.interpolate import lagrange
import numpy as np 
import matplotlib.pyplot as plt 

x = [20, 40, 60, 80, 100, 120, 140, 160, 180]
y1 = [0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181]
y2 = [3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800]
y3 = [2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200]

p1 = lagrange(x,y1)
p2 = lagrange(x,y2)
p3 = lagrange(x,y3)

t = np.linspace(0,200,200)
f1 = p1(t)
f2 = p2(t)
f3 = p3(t)

dx = 20

L2_1 = dx/p1(30)
L1_1 = L2_1*p3(30)
L3_1 = L2_1*p2(30)

print('dx/L2(30): ', p1(30))
print('\nL3/L2(30): ', p2(30))
print('\nL1/L2(30): ', p3(30))
print('\nL1(30): ', L1_1)
print('\nL2(30): ', L2_1)
print('\nL3(30): ', L3_1)

L2_2 = dx/p1(55)
L1_2 = L2_2*p3(55)
L3_2 = L2_2*p2(55)

print('\ndx/L2(55): ', p1(55))
print('\nL3/L2(55): ', p2(55))
print('\nL1/L2(55): ', p3(55))
print('\nL1(55): ', L1_2)
print('\nL2(55): ', L2_2)
print('\nL3(55): ', L3_2)

plt.figure('2')
plt.plot(t, f1, label='interpolacion')
plt.plot(x, y1, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
plt.figure('2')
plt.plot(t, f2, label='interpolacion')
plt.plot(x, y2, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
plt.figure('2')
plt.plot(t, f3, label='interpolacion')
plt.plot(x, y3, 'x', mew=2, label='Datos')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()