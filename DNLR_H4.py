import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#my symbols
x0, x1, x2, x3, t = sp.symbols('x0, x1, x2, x3, t')

#the polynomial function
pos= x0 + x1*t + x2*t**2 + x3*t**3  #positon
vel = sp.diff(pos,t) #velocity, deravative of positon
acc = sp.diff(vel,t)    #acceleration, deravative of velocity

# initial conditions
#turning every equation to a list to be easier to manipulate
init_pos = pos.subs(t,0)    #[1, 0, 0, 0]
init_pos=str(init_pos).split('+')
final_pos = pos.subs(t,2)  #[1, 2, 4, 8]
final_pos=str(final_pos).split('+')
init_vel = vel.subs(t,0)    #[0, 0, 0, 0]
init_vel=str(init_vel).split('+')
final_vel = vel.subs(t,2)   #[0, 1, 4, 12]
final_vel=str(final_vel).split('+')
#print(final_vel)

#getting our cofficents
a = np.array([[1, 0, 0, 0], [1, 2, 4, 8], [0, 1, 0, 0], [0, 1, 4, 12]])
#initial conditions (initial_position, final_position, initial_velocity, final_velocity)
b = np.array([1, 4, 0, 0])
print(a.shape)

# getting the coffiecients
co_of = np.linalg.solve(a, b)   #[ 1.    0.    2.25 -0.75]
print(co_of)
t = np.linspace(0, 2, 1000)

#problem with ploting a sympy
#position = pos.subs({a0:co_of[0], a1:co_of[1], a2:co_of[2], a3:co_of[3]})
#position = 1.25*t**3 - 4.75*t**2 + 4.0*t + 1.0
p = 1 + 2.25*t**2 -0.75*t**3
v = 2*2.25*t+3*-0.75*t**2
a = 2*2.25+6*-0.75*t
#plot
plt.figure()
plt.plot(t, a)
plt.show()