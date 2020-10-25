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

mpl.rcParams['axes.labelsize'] = 24
mpl.rcParams['xtick.labelsize'] =  24
mpl.rcParams['ytick.labelsize'] = 24
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


dat1=np.loadtxt("OpenSystem_response/1-9_on.txt",skiprows=1)\

    
#define plot
fig1 = plt.figure(10,figsize=(10,5))
ax1 = fig1.add_axes([0.12,0.15,0.87,0.8])
ax1.set_ylabel(r'ang. disp. field $\delta\theta$ (rad)',fontsize=24)
ax1.set_xlabel(r'site $n$',fontsize=24)


ii=[0,1]

for i,c in zip(ii,["gray"]+["DeepPink"]):
    #ax1.plot(range(1,len(dat1[i,1:])+1),dat1[i,1:]+6-i,c=mpl.cm.jet(i/6),lw=5,marker="o",markersize=10)
    ax1.plot(range(1,len(dat1[i,3:])+1),np.flipud(dat1[i,3:])+(6-i)*0,c=c,lw=5,marker="o",markersize=10)
    #ax1.annotate(r"$\varepsilon=%0.2f$" % dat1[i,2],xy=(9.2,dat1[i,3]),xytext=(0,10),color=c,horizontalalignment='right', verticalalignment='bottom',size=15)

ax1.set_xlim(0.5,9.5)
ax1.set_ylim(0,0.07)
ax1.set_yticks([0,0.03,0.06])
ax1.set_xticks([1,2,3,4,5,6,7,8,9])
fig1.savefig("fig4_panelF.pdf")

#define plot
fig2 = plt.figure(2,figsize=(8,8))
ax2 = fig2.add_axes([0.15,0.15,0.84,0.8])
ax2.set_ylabel(r'Ampl. fact. $\delta\theta_{9}/\delta\theta_{1}$',fontsize=24)
ax2.set_xlabel(r"non-reciprocal param. $\varepsilon$",fontsize=24)
#plot the energies

fact=1#0.0092#0.02

lim1=0.12*fact
lim3=.2*fact
#ax1.axvspan(0, 0.16, facecolor=color1, alpha=0.1,linewidth=0)
#ax2.axvspan(0, lim1, facecolor="LightGray",alpha=0.5,linewidth=0)
#ax2.axvspan(lim1, lim2, facecolor="DeepPink",alpha=0.5,linewidth=0)
#ax2.axvspan(lim2, lim3, facecolor="DeepPink",alpha=0.5,linewidth=0)

ax2.hlines(1,-0.02,0.22,colors="k",linestyles="-",lw=1,zorder=0)
ax2.vlines(0.12,10**(-1-0.2),10**(1+0.2),colors="DeepPink",linestyles="-",lw=3,zorder=0)

cmapcustom = LinearSegmentedColormap.from_list('mycmap', ['#DCE11F', 'white', '#6DBF51'])

#ax2.plot(dat1[:10,2]*fact,dat1[:10,3]/dat1[:10,-1],c='k',lw=5,marker="+",markersize=15,markeredgewidth=6,ls="none")

datc=(np.log10(dat1[:10,3]/dat1[:10,-1])+1)/2
datc2=np.log10(dat1[:10,3]/dat1[:10,-1])
                                                          
ax2.scatter(dat1[:10,2]*fact,dat1[:10,3]/dat1[:10,-1],s=400,c=cmapcustom(datc),edgecolors="k",linewidths=1,vmin=datc.min(), vmax=datc.max())#,marker="+")#,markeredgewidth=6,ls="none")
ax2.fill_between([0.12,0.22],[10**(-1-0.2),10**(-1-0.2)],[10**(1+0.2),10**(1+0.2)],facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=0)

#ax2.plot([0,0.3],[1,1])
ax2.set_yscale("log")
ax2.set_ylim(10**(-1-0.2),10**(1+0.2))
ax2.set_xlim(-0.02,0.22)
ax2.set_yticks([0.1,1,10])
ax2.set_xticks([0,0.1,0.2])
ax2.yaxis.set_label_coords(-0.11,0.5)

#ax1.yaxis.set_label_coords(-0.17,0.5)
fig2.savefig("fig4_panelG.pdf")


fig11 = plt.figure(11,figsize=(8,8))
ax11 = fig11.add_axes([0.15,0.15,0.8,0.8])
fig21 = plt.figure(21,figsize=(2,8))
ax21 = fig21.add_axes([-0.3,0.15,0.8,0.8])
ax21.set_axis_off()

x=np.linspace(0,5,1000)
y=np.linspace(-3,3,1000)
xx,yy=np.meshgrid(x,y)
ratio=(xx*(1-yy)/(1+yy))**8
levels = np.linspace(-1, 1, 5)

#orm = cm.colors.Normalize(vmax=1, vmin=-1)
norm = cm.colors.Normalize(vmax=datc2.max(), vmin=datc2.min())
cmap = cmapcustom

mpl.rcParams['ytick.direction']="out"
mpl.rcParams['xtick.direction']="out"
im=ax11.contourf(xx,yy,np.log10(ratio), levels, norm=norm,
                     cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both',alpha=1)
fig21.colorbar(im, ax=ax21)
fig21.savefig("fig4_panelG_colormap.pdf")
