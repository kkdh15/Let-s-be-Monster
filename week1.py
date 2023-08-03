# #3040

# num_lst = []

# for _ in range(9):
#   num_lst.append(int(input()))

# for i in range(9):
#   for j in range(i + 1, 9):
#     if (sum(num_lst) - num_lst[i] - num_lst[j] == 100):
#       x, y = i, j
#       break

# num_lst.pop(x)
# num_lst.pop(y - 1)

# for num in num_lst:
#   print(num)

# #2798
# N, M = map(int, input().split())
# card_list = list(map(int, input().split()))
# result = 0

# for i in range(N):
#   for j in range(i + 1, N):
#     for k in range(j + 1, N):
#       tmp_lst = []
#       tmp_lst.append(card_list[i])
#       tmp_lst.append(card_list[j])
#       tmp_lst.append(card_list[k])
#       if (sum(tmp_lst) <= M):
#         result = max(sum(tmp_lst), result)

# print(result)

# #19532
# a, b, c, d, e, f = map(int, input().split())

# for x in range(-999, 1000):
#   for y in range(-999, 1000):
#     if (a * x + b * y == c and d * x + e * y == f):
#       ans_x, ans_y = x, y
#       break

# print(ans_x, ans_y)

# #1051
# N, M = map(int, input().split())
# num_lst = []
# for i in range(N):
#   num_lst.append(list(input()))

# max_len = min(N, M)
# ans_len = 0

# for i in range(N):
#   for j in range(M):
#     for k in range(max_len):
#       if (i + k >= N or j + k >= M):
#         continue
#       else:
#         if (num_lst[i][j] == num_lst[i][j + k] and
#            num_lst[i][j + k] == num_lst[i + k][j] and
#            num_lst[i + k][j] == num_lst[i + k][j + k]):
#           ans_len = max(k, ans_len)

# print((ans_len + 1) * (ans_len + 1))

# #2231
# N = int(input())

# for i in range(N):
#   sum = i
#   ans = i
#   while (i > 0):
#     sum += i % 10
#     i = i // 10
#   if sum == N:
#     break
# else:
#   ans = 0
# print(ans)

# #15650
# N, M = map(int, input().split())

# def rec(lst):
#   if (len(lst) == M):
#     for i in lst:
#       print(i, end=" ")
#     print()
#     lst.pop()
#     return
#   for next in range(lst[-1] + 1, N + 1):
#     lst.append(next)
#     rec(lst)
#   lst.pop()


# for i in range(1, N + 1):
#   lst = [i]
#   rec(lst)

# #6603
# def rec(lst, src_lst):
#   if (len(lst) == 6):
#     for i in lst:
#       print(i, end=" ")
#     print()
#     lst.pop()
#     return
#   for next in S:
#     if (lst[-1] < next):
#       lst.append(next)
#       rec(lst, S)
#   lst.pop()

# while(True):
#   input_lst = list(map(int, input().split()))
#   K = input_lst[0]
#   S = input_lst[1:]
#   if (K == 0):
#     break
#   for i in S:
#     lst = [i]
#     rec(lst, S)
#   print()

# #1182
# def rec(lst, src_lst, S, idx):
#   global cnt
#   if (sum(lst) == S):
#     cnt += 1
#   for idx in range(idx + 1, len(src_lst)):
#     lst.append(src_lst[idx])
#     rec(lst, src_lst, S, idx)
#   lst.pop()

# N, S = map(int, input().split())
# num_lst = list(map(int, input().split()))
# cnt = 0

# for idx in range(len(num_lst)):
#   lst = [num_lst[idx]]
#   rec(lst, num_lst, S, idx)

# print(cnt)

# #2992
# X = int(input())

# tmp = X
# min_num = 1000000
# elements = []

# while (tmp > 0):
#   elements.append(tmp % 10)
#   tmp //= 10

# def rec(lst, elements, idx):
#   global min_num
#   tmp = 0
#   if (len(lst) == len(elements)):
#     for i in lst:
#       tmp *= 10
#       tmp += i
#     if (tmp > X):
#       min_num = min(min_num, tmp)
#     lst.pop()
#     return
#   for idx in range(len(elements)):
#     if (lst.count(elements[idx]) == elements.count(elements[idx])):
#       continue
#     else:
#       lst.append(elements[idx])
#       rec(lst, elements, idx)
#   lst.pop()

# for idx in range(len(elements)):
#   lst = [elements[idx]]
#   rec(lst, elements, idx)

# if (min_num == 1000000):
#   min_num = 0
# print(min_num)
