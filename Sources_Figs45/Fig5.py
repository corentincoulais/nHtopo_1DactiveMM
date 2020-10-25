# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:01:22 2019

@author: coulais
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] =  20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['figure.subplot.left'] = 0.25
mpl.rcParams['figure.subplot.right'] = 0.95
mpl.rcParams['figure.subplot.bottom'] = 0.15
mpl.rcParams['figure.subplot.top'] = 0.95
#mpl.rcParams['figure.figsize']=[ 8,8]
#mpl.rcParams['font.family']='Times'
#mpl.rcParams['axes.labelsize'] = 38
mpl.rcParams['lines.linewidth']=5
mpl.rcParams['axes.linewidth']= 3
mpl.rcParams['xtick.major.size']= 8
mpl.rcParams['xtick.major.width']=3
mpl.rcParams['xtick.major.pad']=2
mpl.rcParams['ytick.major.pad']=2
mpl.rcParams['ytick.major.size']= 8
mpl.rcParams['ytick.major.width']=3
mpl.rcParams['xtick.minor.size']= 0#7.5
mpl.rcParams['xtick.minor.width']=0
mpl.rcParams['ytick.minor.size']= 0#7.5
mpl.rcParams['ytick.minor.width']=0
mpl.rcParams['ytick.minor.width']=0
mpl.rcParams['ytick.direction']="in"
mpl.rcParams['xtick.direction']="in"


mpl.rcParams['legend.fontsize']=22;

dat1=np.loadtxt("OpenSystem_response/1-5_on-6-9 off.txt",skiprows=1)
    
#define plot
fig1 = plt.figure(1,figsize=(10,6))
ax1 = fig1.add_axes([0.14,0.25,0.85,0.7])
ax1.set_ylabel(r'ang. disp. field $\delta\theta$ (rad)',fontsize=24)
ax1.set_xlabel(r'site $n$',fontsize=24)


ax1.plot([5.5,5.5],[0,3],c="k",ls="--",lw=1)

ii=[0,10,9,8,7,6,5,4,3,2,1]

for i,c in zip(ii,["gray"]*7+["DeepPink"]*5):
    ax1.plot(range(1,len(dat1[i,3:])+1),np.flipud(dat1[i,3:])+(6-i)*0,c=c,lw=5,marker="o",markersize=10)

ax1.annotate(r"$\varepsilon$",xy=(9.3,0.06),color="k",horizontalalignment='right', verticalalignment='bottom',size=25)

ax1.set_xlim(0.5,9.5)
ax1.set_ylim(0,0.07)
ax1.set_yticks([0,0.03,0.06])
ax1.set_xticks([1,2,3,4,5,6,7,8,9])
fig1.savefig("fig5_panelA.pdf")



dat1=np.loadtxt("OpenSystem_response/1-5_off-6-9 on.txt",skiprows=1)
    
#define plot
fig2 = plt.figure(2,figsize=(10,6))
ax2 = fig2.add_axes([0.14,0.25,0.85,0.7])
ax2.set_ylabel(r'ang. disp. field $\delta\theta$ (rad)',fontsize=24)
ax2.set_xlabel(r'site $n$',fontsize=24)

ax2.plot([5.5,5.5],[0,3],c="k",ls="--",lw=1)

ii=[0,10,9,8,7,6,5,4,3,2,1]


for i,c in zip(ii,["gray"]*7+["DeepPink"]*5):
    ax2.plot(range(1,len(dat1[i,3:])+1),np.flipud(dat1[i,3:])+(6-i)*0,c=c,lw=5,marker="o",markersize=10)


ax2.annotate(r"$\varepsilon$",xy=(0.8,0.05),color="k",horizontalalignment='center', verticalalignment='center',size=25)

ax2.set_xlim(0.5,9.5)
ax2.set_ylim(0,0.07)
ax2.set_yticks([0,0.03,0.06])
ax2.set_xticks([1,2,3,4,5,6,7,8,9])
fig2.savefig("fig5_panelB.pdf")