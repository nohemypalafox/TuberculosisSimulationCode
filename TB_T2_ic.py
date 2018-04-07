import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()

mu=0.143
Lambda=500

q=0
d=0
dp=0
beta=3
betap=0.3
c=2
p=0.5
r1=2
r2=1
k=1
kp=1

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
x1=0.60
x2=0.25
y1=0.10
y2=0.05
y0=[x1,x2,y1,y2]
t= np.linspace(0,500.0,1000)

sol=odeint(f,y0,t)
x1=sol[:,0]
x2=sol[:,1]
y1=sol[:,2]
y2=sol[:,3]

plt.subplots_adjust(hspace=.4,wspace=.4)

#plt.figure()
plt.subplot(221)
plt.plot(t,x1,label="Latentes1")
plt.xlabel("Anos")
plt.ylabel("Fraccion de Latentes")

plt.subplot(222)
plt.plot(t,x2,label="Infecciosos1")
plt.xlabel("Anos")
plt.ylabel("Fraccion de Infecciosos")

plt.subplot(223)
plt.plot(t,y1,label="Latentes2")
plt.xlabel("Anos")
plt.ylabel("Fraccion de Latentes Resistentes")

plt.subplot(224)
plt.plot(t,y2,label="Infecciosos2")
plt.xlabel("Anos")
plt.ylabel("Fraccion de Infecciosos Resitentes")

plt.show()