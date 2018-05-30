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

for symbol, count in dic.items():
    print("Symbol {0} appears {1} times".format(symbol, count))