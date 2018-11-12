import math
from numpy import *
#Datos Hidraulicos
Q= float(input("Caudal: "))
#Datos Geometricos
h1 = float(input("h1: "))
h2 = float(input("h2: "))
H = float(input("H: "))
b0 = float(input("b0: "))
# b1 = input("b1: ")
# b2 = input("b2: ")
m1 = float(input("m1: "))
m2 = float(input("m2: "))
b1=100
b2=b1
m3 = float(input("m3: "))
m4 = float(input("m4: "))
#calculos
h3 = H - h1
h4 = H - h2
yc = 0.5
dyc = 0.01
if h1 == h2:
	while abs(dyc) > 0.0001:
		At = (2*b0 + yc*m1 + yc*m2)*(yc/2)
		Pm = b0 + yc*(1+m1**2)**0.5 + yc*(1+m2**2)**0.5
		Rh = A/Pm
		T = b0 +yc*m1+yc*m2
		Dh = At/T
		Fr = At**(3/2)/(T)**0.5 - Q/(9.81)**0.5
		dFr = 1.5*(At*T)**0.5 - 1/2*(m1+m2)*Dh**3/2
		yc = yc - Fr/dFr
		dyc = -Fr/dFr
		print(yc)
if h2 > h1:
	yc=0.01
	yc1=0.01
	yc2=0.01
	yc3=0.01
	A1=(2*b0+h1*(m1+m2))*(h1/2)
	T1=b0+h1*(m1+m2)
	At=A1+(2*T1+2*b1+(h2-h1)*(m1+m3))*((h2-h1)/2)
	T=T1+b1+(h2-h1)*(m1+m3)
	Fr=2
	while Fr>=1:
		Fr=Q*((b0+yc*(m1+m2))/(9.81*((2*b0+yc*(m1+m2))*(yc/2))**3))**0.5
		yc=yc+0.001
	fo=2
	yc1 = yc- 0.001
	if h2>yc1 and yc1>=h1:
		while fo>=1:
			fo=Q*((T1+b1+(yc1-h1)*(m1+m3))/(9.81*((A1+(2*T1+2*b1+(yc1-h1)*(m1+m3)*(yc1-h1)/2))**3)))**0.5
			yc1=yc1+0.001
	yc2=yc1-0.001
	ft=2
	if H>yc2 and yc2>=h2:
		while(ft>=1):
			ft=Q*((T+b2+(yc2-h2)*(m3+m4))/(9.81*((At+(2*T+2*b2+(yc2-h2)*(m3+m4))*(yc2-h2)/2)**3)))**0.5
			yc2=yc2+0.001
	yc3=yc2-0.001;
	if yc3>H:
		print('canal desbordado')
if h1>h2:
    yc=0.01
    yc1=0.01
    yc2=0.01
    yc3=0.01
    A1=(2*b0+h2*(m1+m2))*(h2/2)
    T1=b0+h2*(m1+m2)
    At=A1+(2*T1+2*b2+(h1-h2)*(m2+m4))*((h1-h2)/2)
    T=T1+b2+(h1-h2)*(m2+m4)
    Fr=2
    while (Fr>=1):
      Fr=Q*((b0+yc*(m1+m2))/(9.81*((2*b0+yc*(m1+m2))*(yc/2))**3))**0.5
      yc=yc+0.001
    fo=2
    yc1=yc-0.001
    if h1>yc1 and yc1>=h2:
         while (fo>=1):
             fo=Q*((T1+b2+(yc1-h2)*(m2+m4))/(9.81*((A1+(2*T1+2*b2+(yc1-h2)*(m2+m4)*(yc1-h2)/2))**3)))**0.5
             yc1=yc1+0.001
    yc2=yc1-0.001
    ft=2
    if H>yc2 and yc2>=h1:
        while (ft>=1):
            ft=Q*((T+b1+(yc2-h1)*(m3+m4))/(9.81*((At+(2*T+2*b1+(yc2-h1)*(m3+m4))*(yc2-h1)/2)**3)))**0.5
            yc2=yc2+0.001
    yc3=yc2-0.001
    if (yc3>H):
        print('canal desbordado')                   
print(yc)
resultados = array([round(Fr,2),round(yc,4),At,T])
print(resultados)