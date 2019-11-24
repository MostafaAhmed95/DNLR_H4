#question 2
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#our initial conditions
x0, x1, x2, x3, x4, x5, x6, t = sp.symbols('x0, x1, x2, x3, x4, x5, x6, t')#symbols

#basic polynomial equation
pos = x0 + x1*t + x2*t**2 + x3*t**3+x4*t**4+x5*t**5+x6*t**6  #positon
vel = pos.diff(t)  #velocity
acc = vel.diff(t)  #acceleration


init_pos = pos.subs(t,0)
init_pos=str(init_pos).split('+')
mid_pos = pos.subs(t,2)
mid_pos=str(mid_pos).split('+')
final_pos = pos.subs(t,4)
final_pos=str(final_pos).split('+')
init_vel = vel.subs(t,0)
init_vel=str(init_vel).split('+')
final_vel = vel.subs(t,4)
final_vel=str(final_vel).split('+')
init_acc = acc.subs(t,0)
init_acc=str(init_acc).split('+')
final_acc = acc.subs(t,4)
final_acc=str(final_acc).split('+')
'''
print(init_pos)
print(mid_pos)
print(final_pos)
print(init_vel)
print(final_vel)
print(init_acc)
print(final_acc)
'''
#getting our cofficents
a = np.array([[1, 0, 0, 0, 0, 0, 0],
              [1, 2, 4, 8, 16, 32, 64],
              [1, 4, 16, 64,256,1024,4096],
              [0, 1, 0, 0,0,0,0],
              [0, 1, 8, 48,256,1280,6144],
              [0, 0, 2, 0,0,0,0],
              [0, 0, 2, 24,192,1280,7680]
              ])

#initial conditions
b = np.array([1, 2, 0, 0, 0, 0, 0])

co_of = np.linalg.solve(a, b)
#print(co_of)
t = np.linspace(0, 2, 1000)

p = co_of[0]+co_of[1]*t+co_of[2]*t**2+co_of[3]*t**3+co_of[4]*t**4+co_of[5]*t**5+co_of[6]*t**6
v = co_of[1]+2*co_of[2]*t+3*co_of[3]*t**2+4*co_of[4]*t**3+5*co_of[5]*t**4+6*co_of[6]*t**5
a = 2*co_of[2]+6*co_of[3]*t+12*co_of[4]*t**2+20*co_of[5]*t**3+30*co_of[6]*t**4

#plot
plt.figure()
plt.plot(t, a)
plt.show()



