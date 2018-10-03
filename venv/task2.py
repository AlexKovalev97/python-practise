n = int(input('n='))
m = n * 3
v_dash = '.|.'

for i in range(n // 2):
    v_dash_num = int(2*i+1)
    dash_num = int((m - (3 * (2 * i + 1))) / 2)
    print('-' * dash_num, v_dash * v_dash_num, '-' * dash_num)

wel_num = int((m - 7) / 2)
print('-' * wel_num, 'WELCOME', '-' * wel_num)

for i in range((n // 2) - 1, -1, -1):
    v_dash_num = int(2*i+1)
    dash_num = int((m - (3 * (2 * i + 1))) / 2)
    print('-' * dash_num, v_dash * v_dash_num, '-' * dash_num)