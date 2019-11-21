def unsafe_calculate_percent(value, total):
    try:
        return value * 100 / total
    except TypeError:
        raise ValueError(f'Invalid values! "{value}" and "{total}" must be a valid number!')
    except ZeroDivisionError:
        raise ValueError(f'Invalid values! "{value}" and "{total}" must be a valid number333!')


def safe_calculate_percent(value, total):
    try:
        percent = unsafe_calculate_percent(value, total)
    except ValueError as error:
        print(error)
    else:
        print(f'{value} from {total} is {percent}%')


safe_calculate_percent(1, 2)
safe_calculate_percent('1', 2)
safe_calculate_percent('a', None)
safe_calculate_percent(28, 0)
safe_calculate_percent(50, 99)
