import numbers


def addValues(val1, val2):
    # Add any values, handling any conversion from string

    val1_, val2_ = val1, val2
    if not isValidNumber(val1_):
        val1_ = float(val1)

    if not isValidNumber(val2_):
        val2_ = float(val2)

    return val1_ + val2_

def isValidNumber(val):
    valid = True
    if not isinstance(val, numbers.Number):
        #print('Val1 of {} is not a number!'.format(val))
        valid = False

    return valid


print('Welcome to the Simple Calculator')
val1 = input('Value 1:')
val2 = input('Value 2:')
print(addValues(val1, val2))