# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:38:10 2019

@author: coulais
"""
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import pandas as pd
import operator
import matplotlib as mpl
from functools import reduce 
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
cmapcustom = LinearSegmentedColormap.from_list('mycmap', ['#DCE11F', 'white', '#6DBF51'])

mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['xtick.labelsize'] =  24
mpl.rcParams['ytick.labelsize'] = 24
mpl.rcParams['figure.subplot.left'] = 0.25
mpl.rcParams['figure.subplot.right'] = 0.95
mpl.rcParams['figure.subplot.bottom'] = 0.15
mpl.rcParams['figure.subplot.top'] = 0.95
#mpl.rcParams['figure.figsize']=[ 8,8]
#mpl.rcParams['font.family']='Times'
mpl.rcParams['axes.labelsize'] = 42
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
mpl.rcParams['ytick.direction']="in"
mpl.rcParams['xtick.direction']="in"
#functions
def KL_Dyn_periodic(a1,a2,b1,N):
    D=np.diag([a1]*(N-1),1)+np.diag([a2]*(N-1),-1)+np.diag([b1]*(N))+np.diag([a2],N-1)+np.diag([a1],-N+1)
    return D
    
def KL_Dyn_open(a1,a2,b1,N,b11,b1N):
    D=np.diag([a1]*(N-1),1)+np.diag([a2]*(N-1),-1)+np.diag([b1]*(N))
    D[0,0]=b11
    D[-1,-1]=b1N
    return D

    
def KL_Eig(N,a,b,epsilon,rho,BC="periodic"):
    #parameters
    a1=-a*b*(1+epsilon-rho)
    a2=-a*b*(1-epsilon-rho)
    b1=a**2*(1-epsilon+rho)+b**2*(1+epsilon+rho)        
    #define hamiltonian
    if BC == "periodic":
        D=KL_Dyn_periodic(a1,a2,b1,N)
    elif BC== "open":
        D=KL_Dyn_open(a1,a2,b1,N,a**2*(1-epsilon+rho),b**2*(1+epsilon+rho))
    print(D,D.shape)
    
    #calculate eigenvalues and eigenvectors
    w, v = LA.eig(D)    
    #specify complex vectors (not sure it is needed)
    #v=np.array(v,dtype = "complex_")
    #order eigenvectors with increasing Re(eigenvalues)
    idx=np.abs(w).argsort()
    
    return w[idx]

#parameters
N=9
a=2.5;b=1;#geometric parameters

#change these two parameters to explore the role of imperfections.
rho=0.01#bending interaction
g=0.0#on site_potential

#Loop over parameters, a/b and epsilon
ratio=np.zeros((1000,100))
eigv=np.zeros((1000,100))
ass=np.linspace(0,5,100)
ess=np.linspace(-3,3,1000)
for ia,a in enumerate(ass):
    for ie,epsilon in enumerate(ess):
    
        a1=-a*b*(1+epsilon-rho)
        a2=-a*b*(1-epsilon-rho)
        b1=a**2*(1-epsilon+rho+g)+b**2*(1+epsilon+rho+g)        
        #construct the dynamical matrix
        DOBC=KL_Dyn_open(a1,a2,b1,N,a**2*(1-epsilon+rho+g),b**2*(1+epsilon+rho+g))
        #diagonalize the dynamical matrix
        wO, vO = LA.eig(DOBC)    
        #order the eigenmodes and compute the end-to-end ratio
        wOs=wO[np.abs(wO).argsort()]
        vOs=vO[:,np.abs(wO).argsort()]
        ratio[ie,ia]=np.abs(vOs[-1,0]/vOs[0,0])
        eigv[ie,ia]=np.abs(wOs[0])/np.abs(wOs[1])

#plot the contour plot
#define colormap
levels = np.arange(-5.0, 5.0, 0.5)
norm = cm.colors.Normalize(vmax=5, vmin=-5)
cmap = cmapcustom

#plot the contour plot 1
fig1=plt.figure(1,figsize=(6,6))
ax1=fig1.add_axes([0.15,0.15,0.8,0.8])
im=ax1.contourf(ass,ess,np.log10(ratio), levels, norm=norm,
                     cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both',aplha=0.5)

#plot expected transition from the theoretical calculation
x=np.linspace(0,5,100)
x1=np.linspace(0,0.999,50)
x2=np.linspace(1.001,5,50)

ax1.fill_between(x1,(x1 - 1)/(1 + x1)-rho*(x1 + 1)/(1 - x1)+g*(x1**2 + 1)/(x1**2 - 1),(x1 + 1)/(-1 + x1)-rho*(x1 - 1)/(1 + x1)+g*(x1**2 + 1)/(x1**2 - 1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)
ax1.fill_between(x2,(x2 - 1)/(1 + x2)-rho*(x2 + 1)/(1 - x2)+g*(x2**2 + 1)/(x2**2 - 1),(x2 + 1)/(-1 + x2)-rho*(x2 - 1)/(1 + x2)+g*(x2**2 + 1)/(x2**2 - 1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)

#plot ticks and labels
ax1.set_ylim(-3,3)
ax1.set_xlim(0,5)
ax1.set_xticks([0,1,2,3,4,5])

ax1.set_ylabel(r'non-reciprocity $\varepsilon$',fontsize=24)
ax1.set_xlabel(r'ratio $a/b$',fontsize=24)

#save
fig1.savefig("Fig8_bending_%.02f_onsite_%.02f_N_%d.pdf" % (rho,g,N))

#plot the contour plot 1
fig2=plt.figure(2,figsize=(6,6))
ax2=fig2.add_axes([0.15,0.15,0.8,0.8])
im2=ax2.contourf(ass,ess,np.log10(eigv))#, levels, norm=norm,
                     #cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both',aplha=0.5)
cbar2=fig2.colorbar(im2, ax=ax2, pad=0.1,shrink=0.8)
cbar2.ax.tick_params(labelsize=10) 

ax2.fill_between(x1,(x1 - 1)/(1 + x1)-rho*(x1 + 1)/(1 - x1)+g*(x1**2 + 1)/(x1**2 - 1),(x1 + 1)/(-1 + x1)-rho*(x1 - 1)/(1 + x1)+g*(x1**2 + 1)/(x1**2 - 1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)
ax2.fill_between(x2,(x2 - 1)/(1 + x2)-rho*(x2 + 1)/(1 - x2)+g*(x2**2 + 1)/(x2**2 - 1),(x2 + 1)/(-1 + x2)-rho*(x2 - 1)/(1 + x2)+g*(x2**2 + 1)/(x2**2 - 1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)

#plot ticks and labels
ax2.set_ylim(-3,3)
ax2.set_xlim(0,5)
ax2.set_xticks([0,1,2,3,4,5])

cbar2.set_label(r'$\log_{10}|eigenvalue|$', rotation=0,size=10)

#save
#fig2.savefig("eigenvalue_bending_%.02f_onsite_%.02f_N_%d.pdf" % (rho,g,N))