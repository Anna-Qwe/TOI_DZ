from pylab import rcParams
import pandas as pd
import seaborn as sns


def byte_reader(path):
    with open(path, 'rb') as file:
        lines = file.readlines()
    byte_list = []
    for line in lines:
        for byte in line:
            byte_list.append(byte)
    dic = {}
    for byte in byte_list:
        if byte not in dic:
            dic[byte] = 0
        dic[byte] += 1
    inds = sorted(list(dic.keys()))
    vals = [dic[index] for index in inds]

    return inds, vals


inds1, vals1 = byte_reader('hm_8bit.bmp')
inds2, vals2 = byte_reader('TOI_LUChShIJ_PREDMET_NA_SVETE.doc')

rcParams['figure.figsize'] = 100, 10
ax1 = sns.barplot(x=inds1, y=vals1)
ax1.set(xlabel='Byte', ylabel='Count', title='BMP')
ax1.get_figure().savefig('BMP.png')

rcParams['figure.figsize'] = 100, 10
ax2 = sns.barplot(x=inds2, y=vals2)
ax2.set(xlabel='Byte', ylabel='Count', title='DOC')
ax2.get_figure().savefig('DOC.png')

import numpy as np

vals1 = np.array(vals1)
vals2 = np.array(vals2)

bytes_amount1 = vals1.sum()
bytes_amount2 = vals2.sum()

norm_vals1 = vals1 / bytes_amount1
norm_vals2 = vals2 / bytes_amount2

entr1 = -(norm_vals1 * np.log2(norm_vals1)).sum()
entr2 = -(norm_vals2 * np.log2(norm_vals1)).sum()

print("Enthropy of BMP-file: {0}, enthropy of DOC-file: {1}".format(entr1, entr2))