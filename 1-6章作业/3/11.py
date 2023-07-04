import random

print('''
    欢迎来到尼姆的游戏!
    规则如下:
        将硬币分成几堆；
        两个人轮流取硬币；
        每次取硬币只能从同一堆中取出，枚数不限，但至少要取一枚；
        取走最后一枚硬币的是输家，逼迫对方取到最后一枚硬币是赢家。
''')

# 1.生成硬币堆 用一个字典来存储有多少硬币
while True:
    try:
        line = int(input("请输入行数:"))
        lineNum = int(input("请输入第一行有几个硬币:"))
        break
    except Exception:
        print("输入错误!请重新输入")


# 生成硬币堆
def generate_dict(line, lineNum):
    d = dict()
    for i in range(line):
        d[i] = lineNum + i

    return d


# 展示硬币堆
def show_dict(d):
    for i in range(len(d)):
        if d[i] > 0:
            print("第", i + 1, "行:", end="\t")
            for j in range(d[i]):
                print("●", end="\t")
            print()


# 修改硬币堆
def updata_dict(d, line, count):
    d[line] = d[line] - count

# 根据参数生成行和硬币数
d1 = generate_dict(line, lineNum)
# d1 = generate_dict(3, 3) # TestCode
show_dict(d1)

countGame = 0  # 游戏进行的次数 单数为玩家,双数为机器人
line = 0	# 取硬币的第几行
count = 0	# 取硬币多少个硬币

while True:
    if sum(d1.values()) <= 0:  # 如果所有的硬币都为零则游戏结束
        break
    while True:
        # 开始游戏  玩家拿走硬币
        try:
            line = int(input("请输入要拿走第几行的硬币:")) - 1
            count = int(input("请输入要拿走几个硬币:"))
            if count <= d1[line]:
                break
        except Exception:
            print("输入错误!请重新输入")
            
    updata_dict(d1, line, count) # 根据玩家的意愿修改取走硬币
    countGame += 1
    show_dict(d1)	# 展示剩下的硬币
    print("你拿走了{}行的{}枚硬币".format(line + 1, count))
    # 机器人拿走硬币
    if sum(d1.values()) <= 0:  # 如果没有硬币则直接结束游戏
        break
    elif d1[line] > 0:  # 如果当前列是否还有有硬币
        RobotCount = random.randint(1, d1[line])
    else: # 寻找有硬币的行
        for i in range(len(d1)):
            if d1[i] > 0:
                line = i

    # 机器人拿走的硬币
    RobotCount = random.randint(1, d1[line])

    updata_dict(d1, line, RobotCount)
    countGame += 1
    print("机器人拿走了{}行的{}枚硬币".format(line + 1, RobotCount))
    show_dict(d1)

#  # 判断游戏结果
if countGame % 2 == 1:
    print("你输了")
else:
    print("你赢了")
