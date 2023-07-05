# # 8393

# num = int(input())
# sum = 0

# for i in range(1, num + 1):
#     sum += i

# print(sum)

# # 1929

# def check_prime(num):
#     if (num == 1):
#         return 0
#     for i in range(2, int(num**0.5) + 1, 1):
#         if (num % i == 0):
#             return 0
#     return 1


# M, N = map(int, input().split())

# for i in range(M, N + 1, 1):
#     if (check_prime(i)):
#         print(i)

# # 1978

# def check_prime(num):
#     if (num == 1):
#         return 0
#     for i in range(2, int(num**0.5) + 1, 1):
#         if (num % i == 0):
#             return 0
#     return 1


# N = int(input())
# num_lst = list(map(int, input().split()))
# cnt = 0

# for num in num_lst:
#     if (check_prime(num)):
#         cnt += 1

# print(cnt)

# # 4948

# def check_prime(num):
#     if (num == 1):
#         return 0
#     for i in range(2, int(num**0.5) + 1, 1):
#         if (num % i == 0):
#             return 0
#     return 1


# while (True):
#     num = int(input())
#     if (num == 0):
#         break
#     cnt = 0
#     for i in range(num + 1, 2 * num + 1):
#         if (check_prime(i)):
#             cnt += 1
#     print(cnt)

# # 15649

# N, M = map(int, input().split())

# lst = []


# def dfs():
#     if len(lst) == M:
#         print(" ".join(map(str, lst)))
#         return

#     for i in range(1, N + 1):
#         if i not in lst:
#             lst.append(i)
#             dfs()
#             lst.pop()


# dfs()

# 15650

# N, M = map(int, input().split())

# lst = []


# def dfs():
#     flag = 0
#     if len(lst) == M:
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 flag = 1
#         if flag == 0:
#             print(" ".join(map(str, lst)))
#         return

#     for i in range(1, N + 1):
#         if i not in lst:
#             lst.append(i)
#             dfs()
#             lst.pop()


# dfs()

# 6603

# init_lst = []
# lst = []


# def dfs(S):
#     flag = 0
#     if len(lst) == 6:
#         for i in range(len(lst) - 1):
#             if lst[i] > lst[i + 1]:
#                 flag = 1
#         if flag == 0:
#             print(" ".join(map(str, lst)))
#         return

#     for i in S:
#         if i not in lst:
#             lst.append(i)
#             dfs(S)
#             lst.pop()


# while True:
#     init_lst = list(map(int, input().split()))
#     if len(init_lst) == 1 and init_lst[0] == 0:
#         break
#     k = init_lst[0]
#     S = init_lst[1:]
#     dfs(S)
#     print()
