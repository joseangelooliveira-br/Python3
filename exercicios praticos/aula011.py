print('\033[1:30:47mOla mundo!\033[m')
print('\033[7:30:47mOla mundo!\033[m')
print('\033[4:30:47mOla mundo!\033[m')
print('\033[0:30:47mOla mundo!\033[m')
print('\033[3:30:47mOla mundo!\033[m')
print('\033[1:32:46mOla mundo!\033[m')
print('\033[1:33:45mOla mundo!\033[m')
print('\033[1:31:46mOla mundo!\033[m')
print('\033[7:31:46mOla mundo!\033[m')
a = 3
b = 5

print('Os valores \33[1:31m{}\33[m e \33[1:34m{}\33[m são inteiros.'.format(a, b))
print('Os valores {} e {} são inteiros.'.format(a, b))
print('Os valores {}{}{} e {}{}{} são inteiros.'.format('\33[1:31m',a,'\33[m','\33[1:34m', b,'\33[m'))