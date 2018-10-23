# -*- coding: UTF-8 -*-
import copy

# item -> trans
data = {}
# 支持度
min_support = 0.5
size = 0
result = set()


def default_judge(prefix_list):
    global result
    if len(prefix_list) == 0:
        return True

    key = "".join(prefix_list)
    if len(data[key]) >= size * min_support:
        result.add(key)
        return True
    else:
        # print key, False
        return False


def combination(prefix_list, item_list, func=default_judge):
    if not func(prefix_list):
        return

    for i in range(len(item_list)):
        temp = copy.copy(item_list)

        # print "length", len(item_list), i
        ch = temp.pop(i)
        if len(prefix_list) == 0 or (len(prefix_list) > 0 and prefix_list[-1] < ch):
            if len(prefix_list) > 0:
                key1 = "".join(prefix_list)
                key2 = "".join(prefix_list + [ch])
                data[key2] = data[key1] & data[ch]
            combination(prefix_list + [ch], temp)

def main(file_path):
    global size
    # 事务的数量
    with open(file_path, 'r') as fp:
        for line in fp:
            size += 1
            line = line.strip()
            item_list = line.split(":")

            items = item_list[1].split(",")
            for item in items:
                if item not in data:
                    data[item] = set()
                data[item].add(int(item_list[0]))

    combination([], data.keys())
    print "len(data)", len(data)
    # 结果数据集
    print result

if __name__ == "__main__":
    f = "./eclat.dat"
    main(f)
