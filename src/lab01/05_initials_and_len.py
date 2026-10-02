fio = input('ФИО: ')
a = fio.split()
init = a[0][0] + a[1][0] + a[2][0]
print(f'Инициалы: {init.upper()}.')
print(f'Длина (символов): {len(' '.join(a))}')