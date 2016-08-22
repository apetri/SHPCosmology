import matplotlib
from pylab import *
import numpy
from numpy.fft import fft
from scipy import signal

ion()

N=16384
x=arange(N)


def signl(i):
 if i==1:
  y=50*sin(0.01*x)
  lbl=r'$f(x)=50\sin{(0.01x)}$'
 if i==2:
  y=50*sin(0.01*x)+20*sin(0.02*x)
  lbl=r'$f(x)=50\sin{0.01x}+20\sin{0.02x}$'
 if(i==4):
  y=50*sin(0.01*x)+20*sin(0.02*x)+30*sin(0.05*x)
  lbl=r'$f(x)=50\sin{0.01x}+20\sin{0.02x}+30\sin{0.05x}$'
 if(i==5):
  y=exp(-(x-N/4)**2/(N*1.0/10)**2) 
  lbl=r'$f(x)=e^{-(\frac{x-4000}{1000})^2}$'
 if(i==6):
  y=exp(-(x-N/4)**2/(N*1.0/10)**2)+10*(rand(N)-0.5) 
  lbl=r'$f(x)=e^{-(\frac{x-4000}{1000})^2}+\mathrm{noise}$'
 
 plot(x,y,label=lbl)
 xlabel(r'$x$',fontsize=16)
 ylabel(r'$f(x)$',fontsize=16)
 legend(loc='upper left')
 xlim(0,N/2)
 
 return y

def ft(sig):
 fou=(2.0/N)*abs(fft(sig)[:N/2])
 f=arange(N/2)*(1.0/N)*(2*pi)
 plot(f,fou)
 xlim(0,0.1)
 xlabel(r'$k$',fontsize=16)
 ylabel(r'$\hat{f(k)}$',fontsize=16)
  
 
  
 