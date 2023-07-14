# ch_list = list(input())
text = input()

parentheses = []

for idx in range(len(text)):
    if text[idx] == '(':
        parentheses.append(idx)
    elif text[idx] == ')':
        start_idx = parentheses.pop()
        end_idx = idx + 1
        print(text[start_idx:end_idx])
