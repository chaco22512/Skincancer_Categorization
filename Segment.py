# -*- coding: utf-8 -*-
from data import*
import cv2
import numpy as np
import pandas as pd
import math


def segment(file_list):

  file_list1 = [None for i in range(len(file_list))]
  index= [None for i in range(len(file_list))]
  Seg = [None for i in range(len(file_list))]
  CX = [None for i in range(len(file_list))]
  CY = [None for i in range(len(file_list))]
  Area = [None for i in range(len(file_list))]
  Peri = [None for i in range(len(file_list))]
  Dia = [None for i in range(len(file_list))]
  Asy = [None for i in range(len(file_list))]
  Cir = [None for i in range(len(file_list))]
  Bord = [None for i in range(len(file_list))]
  Comp = [None for i in range(len(file_list))]


  for i in range(len(file_list)):
    file_list1[i] = cv2.cvtColor(file_list[i], cv2.COLOR_BGR2GRAY)#gray scale
    _, file_list1[i] = cv2.threshold(file_list1[i], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    file_list1[i] = cv2.blur(file_list1[i], (10, 10));
    im2, contours, hierarchy = cv2.findContours(file_list1[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)>=2 :
      h, w = file_list1[i].shape
      mask = np.zeros((h + 2, w + 2), np.uint8)
      _,I4,_,_=cv2.floodFill(file_list1[i],mask,(1,1),0,)
      _,I4,_,_=cv2.floodFill(file_list1[i],mask,(w-1,1),0,)
      _,I4,_,_=cv2.floodFill(file_list1[i],mask,(w-1,h-1),0,)
      _,I4,_,_=cv2.floodFill(file_list1[i],mask,(1,h-1),0,)

    else: pass

    im2, contours2, hierarchy = cv2.findContours(file_list1[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours2)==1:
      Seg[i]=True
      cv2.drawContours(file_list[i],contours2,-1, (0,255,0),3)
      #feature of contours
      cnt = contours2[0]
      M=cv2.moments(cnt)
      #centeroid
      cx = str(M['m10']/M['m00'])
      cy = str(M['m01']/M['m00'])
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv2.circle(file_list[i],(cx,cy),10,(0,255,0),-1)

      CX[i]=cx
      CY[i]=cy
      Area[i] = cv2.contourArea(cnt)
      Peri[i] = cv2.arcLength(cnt,True)

      x,y,w,h = cv2.boundingRect(cnt)
      Dia[i] = max(w,h)
      Asy[i] = w/h
      Cir[i] = (4*Area[i])/(Peri[i]**2)
      Bord[i] = (Peri[i]**2)/(Area[i])
      Comp[i] = (Peri[i]**2)/(4*math.pi*Area[i])


    else:
      Seg[i]=False
      CX[i]=np.nan
      CY[i]=np.nan
      Area[i] = np.nan
      Peri[i] = np.nan
      Dia[i] = np.nan
      Asy[i] = np.nan
      Cir[i] = np.nan
      Bord[i] = np.nan
      Comp[i] = np.nan


      pass
    
    index[i]=i

  index=np.array(index)
  Seg=np.array(Seg)
  CX=np.array(CX)
  CY=np.array(CY)
  Area=np.array(Area)
  Peri=np.array(Peri)
  Dia=np.array(Dia)
  Asy=np.array(Asy)
  Cir=np.array(Cir)
  Bord=np.array(Bord)
  Comp=np.array(Comp)

  index1=index.reshape(-1,1)
  Seg=Seg.reshape(-1,1)
  CX=CX.reshape(-1,1)
  CY=CY.reshape(-1,1)
  Area=Area.reshape(-1,1)
  Peri=Peri.reshape(-1,1)
  Dia=Dia.reshape(-1,1)
  Asy=Asy.reshape(-1,1)
  Cir=Cir.reshape(-1,1)
  Bord=Bord.reshape(-1,1)
  Comp=Comp.reshape(-1,1)   

  Matrix = np.hstack([Seg,CX,CY,Area,Peri,Dia,Asy,Cir,Bord,Comp])
  df =pd.DataFrame(data=Matrix, index=index,
              columns=['Seg', 'CX', 'CY', 'Area', 'Peri','Dia','Asy','Cir','Bord','Comp'])
  
  return df