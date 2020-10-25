# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:01:22 2019

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
mpl.rcParams['lines.linewidth']=5
mpl.rcParams['axes.linewidth']= 2
mpl.rcParams['xtick.major.size']= 10
mpl.rcParams['xtick.major.width']=2
mpl.rcParams['xtick.major.pad']=8
mpl.rcParams['ytick.major.pad']=8
mpl.rcParams['ytick.major.size']= 10
mpl.rcParams['ytick.major.width']=2
mpl.rcParams['xtick.minor.size']= 0#7.5
mpl.rcParams['xtick.minor.width']=0
mpl.rcParams['ytick.minor.size']= 0#7.5
mpl.rcParams['ytick.minor.width']=0
#mpl.rcParams['text.usetex'] = True
#mpl.rcParams['font.sans-serif'] = 'helvet'



#mpl.rcParams['text.latex.preamble'] = [
#       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
#       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
#       r'\usepackage{sfmath}',
#       r'\usepackage{helvet}',    # set the normal font here
#       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
#       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
#]  



cmapcustom = LinearSegmentedColormap.from_list('mycmap', ['Pink', 'white', 'LightGray'])
cmapcustom2 = LinearSegmentedColormap.from_list('mycmap', ['LightGray','white', 'Pink'])
cmapcustom = LinearSegmentedColormap.from_list('mycmap', ['moccasin', 'white', 'LightSkyBlue'])
cmapcustom = LinearSegmentedColormap.from_list('mycmap', ['#DCE11F', 'white', '#6DBF51'])

#fig, ax = plt.subplots()
#im = ax.imshow(np.random.random((10, 10)), cmap=cmap, interpolation='nearest')
#fig.colorbar(im)
#plt.show()

mpl.rcParams['legend.fontsize']=22;

path="/Users/coulais/Dropbox/Non-Hermitian TI/Figures_for_manuscript/Sources_figure3/"

x=np.linspace(0,5,100)
x1=np.linspace(0,0.999,50)
x2=np.linspace(1.001,5,50)
#define plot
fig1 = plt.figure(1,figsize=(8,8))
ax1 = fig1.add_axes([0.15,0.15,0.8,0.8])
fig2 = plt.figure(2,figsize=(2,8))
ax2 = fig2.add_axes([-0.2,0.15,0.8,0.8])
ax2.set_axis_off()
ax1.set_ylabel(r'non-reciprocity $\varepsilon$')
ax1.set_xlabel(r'ratio $a/b$')

#plot the displacement field
#ax1.fill_between(x1,(x1 - 1)/(1 + x1),3,color="LightGray",alpha=0.5)
#ax1.fill_between(x1,-3,(x1 + 1)/(-1 + x1),color="LightGray",alpha=0.5)
#ax1.fill_between(x2,-3,(x2 - 1)/(1 + x2),color="LightGray",alpha=0.5)
#ax1.fill_between(x2,(x2 + 1)/(-1 + x2),3,color="LightGray",alpha=0.5)


y=np.linspace(-3,3,1000)
xx,yy=np.meshgrid(x,y)
ratio=(xx*(1-yy)/(1+yy))**8
levels = np.arange(-5.0, 5.0, 0.5)

norm = cm.colors.Normalize(vmax=5, vmin=-5)
cmap = cmapcustom

im=ax1.contourf(xx,yy,np.log10(ratio), levels, norm=norm,
                     cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both',aplha=0.5)

"""
y=np.linspace(-3,3,1000)
xx,yy=np.meshgrid(x1,y)
ratio=(xx*(1-yy)/(1+yy))**8
levels = np.arange(-5.0, 5.0, 0.5)

norm = cm.colors.Normalize(vmax=5, vmin=-5)
cmap = cmapcustom2

im2=ax1.contourf(xx,yy,np.log10(ratio), levels, norm=norm,
                     cmap=cm.get_cmap(cmap, len(levels) - 1),extend='both')


"""
fig2.colorbar(im, ax=ax2)
plt.show()


ax1.fill_between(x1,(x1 - 1)/(1 + x1),(x1 + 1)/(-1 + x1),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)
ax1.fill_between(x2,(x2 - 1)/(1 + x2),(x2 + 1)/(-1 + x2),facecolor="none",edgecolor="DeepPink",alpha=1,hatch="/",zorder=20)


xs=2.5/1
ax1.scatter(xs,0.,marker="v",c="None",s=150,linewidths=4,edgecolors="Gray")#,size=10,color="k")
ax1.scatter(xs,0.90,marker="d",c="None",s=150,linewidths=4,edgecolors="DeepPink")#,size=10,color="k")
ax1.scatter(xs,1.80,marker="s",c="None",s=150,linewidths=4,edgecolors="DeepPink")#,size=10,color="k")
ax1.scatter(xs,2.7,marker="^",c="None",s=150,linewidths=4,edgecolors="Gray")#,size=10,color="k")

ax1.plot(x,(x**2 - 1)/(1 + x**2),"Blue",lw=1.5,ls="--",zorder=21)
ax1.plot(x1,(x1**2 + 1)/(-1 + x1**2),"Blue",lw=1.5,ls="--",zorder=21)
ax1.plot(x2,(x2**2 + 1)/(-1 + x2**2),"Blue",lw=1.5,ls="--",zorder=21)

ax1.plot(x,(x - 1)/(1 + x),"DeepPink",lw=3)
ax1.plot(x1,(x1 + 1)/(-1 + x1),"DeepPink",lw=3)
ax1.plot(x2,(x2 + 1)/(-1 + x2),"DeepPink",lw=3)
ax1.plot([1,1],[-3,3],"DeepPink",lw=3)
ax1.plot([1,1],[-3,3],"Blue",lw=1.5,ls="--",zorder=21)
#ax1.set_xscale("log")
ax1.set_ylim(-3,3)
#ax1.set_xlim(1e-1,1e1)
ax1.set_xlim(0,5)
fig1.savefig(path+"/figa_panelA_v4.pdf")
fig2.savefig(path+"/figa_panelA_v4_colormap.pdf")