import numpy as np
import matplotlib.pyplot as plt

camera_1d = np.loadtxt('camera.txt')

camera_1d = camera_1d.reshape(512,512)

camera_1d = camera_1d.T

plt.imshow(camera_1d, interpolation = 'nearest', cmap = 'gray')

plt.show()