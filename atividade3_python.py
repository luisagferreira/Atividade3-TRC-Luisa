import numpy as np
import pint
import matplotlib.pyplot as plt
import plotly.graph_objects as go

### DADOS DO EXEMPLO 5.11 (pág. 569 incropera) ###


q1=1*10**(7)
q2=2*10**(7)
alfa=5*10**(-6)
print(alfa)
L=0.01
k=30
Tinf=250
h=1100
deltax=0.002 #m

## CALCULANDO O VALOR DO Bi ##

Bi=(h*deltax)/k
print(Bi)

## CRITÉRIO DE ESTABILIDADE ##

valor =(1/2)/(1+Bi)
#print(valor)
if valor <=(1/2)/(1+Bi):
    F0=valor
print("F0= ",F0)

deltat=((F0*(deltax)**2)/alfa)
print("Deltat=",deltat)

T5=Tinf+(((10**(7))*0.01)/h)
print("T5=",T5)

### CALCULANDO AS TEMPERATURAS INICIAIS ###
print("IMPRIMINDO AS TEMPERATURAS INICIAIS")
print("                                   ")



Tvet=[]
print("Nós\t\t\tTemperaturas Iniciais")
for i in range(1,7):
    x=(i-1)*deltax
    Tvet=q1*(L**2)/(2*k)*(1-(x**2)/(L**2))+T5
    print(i,"   ","       ",Tvet)


print("__________________________________________________")

"""
### REGISTRANDO AS TEMPERATURAS NODAIS ###

p=1
t=0
tfinal=1.5

T=np.zeros((6,8))

while (t<tfinal):
    p=p+1
    t=deltat*(p-1)

T[i,p]=np.zeros((7,7))
for i in range(1,7):
    x=(i-1)*deltax
    if i==1:
        T[i,p] =F0*(2*T[i+1,p-1]+(q2*((deltax**2)/k)))+(1-2*F0)*T[i,p-1]

    elif i==6:
        T[i, p] = 2*F0 * (T[i + 1, p - 1] + (Bi*Tinf+ q2 * ((deltax ** 2) /(2*k))))+(1 - 2 * (F0-2)*Bi*F0) * T[i, p - 1]
        #print(T[i, p])

    else:
        T[i, p] = F0 * (T[i + 1, p - 1] +(T[i + 1, p - 1])+ (q2 * ((deltax ** 2) / k))) + (1 - 2 * F0) * T[i, p - 1]
        #print(T[i, p])

        #tab=np.array2string(T, precision=3)
    print(p, "     ", i, "        ", T)

"""