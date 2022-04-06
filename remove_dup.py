read = input().strip('[ ]').split()
read = list(map(lambda x: int(x), read))

if len(read) == 0:
    print('no_inputs')
elif len(set(read)) == len(read):
    print('no_change')
else:
    result = sorted(list(set(read)))
    print(*result)
