a = [1, 11, 21, 1211, 111221]

for i in range(30):

    #next_num_list = []
    next_num = ''

    next_char = ''

    step = 0
    count = 0

    # Analyze the string.
    for char in str(a[i+4]):
        if step == 0:
            next_char = char
            count += 1
            step = 1

        elif step == 1:
            if next_char != char:
                next_num += str(count) + str(next_char)

                next_char = char
                count = 1

            else:
                count += 1

    next_num += str(count) + str(next_char)

    a.append(int(next_num))

print len(str(a[30]))
