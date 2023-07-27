# 9093
# T = int(input())

# for i in range(T):
#     lst = list(input().split())
#     for word in lst:
#         print(word[::-1], end=" ")

# 9012

# T = int(input())


# for i in range(T):
#     cnt = 0
#     vps = input()
#     for bracket in vps:
#         if bracket == "(":
#             cnt += 1
#         elif bracket == ")":
#             cnt -= 1
#         if cnt < 0:
#             break
#     if cnt == 0:
#         print("YES")
#     else:
#         print("NO")

# 1158
# n, k = map(int, input().split())
# p_lst = [i for i in range(1, n + 1)]
# a_lst = []
# num = 0
# for i in range(n):
#     num += k - 1
#     num = num % len(p_lst)
#     a_lst.append(str(p_lst.pop(num)))

# print("<", ", ".join(a_lst), ">", sep="")
