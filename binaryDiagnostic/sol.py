with open('input.txt') as f:
    matrix = []
    gamma_rate, epsilon_rate = '', ''
    for line in f.readlines():
        row = []
        for bit in line.replace('\n', ''):
            row.append(bit)
        matrix.append(row)

    num_of_bits = len(matrix[0])
    print(f'number of bits {num_of_bits}')

    count_zero, count_one = 0, 0
    for th_bits in range(num_of_bits):
        for row in matrix:
            if row[th_bits] == '0':
                count_zero += 1
            elif row[th_bits] == '1':
                count_one += 1
            else:
                pass

        gamma_rate += '1' if count_one > count_zero else '0'
        count_zero, count_one = 0, 0 # reset for each row

    print(f'binary value of gammra rate {gamma_rate}')

    count_zero, count_one = 0, 0
    for th_bits in range(num_of_bits):
        for row in matrix:
            if row[th_bits] == '0':
                count_zero += 1
            elif row[th_bits] == '1':
                count_one += 1
            else:
                pass

        epsilon_rate += '1' if count_one < count_zero else '0'
        count_zero, count_one = 0, 0 # reset for each row

    print(f'binary value of epsilon rate {epsilon_rate}')

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
