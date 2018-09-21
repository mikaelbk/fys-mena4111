from numpy import *
from matplotlib.pyplot import *

#importing results
file = open("results.txt", "r")
lines = file.readlines()
file.close()
for i in range(len(lines)):
    lines[i] = lines[i].split()
lines = array(lines)

#declaring variable arrays
MxForce = lines[1:,0].astype(float)
Drift = lines[1:,1].astype(float)
Press = lines[1:,2].astype(float)
TOTEN = lines[1:,3].astype(float)
Filename = lines[1:,4]
cutOff = linspace(400,850,(850-400)/50+1)

#importing bandgaps
file = open("bandgaps.txt","r")
lines = file.readlines()
file.close
for i in range(len(lines)):
    lines[i] = lines[i].split()
lines = array(lines)

#declaring bandgap array
BandGap = lines[1:,0].astype(float)
print(BandGap)

#writing differences in total energies from one cut off to the next to file
totEnDiff = open("totEnergyDifference.txt", "w")
for i in range(len(TOTEN)-1):
    totEnDiff.write(str((TOTEN[i+1]-TOTEN[i])*1e3) + " ")
totEnDiff.close()

#plotting
figure()
subplot(2,2,1)
plot(TOTEN[1:]-TOTEN[:-1],'-o')
plot(3e-3*ones(9),'--r')
plot(-3e-3*ones(9),'--r')
subplot(2,2,2)
plot(Press[1:]-Press[:-1],'-o')
plot(3*ones(9),'--r')
plot(-3*ones(9),'--r')
subplot(2,2,3)
plot(MxForce[1:]-MxForce[:-1],'-o')
plot(5e-2*ones(9),'--r')
plot(-5e-2*ones(9),'--r')
plot(5e-3*ones(9),'--g')
plot(-5e-3*ones(9),'--g')
subplot(2,2,4)
plot(BandGap[1:]-BandGap[:-1],'-o')
plot(1e-2*ones(9),'--r')
plot(-1e-2*ones(9),'--r')
ylim(-0.015,0.015)
savefig("converge.png")

figure()
plot(cutOff,TOTEN,'-o')
grid()
title("Total energy as function of various cut off energies")
xlabel("Energy cut off [eV]")
ylabel("Total energy [eV]")
savefig("TOTENplot.png")

figure()
plot(cutOff,MxForce,'-o')
grid()
title("Maximum force as function of various cut off energies")
xlabel("Energy cut off [eV]")
ylabel("Total energy [eV]")
savefig("MxForcePlot.png")
