import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(a,e0,beta,a0):
   return (e0+(beta*(a-a0)**2))

# Read data: 
adata,efree,toten = np.loadtxt("results.dat",unpack=True, skiprows=1)

# Initial guess:
p0=[-12,30,2.8]

popt,pcov = curve_fit(func,adata,toten,p0)

print "Optimized parameters: ",popt

a_plot = np.linspace(adata[0],adata[-1],50)
toten_fit = popt[0]+popt[1]*(a_plot-popt[2])**2

print(min(toten_fit))

plt.plot(adata,toten,'o')
for i in range(len(adata)):
   plt.annotate(adata[i],xy = [adata[i]-0.02,toten[i]+0.01])
plt.plot(a_plot,toten_fit)
plt.plot(a_plot,min(toten_fit)*np.ones(len(toten_fit)),label = round(min(toten_fit),2))
plt.ylabel("energy [eV]")
plt.xlabel("cell parameter [Angstrom]")
plt.legend()
plt.savefig("fitcurve.png")
plt.savefig("fitcurve.pdf")
plt.show()
