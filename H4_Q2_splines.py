#question 2
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#for our first spline form q0 to q2
#our initial conditions
x0, x1, x2, x3, t = sp.symbols('x0, x1, x2, x3, t')#symbols

#basic polynomial equation
pos = x0 + x1*t + x2*t**2 + x3*t**3  #positon
vel = pos.diff(t)  #velocity
acc = vel.diff(t)  #acceleration


mid_pos = pos.subs(t,2)
mid_pos=str(mid_pos).split('+')
final_pos = pos.subs(t,4)
final_pos=str(final_pos).split('+')
final_vel = vel.subs(t,0)
final_vel=str(final_vel).split('+')
final_acc = acc.subs(t,0)
final_acc=str(final_acc).split('+')

'''
#print(init_pos)
print(mid_pos)
print(final_pos)
#print(init_vel)
print(final_vel)
#print(init_acc)
print(final_acc)
'''

#first spline matrices
#getting our cofficents
a = np.array([[1, 0, 0, 0],
              [1, 2, 4, 8],
              [0, 1, 0, 0],
              [0, 0, 2, 0],
              ])

#initial conditions
b = np.array([1, 2, 0, 0])

co_of_spline_1 = np.linalg.solve(a, b)
t_1 = np.linspace(0, 2, 1000)
p_1 = co_of_spline_1[0]+co_of_spline_1[1]*t_1+co_of_spline_1[2]*t_1**2+co_of_spline_1[3]*t_1**3
v_1 = co_of_spline_1[1]+2*co_of_spline_1[2]*t_1+3*co_of_spline_1[3]*t_1**2
a_1 = 2*co_of_spline_1[2]+6*co_of_spline_1[3]*t_1

#second spline matrices
#getting our cofficents
c = np.array([[1, 2, 4, 8],
              [1, 4, 16, 64],
              [0, 1, 0, 0],
              [0, 0, 2, 0],
              ])

#initial conditions
d = np.array([2, 4, 0, 0])

co_of_spline_2 = np.linalg.solve(c, d)


t_2=np.linspace(2, 4, 1000)
p_2 = co_of_spline_2[0]+co_of_spline_2[1]*t_2+co_of_spline_2[2]*t_2**2+co_of_spline_2[3]*t_2**3
v_2 = co_of_spline_2[1]+2*co_of_spline_2[2]*t_2+3*co_of_spline_2[3]*t_2**2
a_2 = 2*co_of_spline_2[2]+6*co_of_spline_2[3]*t_2

#plot
plt.figure()
plt.plot(t_1, p_1)
plt.plot(t_2, p_2)
plt.show()



