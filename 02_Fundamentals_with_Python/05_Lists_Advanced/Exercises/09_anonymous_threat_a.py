strings_lst = input().split()
command = input()

while command != "3:1":
    temp_lst = []
    action, start, end_info = command.split()
    start_idx = int(start)

    if start_idx > len(strings_lst) - 1:
        command = input()
        continue

    if action == "merge":
        end_idx = int(end_info)
        new_el = ""

        # if end_idx > len(strings_lst) - 1:
        #     end_idx = len(strings_lst) - 1
        # end_idx = min(len(strings_lst) - 1, end_idx)

        for idx in range(len(strings_lst) - 1, -1, -1):
            if start_idx <= idx <= end_idx:
                new_el = strings_lst[idx] + new_el
                strings_lst.pop(idx)
                if idx == max(start_idx, 0):
                    strings_lst.insert(idx, new_el)

        # for idx in range(len(strings_lst)):
        #     if start_idx <= idx <= end_idx:
        #         new_el += strings_lst[idx]
        #     else:
        #         temp_lst.append(strings_lst[idx])
        #
        #     if idx == end_idx:
        #         temp_lst.append(new_el)
        #
        # strings_lst = temp_lst.copy()
    elif action == "divide":
        index = int(start)
        partitions = int(end_info)

        if partitions == 0:
            command = input()
            continue

        str_for_dividing = strings_lst[index]
        strings_lst.pop(index)
        new_el_len = len(str_for_dividing) // partitions
        for j in range(partitions):
            start = j * new_el_len
            end_new = start + new_el_len

            if j == partitions - 1:
                new_el = str_for_dividing[start:]
            else:
                new_el = str_for_dividing[start:end_new]

            strings_lst.insert(index, new_el)
            index += 1

    command = input()

print(' '.join(strings_lst))
