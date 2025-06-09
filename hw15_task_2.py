def infinite_generator(sequence):
    while True:
        for n in sequence:
            yield n


count = int(input('How many numbers do you want to generate?'))
sequence = [1, 2, 3]
generated = infinite_generator(sequence)
for _ in range(count):
    print(next(generated), end=' ')
