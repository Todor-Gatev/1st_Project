from collections import deque

expression = deque(input().split())
nums = deque()

while expression:
    el = expression.popleft()
    if el not in "*-+/":
        nums.append(int(el))
    else:
        num = nums.popleft()
        if el == '*':
            while nums:
                num *= nums.popleft()

            nums.append(num)
        elif el == '/':
            while nums:
                num /= nums.popleft()

            num = int(num)
            nums.append(num)
        elif el == '+':
            while nums:
                num += nums.popleft()

            nums.append(num)
        elif el == '-':
            while nums:
                num -= nums.popleft()

            nums.append(num)

print(nums.popleft())
