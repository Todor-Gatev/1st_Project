text = "1344 4219 087 8969 34875 6695 09856 9866 356 " \
       "9800 145- 135 7990 8782 6597 8453 4599 " \
       "1344 4219 087 8969 34875 6695 09856 9866 356 " \
       "9800 145- 135 7990 8782 6597 8453 4599"

test = input()
errors = 0

for idx in range(len(text)):
    if test[idx] != text[idx]:
        errors += 1
        print(f"{test[idx]} != {text[idx]}")

print(f"errors = {errors}\nchars = {len(text)}")
