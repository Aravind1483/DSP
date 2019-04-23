#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:18:29 2019

@author: aravind
"""

import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure()      #creating subplots
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
fs,data=wav.read("woman.wav")
d=np.zeros(100)
data=np.append(data,d) #appendig 100 zeroes to get equal number of samples(221) in each window
n=np.ceil(0.01*fs)
A=[] #array of windows
B=[] #array of energies
for i in range(0,200,1):
    x=[]
    for j in range(i*221,(1+i)*221,1):
        x.append(data[j])    #storing elements in windows
    A.append(x)
    a=0
    for k in range(0,221,1):
        a+=(x[k]**2)        #calculating energy
    B.append(a)
C=[]
for i in range (0,200,1):
    for j in range(0,221,1):
        C.append(B[i])
ax1.plot(data)
ax1.set_title("original signal")
ax2.stem(B)
ax2.set_title("energy plot")
ax3.plot(C)
ax3.set_title("energy plot2")

        