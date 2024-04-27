def ordinalSuffix(number):
    numberList = list(str(number))
    suffix = str(number)

    if number >=4 and  number <=19:
        suffix = suffix + "th"
    elif numberList[-1] == "0":
        suffix = suffix + "th"
    elif numberList[-1] == "1":
        suffix = suffix + "st"
    elif numberList[-1] == "2":
        suffix = suffix + "nd"
    elif numberList[-1] == "3":
        suffix = suffix + "rd"

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
