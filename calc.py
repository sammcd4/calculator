import numbers


def add_values(val1, val2):
    # Add any values, handling any conversion from string

    val1_, val2_ = val1, val2
    if not is_valid_number(val1_):
        val1_ = float(val1)

    if not is_valid_number(val2_):
        val2_ = float(val2)

    return val1_ + val2_

def is_valid_number(val):
    valid = True
    if not isinstance(val, numbers.Number):
        #print('Val1 of {} is not a number!'.format(val))
        valid = False

    return valid