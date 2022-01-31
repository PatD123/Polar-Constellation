import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



def plot_polar(radius, angle):
    # Defining figures for conversion
    fig = Figure()
    canvas = FigureCanvas(fig)
    
    # setting the axes projection as polar
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    print(radius, angle)

    # Degrees to Radians
    angle = math.radians(angle)

    ax.set_ylim(0, 100)

    # plotting the circle
    ax.plot(angle, radius, 'o')

    # Converting img into numpy array
    fig.canvas.draw()
    image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image_from_plot
