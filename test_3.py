def find_in_different_registers(words):
    res = []
    for i in words:
        i = i.lower()
        if i not in res:
            res.append(i)
    print(res)


words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
print(find_in_different_registers(words))
# ['мама', 'папа', 'дядя', 'брат']