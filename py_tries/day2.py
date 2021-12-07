sub_iter = ['forward', 3, 'up', 2, 'forward', 1, 'down', 13]

def get_directions(directions):
    distance = 0
    depth = 0
    sub_iter = iter(directions)

    while sub_iter:
        try:
            direction, value = next(sub_iter), next(sub_iter)
        except:
            break

        match direction:
            case 'forward' :
                distance += int(value)
            case 'down' :
                depth += int(value)
            case 'up' :
                depth -= int(value)
    return (distance, depth)

def get_aim(directions):
    distance = 0
    depth = 0
    aim = 0
    sub_iter = iter(directions)

    while sub_iter:
        try:
            direction, value = next(sub_iter), next(sub_iter)
        except:
            break

        match direction:
            case 'forward' :
                distance += int(value)
                depth += aim * int(value)
            case 'down' :
                aim += int(value)
            case 'up' :
                aim -= int(value)
    return (distance, depth)


if __name__ == '__main__':

    from daily_data import day2
    import re

    data_list = re.split(r'\n|\s', day2)
    a, b = get_directions(data_list)


    print("%s, %s" % (a, b))

    c, d = get_aim(data_list)
    print("%s, %s" % (c, d))
    print(c * d)
