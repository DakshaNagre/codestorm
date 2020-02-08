# -*- coding: utf-8 -*-
"""DR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqwOGTG6wDaSH0tbB2ZKL9-LC-rIZfA8
"""

# !pip install netCDF4

# !wget https://noaa-nexrad-level2.s3.amazonaws.com/1991/07/05/KTLX/KTLX19910705_235109.gz

# !pip install arm_pyart

#!gunzip /content/KTLX19910705_235109.gz

print(__doc__)

# Author: Jonathan J. Helmus (jhelmus@anl.gov)
# License: BSD 3 clause

import matplotlib.pyplot as plt
import pyart
import netCDF4


# read the data and create the display object
filename = 'KTLX19910705_235109'
radar = pyart.io.read_nexrad_archive(filename)
display = pyart.graph.RadarDisplay(radar)

# fields to plot and ranges
fields_to_plot = ['reflectivity', 'velocity']
ranges = [(-32, 64), (-17.0, 17.0)]

# plot the data
nplots = len(fields_to_plot)
plt.figure(figsize=[5 * nplots, 4])

# plot each field
for plot_num in range(nplots):
    field = fields_to_plot[plot_num]
    vmin, vmax = ranges[plot_num]

    plt.subplot(1, nplots, plot_num + 1)
    display.plot(field, 0, vmin=vmin, vmax=vmax, title_flag=False)
    display.set_limits(ylim=[0, 17])

# set the figure title and show
instrument_name = radar.metadata['instrument_name']
time_start = netCDF4.num2date(radar.time['data'][0], radar.time['units'])
time_text = ' ' + time_start.isoformat() + 'Z '
azimuth = radar.fixed_angle['data'][0]
title = 'RHI ' + instrument_name + time_text + 'Azimuth %.2f' % (azimuth)
plt.suptitle(title)
plt.show()