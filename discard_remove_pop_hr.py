"""Discard-remove-pop operations in python (HackerRank Problem)"""
'''method 1'''

# n = int(input())
# s = set(map(int, input().split()))      # set of n numbers
# operations = int(input())

# for x in range(operations):             # Iterate in range of the input num
#   oper = input().split()
#   if oper[0] == "remove":
#     s.remove(int(oper[1]))
#   elif oper[0] == "discard":
#     s.discard(int(oper[1]))
#   else:
#     s.pop()
    
# print(sum(s))


'''method 2'''

# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
# for i in range(N):
#     cmd = list(map(str, input().split()))
#     if cmd[0] == "pop":
#         s.pop()
#     elif cmd[0] == "remove":
#         try:
#             s.remove(int(cmd[1]))
#         except:
#             continue
#     elif cmd[0] == "discard":
#         try:
#             s.discard(int(cmd[1]))
#         except:
#             continue
# print(sum(s))


'''
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5


4
'''
