import numpy as np
import matplotlib.pyplot as plt
import math


def plot_polar(radius, angle):
    # setting the axes projection as polar
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    print(radius, angle)
    # Degrees to Radians
    angle = math.radians(angle)

    ax.set_ylim(0, 100)

    # plotting the circle
    ax.plot(angle, radius, 'o')

    # display the Polar plot
    plt.show()