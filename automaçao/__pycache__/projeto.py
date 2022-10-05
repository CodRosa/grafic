from cProfile import label
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35,25,25,15])
mylabels = ['Marketing e Varejo','Esporte','Jurídica','Educação']
myexplode = [0.2 , 0.2 , 0 ,0]
plt.pie(y,labels = mylabels , explode = myexplode, shadow=True)
plt.show()