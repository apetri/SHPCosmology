#!/usr/bin/env python

import matplotlib
from pylab import *
import numpy

prefix='model'
suffix='_scalCls.dat'
experimental='exp_power.txt'

l=loadtxt(prefix+'1'+suffix)[:,0]
pow=numpy.zeros([len(l),3])

exp_l=loadtxt(experimental)[:,0]
exp_pow=loadtxt(experimental)[:,1]
exp_err=loadtxt(experimental)[:,2]

ion()

for i in [1,2,3]:
 pow[:,i-1]=loadtxt(prefix+'%d'%(i)+suffix)[:,1]

fig=figure()
ax=fig.add_subplot(1,1,1)
ax.set_xscale('log')
xlim(2,800)
ylim(0,8000)
xlabel(r'$l\sim 180^\circ/\theta$',fontsize=16)
ylabel(r'$l(l+1)C_l/2\pi[\mu\mathrm{K}^2]$',fontsize=16)
inp = raw_input('-->')
errorbar(exp_l,exp_pow,yerr=exp_err,marker='.',linestyle='none',color='grey',label='Measured')
legend(loc='upper left')
inp = raw_input('-->')
plot(l,pow[:,2],color='green',label=r'$\Omega_b=0.05 \Omega_m=0.5 \Omega_\Lambda=0.7$')
legend(loc='upper left')
inp = raw_input('-->')
plot(l,pow[:,1],color='blue',label=r'$\Omega_b=0.05 \Omega_m=0.25 \Omega_\Lambda=0$')
legend(loc='upper left')
inp = raw_input('-->')
plot(l,pow[:,0],color='red',label=r'$\Omega_b=0.0449 \Omega_m=0.222 \Omega_\Lambda=0.734$')
legend(loc='upper left')
inp = raw_input('-->')




