#! usr/bin/env python
# coding:utf-8

""" 計算機実習
問題6.6 ファイゲンバウム定数の評価
-a 相加平均でファイゲンバウム定数を求める
作成者：藤本將太郎
"""

import matplotlib.pylab as plt
from Tkinter import *
import numpy as np

b = [0.750000, 0.862372, 0.886023, 0.891102,
     0.892190, 0.892423, 0.892473, 0.892484]
#      b1         b2        b3        b4
#      b5         b6        b7        b8

def delta(k):
    return (b[k - 1] - b[k - 2]) / (b[k] - b[k - 1])

b_index = range(2, len(b))
delta_k = np.array(map(delta, b_index))
ave_delta_k = np.average(delta_k)

plt.scatter(b_index, delta_k, color='r', s=8, marker='o')
plt.plot([2, len(b) - 1], [ave_delta_k] * 2,
         label=r'$\mathrm{average}\ \mathrm{of}\ \delta_{k}\ :\ \delta \ =\ $'
         + str(ave_delta_k)
         )
plt.gca().set_xlim(1.5, len(b) - 0.5)
plt.xlabel(r'$k$')
plt.ylabel(r'$\delta_{k}$')
plt.title('Feigenbaum constant')
plt.legend(loc='best')
plt.show()
