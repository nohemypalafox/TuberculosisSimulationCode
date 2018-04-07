import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()

Lambda=35
mu=0.016
betap=7

beta=7
c=5
d=0.1
k=0.005
r1=3
r2=1


N=5000

def f(y,t):
    S=y[0]
    L=y[1]
    I=y[2]
    T=y[3]
    f0= Lambda - beta*c*S*(I/N) - mu*S
    f1= beta*c*S*(I/N) - (mu+k+r1)*L + betap*c*T*(I/N)
    f2= k*L - (mu+d+r2)*I
    f3= r1*L +r2*I - betap*c*T*(I/N) - mu*T
    return[f0,f1,f2,f3]
#Condiciones iniciales
S=0
L=3000
I=500
T=1500
y0=[S,L,I,T]
t= np.linspace(0,500.0,1000)

sol=odeint(f,y0,t)
S=sol[:,0]
L=sol[:,1]
I=sol[:,2]
T=sol[:,3]

plt.subplots_adjust(hspace=.4,wspace=.4)


#plt.figure()
plt.subplot(221)
plt.plot(t,S,label="Susceptibles")
plt.xlabel("dias")
plt.ylabel("Susceptibles")

plt.subplot(222)
plt.plot(t,L,label="Latentes")
plt.xlabel("Anos")
plt.ylabel("Latentes")

plt.subplot(223)
plt.plot(t,I,label="Infectados")
plt.xlabel("Anos")
plt.ylabel("Infectados")

plt.subplot(224)
plt.plot(t,T,label="Efectivamente Tratados")
plt.xlabel("Anos")
plt.ylabel("Tratados")


plt.show()