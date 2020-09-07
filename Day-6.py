# n = int(input())
# for i in range(0,n):
#     s = input()
# even = []
# odd = []
# for i, c in enumerate(s):
#     if i % 2 == 0:
#         even.append(c)
#     else:
#         odd.append(c)
# print(''.join(even), ''.join(odd))


for _ in range(int(input())):
    my_str = input()
    print(f"{my_str[::2]} {my_str[1::2]}")
