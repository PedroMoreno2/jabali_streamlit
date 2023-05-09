import os
import streamlit as st
import random
cesped="V"
cesped_cortado="."
jardinero="@"
jabali="J"
ancho=[0,1,2,3,4]
a=[]
b=[]
c=[]
d=[]
e=[]
mapa=[a,b,c,d,e]
def mapa_nuevo():
  for fila in mapa:
    fila.clear()
    for columna in ancho:
      fila.append(cesped)      
mapa_nuevo()
def mapea():
  for linea in mapa:
    for y in linea:
      st.write(y)

# colocar al jardinero y al jabali, necesito las coordenadas del jardinero

posicion=[0,0]
mapa[0][0]=jardinero
jabali_posicion=0
jabali_posicion=[random.randint(1,4),random.randint(1,4)]
mapa[jabali_posicion[1]][jabali_posicion[0]]=jabali

# Movimiento del jabali:
def jabali_mueve():
  jabali_posicion[0]+=random.randint(-1,1)
  jabali_posicion[1]+=random.randint(-1,1)
  if jabali_posicion[0]<0:
    jabali_posicion[0]=0
  elif jabali_posicion[0]>4:
    jabali_posicion[0]=4
  elif jabali_posicion[1]>4:
    jabali_posicion[1]=4
  elif jabali_posicion[1]>4:
    jabali_posicion[1]=4 
  mapa[jabali_posicion[1]][jabali_posicion[0]]=jabali

# definiendo el movimiento de @ y J, y el cortado de cesped, meter a @ en la nueva posicion y dejar cesped cortado donde estaba:
def movimiento():
  mueve=0
  while mueve!="q":
    mueve=st.text_input("mueve:")
    mapa[posicion[1]][posicion[0]]=cesped_cortado
    mapa[jabali_posicion[1]][jabali_posicion[0]]=cesped_cortado
    if mueve=="4":
      posicion[0]-=1
    elif mueve=="6":
      posicion[0]+=1
    elif mueve=="2":
      posicion[1]+=1
    elif mueve=="8":
      posicion[1]-=1   
    mapa[posicion[1]][posicion[0]]=jardinero
    if  jabali_posicion==posicion:
      os.system("cls")
      st.write("pillaste al jabali")
      mapea()
      break
    jabali_mueve()
    if  jabali_posicion==posicion:
      os.system("cls")
      st.write("el jabali te pilla")
      mapea()
      break
    os.system("cls")
    mapea()
mapea()
movimiento()
