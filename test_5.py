def chain_sum(num):
    total = 0
    for i in num:
        total += i
    return total


print(chain_sum([5]))
# 5
print(chain_sum([5, 2]))
# 7
print(chain_sum([5, 100, -10]))
# 95

