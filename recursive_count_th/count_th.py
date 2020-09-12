'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case: if a word is < 2 return 0
    # Will not count capitalized TH
    # Go through each of the letters (two at a time)
    # Looking for 'th'
    # if one is found, add to the count

    if len(word) < 2:
        return 0
    elif word[:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
    
    pass


print(count_th(""))
print(count_th("ththth"))
print(count_th("THTHTHthththththTHTHTH"))