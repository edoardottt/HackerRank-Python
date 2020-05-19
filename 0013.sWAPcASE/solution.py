def swap_case(s):
    result = ''
    for char in s:
        if char==char.lower():
            result += char.upper()
        else:
            result+= char.lower()
    return result