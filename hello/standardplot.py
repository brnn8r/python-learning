#%%
import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.cos(x))
plt.plot([0,20],[0,0],'k-')
plt.show()
