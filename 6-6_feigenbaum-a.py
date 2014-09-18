#! usr/bin/env python
# coding:utf-8

""" 計算機実習
問題6.6 ファイゲンバウム定数の評価
-a 相加平均でファイゲンバウム定数を求める
作成者：藤本將太郎
"""

import matplotlib.pylab as plt
from Tkinter import *
import numpy

b = [0.750000, 0.862372, 0.886023, 0.891102,
     0.892190, 0.892423, 0.892473, 0.892484]
#      b1         b2        b3        b4
#      b5         b6        b7        b8

def delta(k):
    return (b[k - 1] - b[k - 2]) / (b[k] - b[k - 1])

plt.gca().set_xlim(1.5, len(b) - 0.5)
plt.xlabel(r'$k$')
plt.ylabel(r'$\delta_{k}$')
plt.title('Feigenbaum constant')
sum_delta_k = 0

for k in range(2, len(b)):
    plt.scatter(k, delta(k), color='r', s=8, marker='o')
    sum_delta_k = sum_delta_k + delta(k)
ave_delta_k = sum_delta_k / 6

plt.plot([2, len(b) - 1], [ave_delta_k] * 2,
         label=r'$\mathrm{average}\ \mathrm{of}\ \delta_{k}\ :\ \delta \ =\ $'
         + str(ave_delta_k)
         )

plt.legend(loc="best")
plt.show()
