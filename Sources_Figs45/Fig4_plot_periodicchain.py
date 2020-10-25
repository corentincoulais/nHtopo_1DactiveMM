# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:01:22 2019

@author: coulais
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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

mpl.rcParams['legend.fontsize']=22;

color1="#F1AD1D"
color2="#22A4B5"

nu=[]
epsilon=[0,0.127]
lambda1=np.zeros((11,2))
lambda2=np.zeros((11,2))
omega=np.zeros((11,2))

for i,filen in enumerate(["k0","kpi"]):
    dat1=np.loadtxt("PeriodicSystem_response/Bulk_"+filen+".txt",skiprows=1,delimiter=",")
    lambda1[:,i]=dat1[:,2]
    lambda2[:,i]=dat1[:,3]
    omega[:,i]=np.abs(dat1[:,4])
    
nu=2/np.pi*(np.arctan(2*omega[:,-1]/(lambda1[:,-1]-lambda2[:,-1]))-np.arctan(2*omega[:,0]/(lambda1[:,0]-lambda2[:,0])))


fig=[[]]*2
ax=[[]]*2
nam=[[]]*2
fig = plt.figure(i,figsize=(10,5))
for i,ix in enumerate([0,10]):
    ax[i] = fig.add_axes([0.12+i*0.47,0.15,0.4,0.8])#[0.12,0.15,0.87,0.8]
    if i ==0: ax[i].set_ylabel(r'$Im(\omega)$ (s$^{-1}$)',fontsize=24)
    ax[i].set_xlabel(r'$Re(\omega)$ (rad/s)',fontsize=24)
    ax[i].plot(omega[ix,:],lambda1[ix,:],c=color2,marker="o",markersize=10)
    ax[i].plot(-omega[ix,:],lambda1[ix,:],c=color1,marker="o",markersize=10)
    
    ax[i].plot(-omega[ix,:],lambda2[ix,:],c=color1,marker="o",markersize=10)
    ax[i].plot(omega[ix,:],lambda2[ix,:],c=color2,marker="o",markersize=10)
    if i ==0:
        ax[i].set_xlim(-60,60)
        ax[i].set_ylim(-65,30)
        ax[i].set_xticks([-50,0,50])
        ax[i].set_yticks([-50,-25,0,25])
    elif i == 1:
        ax[i].set_xlim(-120,120)
        ax[i].set_ylim(-60,60)
        ax[i].set_xticks([-100,0,100])
        ax[i].set_yticks([-50,0,50])

#define plot
fig1 = plt.figure(10,figsize=(8,8))
ax1 = fig1.add_axes([0.15,0.15,0.84,0.8])

ax1.set_ylabel(r'non-Hermitian winding nb $\nu$',fontsize=24)
ax1.set_xlabel(r'non-reciprocal param. $\varepsilon$',fontsize=24)

ax1.vlines(0.12,-0.1,1.1,colors="DeepPink",linestyles="-",lw=3,zorder=0)

dat_th=np.loadtxt("PeriodicSystem_response/winding_xp_number.txt",skiprows=1,delimiter=",")
ax1.plot(dat_th[:,0],nu,ms=20,ls="--",c="k",lw=2,marker="o")

ax1.fill_between([0.12,0.22],[-0.1,-0.1],[1.1,1.1],facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=0)

ax1.set_xlim(-0.02,0.22)
ax1.set_ylim(-0.1,1.1)
ax1.set_yticks([0,1])
ax1.set_xticks([0,0.1,0.2])
ax1.yaxis.set_label_coords(-0.05,0.5)
ax[1].spines['bottom'].set_color('DeepPink')
ax[1].spines['top'].set_color('DeepPink')
ax[1].spines['left'].set_color('DeepPink')
ax[1].spines['right'].set_color('DeepPink')


fig1.savefig("fig4_panelD.pdf")
fig.savefig("fig4_panelBC.pdf")
