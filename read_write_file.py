
with open('text1.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('text1.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end="")

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

with open('text1.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="%")
        f_contents = f.read(size_to_read)

with open('text1.txt', 'r') as f:
    # read every line
    for line in f:
        print(line, end='^')

print()

with open('text1.txt') as f:
    f_contents = f.readline()  # read one line at a time
    print(f_contents, end='')
    f_contents = f.readline()  # read next line
    print(f_contents, end='')

print()
with open('text1.txt') as f:
    f_contents = f.readlines()
    print(f_contents)  # read all the lines as an array
