def my_list():
    list0 = [1, 2, 3, 4]
    list1 = []
    for i in list0:
        for j in list0:
            if i == j:
                continue
            for k in list0:
                if (i == k) or (j == k):
                    continue
                for l in list0:
                    if (i == l) or (j == l) or (k == l):
                        continue
                    result = 1000 * i + 100 * j + 10 * k + l
                    list1.append(result)
    return list1

prime_list=[p for p in my_list() if 0 not in [p%d for d in range(2,int(p**0.5+1))]]
print(prime_list)
