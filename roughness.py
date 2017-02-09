import pandas as pd
import math
import numpy as np

p1=pd.read_csv("./postProcessing/Upstream/0/faceSource.dat", skiprows=[0,1,2,3], header=0,names=["Time","Pressure"], sep="\t")
p2=pd.read_csv("./postProcessing/Downstream/0/faceSource.dat", skiprows=[0,1,2,3], header=0,names=["Time","Pressure"], sep="\t")

surfaceArea=0.0505
info=pd.DataFrame()
info['Time']=p1.Time
info['Head_loss']=(p1.Pressure-p2.Pressure)*1000.0/9810.0

L=1.686
flow=0.035
diameter=0.254
radius=0.5*diameter
V=flow/(3.14*(radius*radius))
info['f']=(info.Head_loss*diameter*2*9.81)/(L*V*V)

info['n']=((diameter*0.25)**(0.16666666))*np.sqrt(info.f/(8*9.81))

meanInfo=(info.tail(10)).mean()
info.to_csv("manning")
print meanInfo


