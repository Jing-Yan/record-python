# -*- coding:utf-8 -*-

# 递归函数


# 第一种方法, 如果超过1000，栈会溢出
def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)


# 第二种方法，解决栈溢出的问题
def fact_(a):
    return fact_iter(a, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)


# 汉诺塔 递归函数
def move(n, x, y, z,):
    if n == 1:
        print x, "-->", z
    else:
        move(n-1, x, z, y)  # 将前n-1个盘子从x移动到y上
        move(1, x, y, z)  # 将最底下的最后一个盘子从x移到z上
        move(n-1, y, x, z)  # 将y上的n-1的盘子移到z上
n = int(input('请输入汉诺塔的层数：'))


if __name__ == "__main__":
    # print fact_(5)
    move(n, 'A', 'B', 'C')
