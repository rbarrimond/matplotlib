from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import tarfile
from urllib.request import urlopen

url = 'https://ndownloader.figshare.com/files/5976036'
b = BytesIO(urlopen(url).read()) 
fpath = 'CaliforniaHousing/cal_housing.data'

with tarfile.open(mode='r', fileobj=b) as archive:
    housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')
    
    value = housing[:, -1]
    pop, age = housing[:, [4, 7]].T 
    
def add_innerbox(ax: Axes, text):
    ax.text(0.55, 0.8, text,
            horizontalalignment='center',
            transform=ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=12.5)
    
gridsize = (3, 2)

fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0,0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2,0))
ax3 = plt.subplot2grid(gridsize, (2,1))

ax1.set_title('Home value as a function of home age (x) & area population (y)',
              fontsize=14)
sctr = ax1.scatter(x=age, y=pop, c=value, cmap='RdYlGn')
plt.colorbar(sctr, ax=ax1, format='$%d')
ax1.set_yscale('log')
ax2.hist(age, bins='auto')
ax3.hist(pop, bins='auto', log=True)

add_innerbox(ax2, 'Histogram: home age')
add_innerbox(ax3, 'Histogram: area population (log scale)')

plt.show()
