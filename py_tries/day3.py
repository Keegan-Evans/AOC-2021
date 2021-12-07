def get_gamma(input_values):
    col_values = {}
    for i, col in enumerate(range(len(input_values[0]))):
        col_values[i] = {'0': 0, '1': 0}

        for each in range(len(input_values)):
            row_val = input_values[each][col]
            col_values[i][str(row_val)] += 1

    calculated_gamma = []
    for vals in list(col_values.values()):
        position_value = max(vals, key=vals.get)
        calculated_gamma.append(position_value)

    print("Gamma: %s" % "".join(calculated_gamma))

def get_epsilon(input_values):

    col_values = get_col_vals(input_values)

    calculated_epsilon = []
    for vals in list(col_values.values()):
        position_value = min(vals, key=vals.get)
        calculated_epsilon.append(position_value)

    print("Epsilon: %s" % "".join(calculated_epsilon))

def get_col_vals(input_values):

    col_values = {}
    for i, col in enumerate(range(len(input_values[0]))):
        col_values[i] = {'0': 0, '1': 0}

        for each in range(len(input_values)):
            row_val = input_values[each][col]
            col_values[i][str(row_val)] += 1
    return col_values

def check_position(idx, val):
    def idx_is_val(target):
        return target[idx] == str(val)
    return idx_is_val

# part 2

def get_oxygen(input_values):
    for position in range(len(input_values[0])):
        col_values = get_col_vals(input_values)

        if col_values[position]['0'] == col_values[position]['1']:
            val = '1'
        else:
            val = max(col_values[position],
                      key=col_values[position].get)

            # filter to keep only most common value at current column
        input_values = list(filter(check_position(position, val), input_values))
        # return if down to a single value
        if len(input_values) == 1:
            print("Oxygen: %s" % input_values[0])
            break

def get_co2(input_values):
    for position in range(len(input_values[0])):
        col_values = get_col_vals(input_values)

        if col_values[position]['0'] == col_values[position]['1']:
            val = '0'
        else:
            val = min(col_values[position],
                      key=col_values[position].get)

            # filter to keep only most common value at current column
        input_values = list(filter(check_position(position, val), input_values))
        # return if down to a single value
        if len(input_values) == 1:
            print("CO2: %s" % input_values[0])
            break


if __name__ == '__main__':
    test_data = """00100
                   11110
                   10110
                   10111
                   10101
                   01111
                   00111
                   11100
                   10000
                   11001
                   00010
                   01010""".split("\n")
    test_data = [each.lstrip() for each in test_data]

    print("Test Data:")
    get_gamma(test_data)
    get_epsilon(test_data)
    get_oxygen(test_data)
    get_co2(test_data)

    print("\nReal Data:")
    from daily_data import day3
    day3 = day3.split("\n")

    get_gamma(day3)
    get_epsilon(day3)
    get_oxygen(day3)
    get_co2(day3)

    

    
