n, m = list(map(int, input().split()))

# n_set = set()
# m_set = set()

# for _ in range(n):
#     n_set.add(input())
#
# for _ in range(m):
#     m_set.add(input())

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

# intersection_set = n_set.intersection(m_set)
# print(*intersection_set, sep='\n')
# n_set.intersection_update(m_set)
# print(*n_set, sep='\n')
print(*(n_set & m_set), sep='\n')
