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


mpl.rcParams['legend.fontsize']=22;                                                       
                                                         
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
rho=0#bending interaction
    
#Loop over parameters, a/b and epsilon
ratio=np.zeros((1000,100))
eigv=np.zeros((1000,100))
ass=np.linspace(0,5,100)
ess=np.linspace(-3,3,1000)

Forcing=np.zeros(N)
Forcing[int((N-1)/2)]=1

s=0
for omega in [0.01,10]:
    s+=1
    for ia,a in enumerate(ass):
        for ie,epsilon in enumerate(ess):
        
            a1=-a*b*(1+epsilon-rho)
            a2=-a*b*(1-epsilon-rho)
            b1=a**2*(1-epsilon+rho)+b**2*(1+epsilon+rho)        
            #construct the dynamical matrix
            DOBC=KL_Dyn_open(a1,a2,b1,N,a**2*(1-epsilon+rho),b**2*(1+epsilon+rho))
            #diagonalize the dynamical matrix
            M=DOBC-omega**2*np.diag([1]*N,0)
            vsol=np.linalg.solve(M,Forcing)
            #wO, vO = LA.eig(DOBC)    
            #order the eigenmodes and compute the end-to-end ratio
            #Os=wO[np.abs(wO).argsort()]
            #vOs=vO[:,np.abs(wO).argsort()]
            ratio[ie,ia]=np.abs(vsol[-1]/vsol[0])
            #eigv[ie,ia]=np.abs(wOs[0])
    
    #plot the contour plot
    #define colormap
    levels = np.arange(-5.0, 5.0, 0.5)
    norm = cm.colors.Normalize(vmax=5, vmin=-5)
    cmap = cmapcustom
    
    #plot the contour plot 1
    fig1=plt.figure(s,figsize=(9,8))
    ax1=fig1.add_axes([0.15,0.15,0.8*8/9,0.8])
    im=ax1.contourf(ass,ess,np.log10(ratio), levels, norm=norm,
                         cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both',aplha=0.5)
    #plot colorbar
    cbar=fig1.colorbar(im, ax=ax1, pad=0.1,shrink=0.8)
    cbar.ax.tick_params(labelsize=10) 
    
    #plot expected transition from Ananya's calculation
    x=np.linspace(0,5,100)
    x1=np.linspace(0,0.999,50)
    x2=np.linspace(1.001,5,50)
    
    ax1.fill_between(x1,(x1 - 1)/(1 + x1)-rho*(x1 + 1)/(1 - x1),(x1 + 1)/(-1 + x1)-rho*(x1 - 1)/(1 + x1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)
    ax1.fill_between(x2,(x2 - 1)/(1 + x2)-rho*(x2 + 1)/(1 - x2),(x2 + 1)/(-1 + x2)-rho*(x2 - 1)/(1 + x2),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)
    
    #plot ticks and labels
    ax1.set_ylim(-3,3)
    ax1.set_xlim(0,5)
    ax1.set_ylabel(r'non-reciprocity $\varepsilon$')
    ax1.set_xlabel(r'ratio $a/b$')
    cbar.set_label(r'$\log_{10}|\delta\theta_9/\delta\theta_1|$', rotation=270,size=10)
    
    #save
    fig1.savefig("Fig7_response_frequency_%.02f_N_%d.pdf" % (omega,N))