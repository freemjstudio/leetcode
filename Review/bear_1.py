import string


def StringChallenge(strParam):
    # condition 5
    if not (7 < len(strParam) < 31):
        return "false"

    # condition 1 - capital letter & condition 2 - at least one number & condition 3
    check_digit, check_upper, check_symbol = False, False, False
    symbols = string.punctuation

    for i in strParam:
        if i.isdigit():
            check_digit = True
            continue
        if i.isupper():
            check_upper = True
            continue
        if i in symbols:
            check_symbol = True
    if check_digit == False or check_upper == False or check_symbol == False:
        return "false"

    # condition 4
    if "password" in strParam.lower():
        return "false"

    return "true"


# keep this function call here
print(StringChallenge(input()))