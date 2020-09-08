# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 00:37:01 2020

@author: vumin
"""

import numpy as np
import matplotlib.pyplot as plt
# plt.plot([0,1,4,9,16])
# plt.show()
# x = np.linspace(0,10,20)
# y1 = x**2.0
# y2 = x**1.5
# plt.loglog(x,y1,"bo-",linewidth=2,markersize=5,label="First")
# plt.loglog(x,y2,"gd-",linewidth=4,markersize=10,label="Second")
# plt.xlabel("$X$")
# plt.ylabel("$Y$")
# plt.axis([-0.5,10.5,-5,105])
# plt.legend(loc="upper left")
# plt.savefig("plot.pdf")

histogram = np.random.normal(size=1000)
# plt.hist(histogram)
# plt.hist(histogram, bins = 30, cumulative=True, density=True, histtype="step")
# gamma_plot = np.random.gamma(2,3,1000)
# plt.hist(gamma_plot, bins=50)

plt.figure()
# plt.subplot(221)
# plt.hist(histogram, bins = 30)
# plt.subplot(222)
# plt.hist(histogram, bins = 30, density=True)
# plt.subplot(223)
# plt.hist(histogram, bins = 30, cumulative=True)
# plt.subplot(224)
# plt.hist(histogram, bins = 30, density=True, cumulative=True, histtype="step")

plt.subplot(3, 3, 3)
plt.subplot(333)


