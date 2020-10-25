# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:01:22 2019

@author: coulais
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection

'''
mpl.rcParams['axes.labelsize'] = 42
mpl.rcParams['xtick.labelsize'] =  42
mpl.rcParams['ytick.labelsize'] = 42
mpl.rcParams['figure.subplot.left'] = 0.25
mpl.rcParams['figure.subplot.right'] = 0.95
mpl.rcParams['figure.subplot.bottom'] = 0.15
mpl.rcParams['figure.subplot.top'] = 0.95
#mpl.rcParams['figure.figsize']=[ 8,8]
#mpl.rcParams['font.family']='Times'
mpl.rcParams['lines.linewidth']=1
mpl.rcParams['axes.linewidth']= 3
mpl.rcParams['xtick.major.size']= 15
mpl.rcParams['xtick.major.width']=3
mpl.rcParams['xtick.major.pad']=8
mpl.rcParams['ytick.major.pad']=8
mpl.rcParams['ytick.major.size']= 15
mpl.rcParams['ytick.major.width']=3
mpl.rcParams['xtick.minor.size']= 0#7.5
mpl.rcParams['xtick.minor.width']=0
mpl.rcParams['ytick.minor.size']= 0#7.5
'''
mpl.rcParams['axes.linewidth']= 1
mpl.rcParams['xtick.major.width']=1
mpl.rcParams['ytick.major.width']=1
mpl.rcParams['xtick.minor.width']=1
#mpl.rcParams['ztick.major.width']=3


#mpl.rcParams['ytick.minor.width']=0
mpl.rcParams['text.usetex'] = True 
mpl.rcParams['font.sans-serif'] = 'helvet'
mpl.rcParams['grid.linewidth']=0.5
 
mpl.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{sfmath}',
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]  


mpl.rcParams['legend.fontsize']=22;


color1="darkmagenta"
color2="limegreen"

