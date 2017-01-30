import matplotlib.pyplot as plt
import numpy  as np
import h5py
import matplotlib.gridspec as gridspec
from matplotlib.ticker import NullFormatter
import matplotlib
params = {
    'figure.figsize'    : [9, 5.4],
    'text.usetex'       : True,
    'xtick.major.size'  : 10,
    'xtick.minor.size'  : 5,
    'ytick.major.size'  : 10,
    'ytick.minor.size'  : 5,
}
matplotlib.rcParams.update(params)
nullfmt   = NullFormatter()
itr2ctu=0.010909090909090894
ctu2ms=0.0049267398258
ctu2dens=6.172716354369236e+17
tmerg=270336


def get_data(rl,itr):
  x=np.loadtxt("data/xz/x"+str(rl)+"."+str(d)+".xz.dat")
  y=np.loadtxt("data/xz/y"+str(rl)+"."+str(d)+".xz.dat")
  rho=np.loadtxt("data/xz/rho"+str(rl)+"."+str(d)+".xz.dat")
  rho=np.log10(rho)
  return x,y,rho



itrList=[272384,308224,456704]
fig =plt.figure(0)
gs = gridspec.GridSpec(1, 3, width_ratios=[1,1,1], wspace=0.00, hspace=0.00)
ax=[ plt.subplot(gs[0]), plt.subplot(gs[1]), plt.subplot(gs[2])]

cbar_list=[]
for i,d in enumerate(itrList):
    
  time=(int(d)-tmerg)*itr2ctu*ctu2ms
  
  x5,y5,r5=get_data(5,d)
  x4,y4,r4=get_data(4,d)
  x3,y3,r3=get_data(3,d)
  x2,y2,r2=get_data(2,d)
  print d

  
  cmap_max=15.0
  cmap_min=5.0
  ax[i].pcolormesh(x2,y2,r2,shading='gouraud',vmin=cmap_min,vmax=cmap_max,rasterized=True) 
  ax[i].pcolormesh(x3,y3,r3,shading='gouraud',vmin=cmap_min,vmax=cmap_max,rasterized=True) 
  ax[i].pcolormesh(x4,y4,r4,shading='gouraud',vmin=cmap_min,vmax=cmap_max,rasterized=True) 
  cbar=ax[i].pcolormesh(x5,y5,r5,shading='gouraud',vmin=cmap_min,vmax=cmap_max,rasterized=True) 
  ax[i].axis([-80,80,0,120])
  ax[i].minorticks_on()
  ax[i].tick_params(length=6, width=0.8, which='major')
  ax[i].tick_params(length=3, width=0.3, which='minor')
  ax[i].set_xticks([-60,-30,0,30,60])
  ax[i].set_xticklabels(["$-60$","$-30$","$0$","$30$","$60$"])
  ax[i].set_yticks([0,30,60,90,120])
  ax[i].set_yticklabels(["$0$","$30$","$60$","$90$","$120$"])
  ax[i].xaxis.set_tick_params(color='black', which='both')
  ax[i].yaxis.set_tick_params(color='black', which='both')
  ax[i].set_aspect('equal')


  if i==0:
    ax[i].annotate(r'$\mathbf{t = %6.2f\ [\mathbf{ms}]}$' % (time),xy=(10,100), color='white',size=8) 
  else: 
    ax[i].annotate(r'$\mathbf{t = %6.2f\ [\mathbf{ms}]}$' % (time),xy=(10,100), color='white',size=8) 




ax[1].yaxis.set_major_formatter(nullfmt)
ax[2].yaxis.set_major_formatter(nullfmt)
#
ax[0].set_ylabel(r'$z  \,\rm [km]$')
ax[0].set_xlabel(r'$x  \,\rm [km]$')
ax[1].set_xlabel(r'$x  \,\rm [km]$')
ax[2].set_xlabel(r'$x  \,\rm [km]$')
#
#
cb=fig.colorbar(cbar,ax=ax[0:3],ticks=[5.0,7.0,9.0,11.0,13.0,15.0],shrink=0.33,pad=0.02,aspect=20)
cb.ax.tick_params(labelsize=8)
cb.set_label(r"$\log \rho \,\rm [g/cm^{3}]$") #+ str(time) + "ms",size=10)
saveFig="rho_xz.pdf"
plt.savefig(saveFig,bbox_inches="tight",pad_inches=0.05,format="pdf")

