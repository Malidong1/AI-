import numpy as np
import operator


class State:
    def __init__(self, m):
        self.node = m  # 节点代表的状态
        self.f = 0  # f(n)=g(n)+h(n)
        self.g = 0  # g(n)
        self.h = 0  # h(n)
        self.father = None  # 节点的父亲节点


# 对节点列表按照估价函数的值的规则排序
def list_sort(l):
    cmp = operator.attrgetter('f')
    l.sort(key=cmp)


# A*算法
def A_star(s, goal1):
    openlist = [s]
    while openlist:  # 当open表不为空
        get = openlist[0]  # 取出open表的首节点
        if (get.node == goal.node).all():  # 判断是否与目标节点一致
            return get
        openlist.remove(get)  # 将get移出open表

        # 判断此时状态的空格位置（a,b)
        for a in range(len(get.node)):
            for b in range(len(get.node[a])):
                if get.node[a][b] == 0:
                    break
            if get.node[a][b] == 0:
                break

        # 开始移动
        for i in range(len(get.node)):
            for j in range(len(get.node[i])):
                c = get.node.copy()
                if (i + j - a - b) ** 2 == 1:
                    c[a][b] = c[i][j]
                    c[i][j] = 0
                    new = State(c)
                    new.father = get  # 此时取出的get节点成为新节点的父亲节点
                    new.g = get.g + 1  # 新节点与父亲节点的距离
                    new.h = heu(new, goal1)  # 新节点的启发函数值
                    new.f = new.g + new.h  # 新节点的估价函数值
                    openlist.append(new)  # 加入open表中
        list_sort(openlist)  # 排序


# 启发函数，统计位置不相同的个数
def heu(s, goal2):
    a = 0
    # print(goal2.node)
    for i in range(len(s.node)):
        for j in range(len(s.node[i])):
            if s.node[i][j] != goal2.node[i][j]:
                a = a + 1
    # print(a)
    return a


# 递归打印路径
def printpath(f):
    if f is None:
        return
    printpath(f.father)
    print(f.node)


if __name__ == '__main__':
    h = 3
    A = list(input("请输入初始状态："))
    B = list(input("请输入目标状态："))
    z = 0
    M = np.zeros((h, h))  # 初始状态
    N = np.zeros((h, h))  # 目标状态
    for i in range(h):
        for j in range(h):
            M[i][j] = A[z]
            N[i][j] = B[z]
            z = z + 1

    init = State(M)  # 初始状态
    goal = State(N)  # 目标状态
    print(init.node)
    print(goal.node)
    final = A_star(init, goal)
    if final:
        print("求解步骤为：")
        printpath(final)
    else:
        print("无解")