path="/Users/coulais/Dropbox/Non-Hermitian TI/Figures_for_manuscript/Sources_figure2/"
stop=200
stop1=100;stop2=301
off=1.5
ls="-"
zoff=2*np.pi*1.5
for case,panel in zip(["1","2","3","4","5","6"],["A","B","C","D","E","F"]):

    #dat1=np.loadtxt(path+"2d_para_"+case+".txt",delimiter=",")
    dat1=np.loadtxt(path+"eigenfrequencies_"+case+"_v3.txt",delimiter=",")
    
    #define plot
    fig1 = plt.figure(1,figsize=(6,6))
    #ax1 = fig1.add_axes([0.25,0.25,0.7,0.7])
    ax1 = fig1.add_axes([0.15,0.05,0.8,0.9], projection='3d')
    ax1.xaxis._axinfo["grid"]['linewidth'] = 1.
    ax1.yaxis._axinfo["grid"]['linewidth'] = 1.
    ax1.zaxis._axinfo["grid"]['linewidth'] = 1.
    
    ax1.set_ylabel(r'$Im(E)$',fontsize=24, labelpad=10)
    ax1.set_xlabel(r'$Re(E)$',fontsize=24, labelpad=10)
    ax1.set_zlabel(r'$k$',fontsize=24)
    
    #ax1.set_ylabel(r'$Im(\omega)$')
    #ax1.set_xlabel(r'$Re(\omega)$')
    #plot the energies
    if case in ["1","2","3","4","5"]:

        ax1.plot(dat1[:stop,2],dat1[:stop,3],dat1[:stop,-1],c=color2,lw=5,ls=ls)
        ax1.plot(dat1[stop:,2],dat1[stop:,3],dat1[stop:,-1],c=color2,lw=5,ls=ls)
        d1=ax1.plot(dat1[:stop,0],dat1[:stop,1],dat1[:stop,-1],c=color1,lw=5,ls=ls)
        d2=ax1.plot(dat1[stop:,0],dat1[stop:,1],dat1[stop:,-1],c=color1,lw=5,ls=ls)
        
        d1=ax1.plot(dat1[:stop,0],dat1[:stop,1],zoff,zdir='z',c=color1,lw=5,ls=ls)
        d2=ax1.plot(dat1[stop:,0],dat1[stop:,1],zoff,zdir='z',c=color1,lw=5,ls=ls)
        ax1.plot(dat1[:stop,2],dat1[:stop,3],zoff,zdir='z',c=color2,lw=5,ls=ls)
        ax1.plot(dat1[stop:,2],dat1[stop:,3],zoff,zdir='z',c=color2,lw=5,ls=ls)
                
    elif case in ["6"]:
        
        x=np.hstack((dat1[:stop1,0],dat1[stop1:stop1+1,2]))
        y=np.hstack((dat1[:stop1,1],dat1[stop1:stop1+1,3]))
        z=np.hstack((dat1[:stop1,-1],dat1[stop1:stop1+1,-1]))        
        
        #ax1.plot(dat1[:stop1,0],dat1[:stop1,1],dat1[:stop1,-1],c=color1,lw=5,ls=ls,zorder=2)
        ax1.plot(x,y,z,c=color1,lw=5,ls=ls,zorder=2)
        ax1.plot(dat1[stop1:stop,0],dat1[stop1:stop,1],dat1[stop1:stop,-1],c=color1,lw=5,ls=ls,zorder=2)
        
        x=np.hstack((dat1[stop:stop2,0],dat1[stop2:stop2+1,2]))
        y=np.hstack((dat1[stop:stop2,1],dat1[stop2:stop2+1,3]))
        z=np.hstack((dat1[stop:stop2,-1],dat1[stop2:stop2+1,-1]))  
        
        #ax1.plot(dat1[stop:stop2,0],dat1[stop:stop2,1],dat1[stop:stop2,-1],c=color1,lw=5,ls=ls)
        ax1.plot(x,y,z,c=color1,lw=5,ls=ls)
        ax1.plot(dat1[stop2:,0],dat1[stop2:,1],dat1[stop2:,-1],c=color1,lw=5,ls=ls,zorder=4)       
        
        ax1.plot(dat1[:stop1,0],dat1[:stop1,1],zoff,c=color1,lw=5,ls=ls)
        ax1.plot(dat1[stop1:stop,0],dat1[stop1:stop,1],zoff,c=color1,lw=5,ls=ls)
        ax1.plot(dat1[stop:stop2,0],dat1[stop:stop2,1],zoff,c=color1,lw=5,ls=ls)
        ax1.plot(dat1[stop2:,0],dat1[stop2:,1],zoff,c=color1,lw=5,ls=ls)    
        
        x=np.hstack((dat1[:stop1,0],dat1[stop1:stop,2],dat1[stop:stop2,0],dat1[stop2:,2]))
        y=np.hstack((dat1[:stop1,1],dat1[stop1:stop,3],dat1[stop:stop2,1],dat1[stop2:,3]))
        z=np.hstack((dat1[:stop1,-1],dat1[stop1:stop,-1],dat1[stop:stop2,-1],dat1[stop2:,-1]))
        #ax1.plot(x,y,z,c=color1,lw=5,ls=ls)  
        
        ax1.plot(x,y,zoff,zdir="off",c=color1,lw=5,ls=ls)
        
        x=np.hstack((dat1[:stop1,2],dat1[stop1:stop1+1,0]))
        y=np.hstack((dat1[:stop1,3],dat1[stop1:stop1+1,1]))
        z=np.hstack((dat1[:stop1,-1],dat1[stop1:stop1+1,-1]))    
        
        #ax1.plot(dat1[:stop1,2],dat1[:stop1,3],dat1[:stop1,-1],c=color2,lw=5,ls=ls,zorder=1)
        ax1.plot(x,y,z,c=color2,lw=5,ls=ls,zorder=1)
        ax1.plot(dat1[stop1:stop,2],dat1[stop1:stop,3],dat1[stop1:stop,-1],c=color2,lw=5,ls=ls,zorder=3)

        x=np.hstack((dat1[stop:stop2,2],dat1[stop2:stop2+1,0]))
        y=np.hstack((dat1[stop:stop2,3],dat1[stop2:stop2+1,1]))
        z=np.hstack((dat1[stop:stop2,-1],dat1[stop2:stop2+1,-1]))          
        
        #ax1.plot(dat1[stop:stop2,2],dat1[stop:stop2,3],dat1[stop:stop2,-1],c=color2,lw=5,ls=ls,zorder=3)
        ax1.plot(x,y,z,c=color2,lw=5,ls=ls,zorder=3)
        
        ax1.plot(dat1[stop2:,2],dat1[stop2:,3],dat1[stop2:,-1],c=color2,lw=5,ls=ls,zorder=1)
        
        ax1.plot(dat1[:stop1,2],dat1[:stop1,3],zoff,c=color2,lw=5,ls=ls)
        ax1.plot(dat1[stop1:stop,2],dat1[stop1:stop,3],zoff,c=color2,lw=5,ls=ls)
        ax1.plot(dat1[stop:stop2,2],dat1[stop:stop2,3],zoff,c=color2,lw=5,ls=ls)
        ax1.plot(dat1[stop2:,2],dat1[stop2:,3],zoff,c=color2,lw=5,ls=ls)
        
        x=np.hstack((dat1[:stop1,2],dat1[stop1:stop,0],dat1[stop:stop2,2],dat1[stop2:,2]))
        y=np.hstack((dat1[:stop1,3],dat1[stop1:stop,1],dat1[stop:stop2,3],dat1[stop2:,1]))
        z=np.hstack((dat1[:stop1,-1],dat1[stop1:stop,-1],dat1[stop:stop2,-1],dat1[stop2:,-1]))
        #ax1.plot(x,y,z,c=color2,lw=5,ls=ls) 

        #ax1.plot(x,y,zoff,zdir="off",c=color2,lw=5,ls=ls)
        
        #d1=ax1.plot(dat1[:stop1,0],dat1[:stop1,1],zoff,zdir='z',c=color1,lw=5,ls=ls)
        #ax1.plot(dat1[stop1:stop,0],dat1[stop1:stop,1],zoff,zdir='z',c=color2,lw=5,ls=ls)
        #d2=ax1.plot(dat1[stop:stop2,0],dat1[stop:stop2,1],zoff,zdir='z',c=color1,lw=5,ls=ls)
        #ax1.plot(dat1[stop2:,0],dat1[stop2:,1],zoff,zdir='z',c=color2,lw=5,ls=ls)
        #ax1.plot(dat1[:stop1,2],dat1[:stop1,3],zoff,zdir='z',c=color2,lw=5,ls=ls)
        #d1=ax1.plot(dat1[stop1:stop,2],dat1[stop1:stop,3],zoff,zdir='z',c=color1,lw=5,ls=ls)
        #ax1.plot(dat1[stop:stop2,2],dat1[stop:stop2,3],zoff,zdir='z',c=color2,lw=5,ls=ls)
        #d2=ax1.plot(dat1[stop2:,2],dat1[stop2:,3],zoff,zdir='z',c=color1,lw=5,ls=ls)

    ax1.set_ylim(-np.pi*1.2,np.pi*1.2)
    ax1.set_xlim(-np.pi*1.2,np.pi*1.2)
    ax1.set_yticks([-np.pi,0,np.pi])
    ax1.set_xticks([-np.pi,0,np.pi])
    ax1.set_yticklabels([r'$-\pi$',r'$0$',r'$\pi$'],fontsize=24,
                                       fontdict= {'fontsize': mpl.rcParams['axes.titlesize'], 
                                        'fontweight': mpl.rcParams['axes.titleweight'],
                                        'verticalalignment': 'baseline','horizontalalignment': "center"})
    ax1.set_xticklabels([r'$-\pi$',r'$0$',r'$\pi$'],fontsize=24,
                                       fontdict= {'fontsize': mpl.rcParams['axes.titlesize'], 
                                        'fontweight': mpl.rcParams['axes.titleweight'],
                                        'verticalalignment': 'baseline','horizontalalignment': "center"})
    
    ax1.set_zlim(-2*np.pi,2*np.pi)
    ax1.set_zticks([-2*np.pi,0,2*np.pi])
    ax1.set_zticklabels([r'$-2\pi$',0,r'$2\pi$'],fontsize=24)
    
    #if case =="6":
    #    gfdsffs
    fig1.savefig(path+"/fig2_panel"+panel+"_v5.pdf")
    plt.close("all")