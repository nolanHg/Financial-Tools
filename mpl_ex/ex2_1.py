#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Generate data
y_raw = np.random.randn(1000).cumsum() + 15
x_raw = np.linspace(0, 24, y_raw.size)

# Get averages of every 100 samples
x_pos = x_raw.reshape(-1, 100).min(axis = 1)
y_avg = y_raw.reshape(-1, 100).mean(axis = 1)
y_err = y_raw.reshape(-1, 100).ptp(axis = 1)

bar_width = x_pos[1] - x_pos[0]

# Make a made up future prediction with a fake confidence
x_pred = np.linspace(0, 30)
y_max_pred = y_avg[0] + y_err[0] + 2.3 * x_pred
y_min_pred = y_avg[0] - y_err[0] + 1.2 * x_pred

barcolor, linecolor, fillcolor = 'wheat', 'salmon', 'lightblue'

fig, ax = plt.subplots()

## Plot blue envelope
ax.fill_between(x_pred, y_max_pred, y_min_pred, color = fillcolor)

## Plot bars
ax.bar(x_pos, y_avg, align = 'edge', color = barcolor, width = bar_width, edgecolor = 'black', linewidth = 0.5, yerr = y_err, capsize = 2)

## Plot squiggly line
ax.plot(x_raw, y_raw, color = linecolor, linewidth = 1)

## Add title, labels; set range for x 
ax.set_xlim(0, 30)
ax.set_title("Future Projection of Attitudes")
ax.set_xlabel("Minutes since class began")
ax.set_ylabel("Snarkiness (snark units)")

plt.show()
