import sys

print("please select option type : -a == write, -v == read")
option = input()

memo = input()

print('option : ', option)
print('memo : ', memo)
    f = open('memo.txt', 'a')

if option == '-a':
    f.write(memo)
    f.write('\n')
    f.close()
elif option == 'r':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print("memo print ", memo)

