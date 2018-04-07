import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()

mu=0.0143
beta=13
betap=0.02900898
c=1
k=1
q=0
p=0.5
r1=1
r2=2
kp=1
Lambda=35
d=0
dp=0

def f(y,t):
    x1=y[0]
    x2=y[1]
    y1=y[2]
    y2=y[3]
    f0=beta*c*(1.0-x1-x2-y1-y2)*x2-(mu+k+r1)*x1+p*r2*x2-betap*c*x1*y2
    f1=k*x1 -(mu+r2)*x2
    f2=q*r2*x2 -(mu+kp)*y1 +betap*c*(1.0-x2-y1-y2)*y2
    f3=kp*y1-mu*y2
    return[f0,f1,f2,f3]

#Condiciones iniciales
x1=0.1
x2=0.04964503797845406
y1=0.013
y2=0.9090909090909091
y0=[x1,x2,y1,y2]
t= np.linspace(0,10.0,1000)

sol=odeint(f,y0,t)
x1=sol[:,0]
x2=sol[:,1]
y1=sol[:,2]
y2=sol[:,3]

#plt.figure()
plt.plot(x1+y1,x2+y2,label="Latentes vs Infectados")
plt.xlabel("x1+y1")
plt.ylabel("x2+y2")


plt.show()