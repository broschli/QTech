# -*- coding: utf-8 -*-
"""
Polarization measurement of a two photon source.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.optimize import curve_fit


# Import data
data1 = np.genfromtxt("./data/p1_data_1.csv", delimiter=";", skip_header=1)
data2 = np.genfromtxt("./data/p1_data_2.csv", delimiter=";", skip_header=1)


# %% Dataset 1
# Split data in subsets with same alpha
data1_split = np.split(data1, 9, axis=0)

# Fit and plot counts of beta for different alpha 0° ... 90°
def fit(angle, I0, phi):
    return I0 * np.cos(angle/180 * np.pi - phi)**2

angles = np.linspace(0, 180, 100)

fig1, ax = plt.subplots()
for data in data1_split[:5]:
    alpha = data[0,0]
    ax.scatter(data[:,1], data[:,2], marker="o", s=16,
            label="$\\alpha = $" + str(alpha) + "°")
    
    param, _ = curve_fit(fit, data[:,1], data[:,2])
    ax.plot(angles, fit(angles, *param),)

ax.set(xlabel="$\\beta$ in °", ylabel="coincident counts", title="Dataset 1")
# ax.text(195, 700 , "Fit function:\n$I_0 \\, \\cos^2(\\beta-\\phi)$")
ax.set_xticks(data1_split[0][:,1])
ax.grid()

handles, labels = ax.get_legend_handles_labels()
handles.append(mpatches.Patch(color="none", 
                              label="Fit function:\n$I_0 \\, \\cos^2(\\beta-\\phi)$"))
ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.325, 1))


# %% Dataset 2
# Split data in subsets with same alpha
data2_split = np.split(data2, 9, axis=0)

# Fit and plot counts of beta for different alpha
fig2, ax = plt.subplots()
for data in data2_split[:5]:
    alpha = data[0,0]
    ax.scatter(data[:,1], data[:,2], marker="o", s=16,
            label="$\\alpha = $" + str(alpha) + "°")
    
    param, _ = curve_fit(fit, data[:,1], data[:,2])
    ax.plot(angles, fit(angles, *param),)

ax.set(xlabel="$\\beta$ in °", ylabel="coincident counts", title="Dataset 2")
ax.set_xticks(data1_split[0][:,1])
ax.grid()

handles, labels = ax.get_legend_handles_labels()
handles.append(mpatches.Patch(color="none", 
                              label="Fit function:\n$I_0 \\, \\cos^2(\\beta-\\phi)$"))
ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.325, 1))


# Fit and plot counts of alpha for fixed beta=90°
def fit2(angle, I0):
    return I0 * np.cos(angle/180 * np.pi)**2

param, _ = curve_fit(fit2, data2[4::9,0], data2[4::9,2], p0=(1400))

fig3, ax = plt.subplots()
ax.scatter(data2[4::9,0], data2[4::9,2], s=16)
ax.plot(angles, fit2(angles, *param),
        label="Fit with $I_0 \\, \\cos^2(\\alpha)$")
ax.set(xlabel="$\\alpha$ in °", ylabel="conincident counts", 
       title="Dataset 2 for $\\beta = 90°$")
ax.set_xticks(data2[4::9,0])
ax.grid()
ax.legend(loc="upper center")

