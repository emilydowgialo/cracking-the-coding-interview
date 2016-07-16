# 1.3 URLify
def urlify(string, length):

    new = len(string)
    string = list(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new - 3:new] = '%20'
            new -= 3

        else:
            string[new - 1] = string[i]
            new -= 1

    return ''.join(string)


l = urlify('Mr John Smith    ', 13)
print l
