print("Input text to replace name: ")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)
text_input = ' '.join(lines)
words = text_input.split()


i = 0
while i < len(words):
    word = words[i]
    if word.startswith("Подсудимая") or word.startswith("Подсудимый"):
        j = i + 1
        count = 0
        while j < len(words) and count < 3:
            if words[j][0].isupper():
                count += 1
                j += 1
            else:
                break
        words[i + 1:j] = ["N"]
        i = j
    else:
        i += 1
result = ' '.join(words)

print(result)