import imageio
import os
os.chdir('D:\课\信导\project\data\png')
Q = os.listdir()
W = []
for png in Q:
    W.append(imageio.imread(png))
imageio.mimsave('GIF.gif', W, 'GIF', duration=0.3)
