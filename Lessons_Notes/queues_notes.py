import time
from datetime import datetime, timedelta
from collections import deque

deque_of_nums = deque([0, 1, 2, 3])
print(deque_of_nums[2])

x_time = "8:00:00"
line_time = datetime.strptime(x_time, "%H:%M:%S")
details = [x for x in range(10)]
while details:
    line_time += timedelta(0, 1)
    print(line_time)
    details.pop()

# list_test = [x for x in range(100000000)]
# list_test_copy = list_test.copy()
# queue = deque(list_test)
#
start_time = time.time()
# while queue:
#     queue.popleft()
#
# diff = time.time() - start_time
# print(diff)
#
# start_time = time.time()
# while list_test:
#     list_test.pop()
#
# diff = time.time() - start_time
# print(f"list-{diff}")


# start_time = time.time()
# while list_test_copy:
#     list_test_copy.pop(0)
#
# diff = time.time() - start_time
# print(diff)

# start_time = time.time()
# max_num = max(queue)
# diff = time.time() - start_time
# print(diff)
#
# start_time = time.time()
# max_num1 = max(list_test)
# diff = time.time() - start_time
# print(f"list - {diff}")
#
# print(max_num)
# print(max_num1)


