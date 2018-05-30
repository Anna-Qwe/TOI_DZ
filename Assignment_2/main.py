def byte_reader(path):
    with open(path, 'r', encoding='utf-16') as file:
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
    return dic

dic = byte_reader('9VAR.txt')

import numpy as np
vals = np.array(list(dic.values()))
symbols_amount = vals.sum()
norm_vals = vals / symbols_amount
entr = -(norm_vals * np.log2(norm_vals)).sum()

for symbol, count in dic.items():
    print("Symbol {0} appears in {1}% of times".format(symbol, round(count / symbols_amount * 100, 2)))

print("Entropy of text: {0}".format(entr))
