#!/usr/bin/env python


import numpy as np

filename=open("test.gdml","w") 
n=7 # number of boxes to make
radius=np.array([700,700,700,700,700,700,700])
angle=np.array([0., 360./7, 2*360./7, 3*360./7, 4*360/7, 5*360/7, 6*360/7, 7*360/7])
size= np.array([100,100,100,100,100,100,100])
print(angle)


out="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
out+="<gdml xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"http://service-spi.web.cern.ch/service-spi/app/releases/GDML/schema/gdml.xsd\">\n"

out+="<define>\n</define>\n"

out+="<materials>\n"
out+="\t<material formula=\" \" name=\"Air\" >\n"
out+="\t\t <D value=\"1.290\" unit=\"mg/cm3\"/>\n"
out+="\t\t <fraction n=\"0.7\" ref=\"G4_N\" />\n"
out+="\t\t <fraction n=\"0.3\" ref=\"G4_O\" />\n"
out+=" \t</material>\n"
out+="</materials>\n"


out+="<solids>\n"
out+="\t<box lunit=\"mm\" name=\"World\" x=\"1400\" y=\"1400\" z=\"1400\"/>\n"
for i in range(0, n):
    out+="\t <box lunit=\"mm\" name=\"Tracker"+str(i+1)+"\" x=\""+str(size[i])+"\" y=\""+str(size[i])+"\" z=\""+str(size[i])+"\"/>\n"
out+="</solids>\n"

out+="<structure>\n"

for i in range(0, n):
   out+="<volume name=\"Tracker"+str(i+1)+"\">\n"
   out+="\t<materialref ref=\"Air\"/>\n"
   out+="\t<solidref ref=\"Tracker"+str(i+1)+"\"/>\n"
   out+="</volume>\n"


out+="<volume name=\"World\" >\n"
out+="\t<materialref ref=\"G4_Galactic\" />\n"
out+="\t<solidref ref=\"World\" />\n"

for i in range(0,n):
   out+="\t<physvol>\n"
   out+="\t\t <volumeref ref=\"Tracker"+str(i+1)+"\" />\n"
   out+="\t\t <position name=\"TrackerinWorldpos"+str(i+1)+"\" unit=\"mm\" x=\""+str(radius[i]*np.cos(angle[i]*3.1416/180))+"\" y= \""+str(radius[i]*np.sin(angle[i]*3.1416/180))+"\" z=\"0\"/>\n"
   out+="\t\t <rotation name=\"TrackerinWorldrot"+str(i+1)+"\" unit=\"deg\" x=\""+str(0)+"\" y= \""+str(0)+"\" z=\""+str(-1.0*angle[i])+"\"/>\n"
   out+="\t </physvol>\n"
out+="</volume>\n"

out+="</structure>\n"

out+="<setup name=\"Default\" version=\"1.0\" >\n"
out+="\t<world ref=\"World\"/>\n"
out+="</setup>\n"

out+="</gdml>\n"


filename.write(out)
