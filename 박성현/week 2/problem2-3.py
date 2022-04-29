word = input(str())
word = word.upper()

count = {}
a = list(word)
for i in a:
    try: count[i] += 1
    except: count[i] =1

answer = [k for k, v in count.items() if max(count.values()) == v]
if len(answer) > 1:
    print("?")
else:
    print(''.join(str(s) for s in answer))
