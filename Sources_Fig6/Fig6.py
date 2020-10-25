# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:38:10 2019

@author: coulais
"""
import numpy as np
from numpy import linalg as LA
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import operator
from functools import reduce 


mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['xtick.labelsize'] =  24
mpl.rcParams['ytick.labelsize'] = 24
mpl.rcParams['figure.subplot.left'] = 0.25
mpl.rcParams['figure.subplot.right'] = 0.95
mpl.rcParams['figure.subplot.bottom'] = 0.15
mpl.rcParams['figure.subplot.top'] = 0.95
#mpl.rcParams['figure.figsize']=[ 8,8]
#mpl.rcParams['font.family']='Times'
mpl.rcParams['lines.linewidth']=1
mpl.rcParams['axes.linewidth']= 1
mpl.rcParams['xtick.major.size']= 5
mpl.rcParams['xtick.major.width']=1
mpl.rcParams['xtick.major.pad']=8
mpl.rcParams['ytick.major.pad']=8
mpl.rcParams['ytick.major.size']= 5
mpl.rcParams['ytick.major.width']=1
mpl.rcParams['xtick.minor.size']= 0#7.5
mpl.rcParams['xtick.minor.width']=0
mpl.rcParams['ytick.minor.size']= 0#7.5
mpl.rcParams['ytick.minor.width']=0


mpl.rcParams['legend.fontsize']=22;

dateven=np.loadtxt("./even.dat")
datodd=np.loadtxt("./odd.dat")
    
fig1=plt.figure(1,figsize=(8,6))
ax1=fig1.add_axes([0.15,0.14,0.8,0.8])

gammaEP1=(1-2.5)/(1+2.5)
gammaEP2=(1+2.5)/(1-2.5)
gammaZhong1=(1-2.5**2)/(1+2.5**2)
gammaZhong2=(1+2.5**2)/(1-2.5**2)
print(gammaEP1,gammaEP2)

ax1.axvspan(gammaEP2, gammaEP1, facecolor="Pink",alpha=0.3,linewidth=0)
ax1.scatter(datodd[:,0],datodd[:,-1])
ax1.set_xlabel("epsilon")


fig10=plt.figure(10,figsize=(8,6))
ax10=fig10.add_axes([0.15,0.14,0.8,0.8])

ax10.axvspan(-gammaEP2,2.5, facecolor="LightGray",alpha=0.5,linewidth=0,zorder=0)
ax10.axvspan(0,-gammaEP1, facecolor="LightGray",alpha=0.5,linewidth=0,zorder=0)
ax10.axvspan(-gammaEP2, -gammaEP1, facecolor="Pink",alpha=0.5,linewidth=0,zorder=0)

ax10.plot([-gammaEP2,-gammaEP2],[-0.5,5],color='DeepPink',lw=3,zorder=20)
ax10.plot([-gammaEP1,-gammaEP1],[-0.5,5],color='DeepPink',lw=3,zorder=20)

ax10.plot([-gammaZhong1,-gammaZhong1],[-0.5,5],color='b',lw=1.5,ls="--",zorder=19)
ax10.plot([-gammaZhong2,-gammaZhong2],[-0.5,5],color='b',lw=1.5,ls="--",zorder=19)

epsilon=np.zeros(200)
edgemode=np.zeros(200)
bulksup=np.zeros(200)
bulkinf=np.zeros(200)
for i in range(200):
    epsilon[i]=datodd[99*i,0]
    tmp=datodd[i*99:(i+1)*99,-1]
    ix=tmp.argmin()
    edgemode[i]=tmp[ix]
    tmp2= np.delete(tmp, ix)
    bulksup[i]=tmp2.max()
    bulkinf[i]=tmp2.min()
    
ax10.plot(-epsilon,edgemode,color='Black',lw=3)
ax10.fill_between(-epsilon,bulkinf,bulksup,alpha=1,color="gray")#,zorder=10)

ax10.set_xlabel(r"$\varepsilon$")
ax10.set_ylabel(r"$|$Eigenvalues$|$")
ax10.set_ylim(-0.5,4.5)
ax10.set_xlim(0,2.5)
ax10.set_xticks([0,0.5,1,1.5,2,2.5])
ax10.set_xticklabels([0,0.5,1,1.5,2,2.5])


fig10.savefig("./Fig6_panelA.pdf" ) 

fig2=plt.figure(2,figsize=(8,6))
ax2=fig2.add_axes([0.15,0.14,0.8,0.8])

gammaEP1=(1-2.5)/(1+2.5)
gammaEP2=(1+2.5)/(1-2.5)
gammaZhong1=(1-2.5**2)/(1+2.5**2)
gammaZhong2=(1+2.5**2)/(1-2.5**2)
print(gammaEP1,gammaEP2)

ax2.axvspan(gammaEP2, gammaEP1, facecolor="Pink",alpha=0.3,linewidth=0)
ax2.scatter(dateven[:,0],dateven[:,-1])
ax2.set_xlabel("epsilon")
    
fig11=plt.figure(11,figsize=(8,6))
ax11=fig11.add_axes([0.15,0.14,0.8,0.8])

ax11.axvspan(-gammaEP2,2.5, facecolor="LightGray",alpha=0.5,linewidth=0,zorder=0)
ax11.axvspan(0,-gammaEP1, facecolor="LightGray",alpha=0.5,linewidth=0,zorder=0)
ax11.axvspan(-gammaEP2, -gammaEP1, facecolor="Pink",alpha=0.5,linewidth=0,zorder=0)

ax11.plot([-gammaEP2,-gammaEP2],[-0.5,5],color='DeepPink',lw=3,zorder=20)
ax11.plot([-gammaEP1,-gammaEP1],[-0.5,5],color='DeepPink',lw=3,zorder=20)

ax11.plot([-gammaZhong1,-gammaZhong1],[-0.5,5],color='b',lw=1.5,ls="--",zorder=19)
ax11.plot([-gammaZhong2,-gammaZhong2],[-0.5,5],color='b',lw=1.5,ls="--",zorder=19)

epsilon=np.zeros(200)
edgemode=np.zeros(200)
edgemode2=np.zeros(200)
bulksup=np.zeros(200)
bulkinf=np.zeros(200)
for i in range(200):
    epsilon[i]=dateven[100*i,0]
    tmp=dateven[i*100:(i+1)*100,-1]
    ix=tmp.argmin()
    edgemode[i]=tmp[ix]
    tmp2= np.delete(tmp, ix)
    ix2=tmp2.argmin()
    edgemode2[i]=tmp2[ix2]
    tmp3= np.delete(tmp2, ix2)
    bulksup[i]=tmp3.max()
    bulkinf[i]=tmp3.min()
    
ax11.plot(-epsilon,edgemode,color='Black',lw=3)
ax11.fill_between(-epsilon,bulkinf,bulksup,alpha=1,color="gray")#,zorder=10)

ax11.set_xlabel(r"$-\varepsilon$")
ax11.set_ylabel(r"$|$Eigenvalues$|$")
ax11.set_ylim(-0.5,4.5)
ax11.set_xlim(0,2.5)
ax11.set_xticks([0,0.5,1,1.5,2,2.5])
ax11.set_xticklabels([0,0.5,1,1.5,2,2.5])


fig11.savefig("./Fig6_panelB.pdf" )
