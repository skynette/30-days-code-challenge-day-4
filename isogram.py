def is_isogram(string):
    for i in string:
        if i == " " or i == "-": continue
        elif string.lower().count(i)>1:
            return False
    return True