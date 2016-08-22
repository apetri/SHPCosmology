import matplotlib
from pylab import *
import healpy
import numpy
import scipy
from scipy.special import *

ion()

Nside=64
Npix=12*(Nside**2)

def mode(l,m):
 map=numpy.zeros(Npix)+1.0
 for i in range(0,Npix): 
  print(i)
  theta,phi=healpy.pixelfunc.pix2ang(Nside,i)
  map[i]=abs(sph_harm(m,l,theta,phi)+((-1)**m)*sph_harm(-m,l,theta,phi))
 
 tit=r'$(l,m)=(%d,%d)$'%(l,m)
 healpy.mollview(map,title=tit)
 savefig('(%d,%d).png'%(l,m))
 
 return
 
def contr(l,m,theta,phi):
 res=abs(sph_harm(m,l,theta,phi)+((-1)**m)*sph_harm(-m,l,theta,phi))
 return res
 

def add():
 map=numpy.zeros(Npix)+1.0
 for i in range(0,Npix): 
  print(i)
  theta,phi=healpy.pixelfunc.pix2ang(Nside,i)
  map[i]=contr(2,0,theta,phi)+2*contr(10,7,theta,phi)+1.5*contr(100,50,theta,phi)
 
 return map
 