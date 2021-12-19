with open('input.txt') as f:
    matrix = []
    oxygen_rating, co2_rating = [], []

    for line in f.readlines():
        row = []
        for bit in line.replace('\n', ''):
            row.append(bit)
        matrix.append(row)

    num_of_bits = len(matrix[0])
    count_zero, count_one = 0, 0

    # populate values for the first bit
    for row in matrix:
        if row[0] == '1':
            count_one += 1
        elif row[0] == '0':
            count_zero += 1
        else:
            pass
    compare_with = '1' if count_one >= count_zero else '0'

    for row_num in range(len(matrix)):
        if matrix[row_num][0] == compare_with:
            oxygen_rating.append(row_num)

    # populate values for other bits in the input starting from 1
    for th_bit in range(1, num_of_bits):
        count_zero, count_one = 0, 0

        if len(oxygen_rating) == 1: # base condition
            break

        for row_num in oxygen_rating:
            if matrix[row_num][th_bit] == '1':
                count_one += 1
            elif matrix[row_num][th_bit] == '0':
                count_zero += 1
            else:
                pass

        compare_with = '1' if count_one >= count_zero else '0'

        new_arr = []
        for row_num in oxygen_rating:
            if matrix[row_num][th_bit] == compare_with:
                new_arr.append(row_num)
        oxygen_rating = new_arr

    #######################
    # co2 calc
    #######################

    count_zero, count_one = 0, 0

    # populate values for the first bit
    for row in matrix:
        if row[0] == '1':
            count_one += 1
        elif row[0] == '0':
            count_zero += 1
        else:
            pass
    compare_with = '0' if count_zero <= count_one else '1'

    for row_num in range(len(matrix)):
        if matrix[row_num][0] == compare_with:
            co2_rating.append(row_num)

    # populate values for other bits in the input starting from 1
    for th_bit in range(1, num_of_bits):
        count_zero, count_one = 0, 0

        if len(co2_rating) == 1: # base condition
            break

        for row_num in co2_rating:
            if matrix[row_num][th_bit] == '1':
                count_one += 1
            elif matrix[row_num][th_bit] == '0':
                count_zero += 1
            else:
                pass

        compare_with = '0' if count_zero <= count_one else '1'

        new_arr = []
        for row_num in co2_rating:
            if matrix[row_num][th_bit] == compare_with:
                new_arr.append(row_num)
        co2_rating = new_arr

    ##################
    # decimal values
    ##################
    oxygen_value = int(''.join(matrix[oxygen_rating[0]]), 2)
    co2_value = int(''.join(matrix[co2_rating[0]]), 2)
    print(oxygen_value * co2_value)
