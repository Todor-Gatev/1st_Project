import time

# region Diff = End_time - Start_time
start_time = time.time()
test_list = [x for x in range(100000)]
while test_list:
    test_list.pop()
diff = time.time() - start_time
print(diff)
start_time = time.time()
test_list = [x for x in range(100000)]
while test_list:
    test_list.pop(0)
diff = time.time() - start_time
print(diff)
# endregion

