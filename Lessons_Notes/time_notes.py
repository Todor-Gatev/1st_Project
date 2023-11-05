# region datetime timedelta, strptime, strftime

# from datetime import datetime, timedelta
#
# # input_time = "8:00:00"
# input_time = "2023:8:00:00:17"  # Month is omitted
# current_time = datetime.strptime(input_time, "%Y:%H:%M:%S:%d")
# current_time += timedelta(seconds=7)
# # class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# print(current_time.strftime("p[%H:%M:%S{q"))  # p[08:00:07-{q
# print(current_time.strftime("%H:%M:%S-(%d/%Y)"))  # 08:00:07--(17/2023) - Month is omitted

# endregion

# region Diff = End_time - Start_time

import time

start_time = time.time()
# test_list = [x for x in range(100000)]
test_list = list(range(100000))
while test_list:
    test_list.pop()
diff = time.time() - start_time
print(diff)
start_time = time.time()
# test_list = [x for x in range(100000)]
test_list = list(range(100000))
while test_list:
    test_list.pop(0)
diff = time.time() - start_time
print(diff)

# endregion

