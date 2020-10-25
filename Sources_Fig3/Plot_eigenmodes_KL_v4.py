# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:15:45 2019

@author: coulais
"""
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import pandas as pd
import operator
from functools import reduce 

path="/Users/coulais/Dropbox/Non-Hermitian TI/Figures_for_manuscript/Sources_figure3/"

def SSHHamiltonian(a1,a2,b1,b2,N):
    return np.diag([a1,b2]*N+[a1],1)+np.diag([a2,b1]*N+[a2],-1)
def complexdot(a,b):
    return np.real(a).dot(np.real(b)) -  np.imag(a).dot(np.imag(b)) + 1j*(np.real(a).dot(np.imag(b)) +  np.real(b).dot(np.imag(a)))

    
def KLeigenvectors(N,c1,c2,alpha):
    #define hamiltonian
    psiL=np.array([(c1/c2)**i for i in range(0,N,1)])
    psiR=np.array([(c1/c2*(1-alpha)/(1+alpha))**i for i in range(0,N,1)])
    return psiR,psiL
    
def plotKLchain(ax1,psi,theta,r,N,color="LightGray",sign=1):
    for i in range(N):
        #ang=psi[i]*180/np.pi*(sign)**i#/np.pi*2
        ang=psi[i]*45*(sign)**i#/np.pi*2
        th=(-1)**i*(90-theta*180/np.pi)
        #for x1,y1,r,t1,t2 in zip(x, y, radii, theta1, theta2):
        wedge = Wedge((i,0), r, th-ang, th+ang,fc=color,alpha=1,ec=color,zorder=i)
        ax1.add_artist(wedge)
    
    for i in range(N):
       ax1.plot([i,i+r*np.sin(theta)],[0,(-1)**i*r*np.cos(theta)],ls="-",lw=2,color="k",zorder=i+10)
    
    xsprings=[i+r*np.sin(theta) for i in range(N)]
    ysprings=[(-1)**i*r*np.cos(theta)for i in range(N)]
    ax1.plot(xsprings,ysprings,ls="--",lw=2,color="k",zorder=20)
    ax1.scatter(xsprings,ysprings,marker="o",c="k",s=200,linewidths=4,edgecolors="k",zorder=21)#,size=10,color="k")

#Parameters
N=9#Length of the chain / 2 -1
c1=2.5#geometrical parameter 1
c2=1#geometrical parameter 2  
L=(N*2-1)# Real length of the chain
r=1#0.18/0.6*2
theta=0.22#15*np.pi/180

######
alpha=0.#non-reciprocal parameter 
###
fig1=plt.figure(1,figsize=(10,4))
ax1=fig1.add_axes([0.,0.,1,1])

#psiR1,psiR2, psiL1,psiL2 = SSHeigenvectors(N,c1,c2,alpha)
psiR,psiL=KLeigenvectors(N,c1,c2,alpha)
ixm=np.abs(psiR).argmax()
#ax1.plot(range(1,N+1),psiR/psiR[ixm],c="Gray")
#ixm=np.abs(psiL).argmax()
#ax1.plot(range(1,N+1),psiL/psiL[ixm],c="Gray")

xs=N-1
ys=0.9

plotKLchain(ax1,psiR/psiR[ixm],theta,r,N,color="Gray")

ax1.set_ylim(-2,2)
ax1.set_xlim(-1,N)
ax1.set_axis_off()

fig1.savefig(path+ "/figb_psiR_panel_alpha_0_KL_v4.pdf")


######
alpha=0.9#non-reciprocal parameter 
###
fig2=plt.figure(2,figsize=(10,4))
ax2=fig2.add_axes([0.,0.,1,1])


psiR,psiL=KLeigenvectors(N,c1,c2,alpha)
ixm=np.abs(psiR).argmax()
#ax2.plot(range(1,N+1),psiR/psiR[ixm],c="DeepPink")
#ixm=np.abs(psiL).argmax()
#ax2.plot(range(1,N+1),psiL/psiL[ixm],c="DeepPink")
#ax2.scatter(xs,ys,marker="d",c="None",s=150,linewidths=4,edgecolors="DeepPink")#,size=10,color="k")

plotKLchain(ax2,psiR/psiR[ixm],theta,r,N,color="DeepPink")


ax2.set_ylim(-2,2)
ax2.set_xlim(-1,N)
ax2.set_axis_off()


fig2.savefig(path+ "/figb_psiR_panel_alpha_0p8_KL_v4.pdf")

######
alpha=1.8#non-reciprocal parameter 
###
fig3=plt.figure(3,figsize=(10,4))
ax3=fig3.add_axes([0.,0.,1,1])

psiR,psiL=KLeigenvectors(N,c1,c2,alpha)
ixm=np.abs(psiR).argmax()

plotKLchain(ax3,psiR/psiR[ixm],theta,r,N,color="DeepPink",sign=-1)


ax3.set_ylim(-2,2)
ax3.set_xlim(-1,N)
ax3.set_axis_off()

fig3.savefig(path+ "/figb_psiR_panel_alpha_1p6_KL_v4.pdf")


######
alpha=2.7#non-reciprocal parameter 
###
fig4=plt.figure(4,figsize=(10,4))
ax4=fig4.add_axes([0.,0.,1,1])

psiR,psiL=KLeigenvectors(N,c1,c2,alpha)
ixm=np.abs(psiR).argmax()
#ax4.plot(range(1,N+1),psiR/psiR[ixm],c="Gray")
#ixm=np.abs(psiL).argmax()
#ax4.plot(range(1,N+1),psiL/psiL[ixm],c="Gray")

#ax4.scatter(xs,ys,marker="^",c="None",s=150,linewidths=4,edgecolors="Black")#,size=10,color="k")


#ax4.set_ylabel(r'eigenmode',fontsize=24)
#ax4.set_xlabel(r'site $n$',fontsize=24)

#ax4.set_ylim(-1.25,1.25)
#ax4.set_xlim(0.5,N+0.5)

plotKLchain(ax4,psiR/psiR[ixm],theta,r,N,color="Gray",sign=-1)


ax4.set_ylim(-2,2)
ax4.set_xlim(-1,N)
ax4.set_axis_off()


fig4.savefig(path+ "/figb_psiR_panel_alpha_2p4_KL_v4.pdf")