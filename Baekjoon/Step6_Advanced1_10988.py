word = input()

if len(word) == 1:
    print(1)
else:
    for i in range(1, len(word)//2 + 1):
        if word[i-1] != word[-i]:
            print(0)
            break
    else:
        print(1)
