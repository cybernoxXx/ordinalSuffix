def ordinalSuffix(number):
    suffix = str(number)

    # I have to check the last two digit to be sure to add the right suffix (213 is 213st not 213rd)
    if str(number)[-2:] == "11" or str(number)[-2:] == "12" or str(number)[-2:] == "13":
        suffix = suffix + "th"
    elif str(number)[-1:] == "1":
        suffix = suffix + "st"
    elif str(number)[-1:] == "2":
        suffix = suffix + "nd"
    elif str(number)[-1:] == "3":
        suffix = suffix + "rd"
    else:
        suffix = suffix + "th"

    return suffix

assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
assert ordinalSuffix(213) == '213th'
