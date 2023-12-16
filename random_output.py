import random

#  给定一个类的数字，随机输出一个属于该类的元组
def random_output(cluster, cluster_num):
    cluster_dict = {}
    for i in cluster:
        if i[1] not in cluster_dict.keys():
            cluster_dict[i[1]] = []
            cluster_dict[i[1]].append(i)
        else:
            cluster_dict[i[1]].append(i)

    output = cluster_dict[cluster_num]

    return random.choice(output)

if __name__ == '__main__':
    cluster = [('a', 1), ('b', 1), ('c', 1), ('d', 2), ('e', 2), ('f', 3), ('g', 3), ('h', 3)]
    a = random_output(cluster, 1)
    print(a)