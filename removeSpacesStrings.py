# Remove extra spaces from a string
# Given a string containing many consecutive spaces, trim all spaces so that all
# words should contain only a single space between them. The conversion should be
#  done in-place and solution should handle trailing and leading spaces and also
# remove preceding spaces before common punctuation like full stop, comma and a
# question mark.
#

def removeExtraSpaces(inputString):
    n = len(inputString)
    i = 0
    j = 0
    spaceFound = False
    #Take out leading spaces
    while inputString[j] == ' ':
        j = j+1
    while j < n:
        if inputString[j] != ' ':
            inputString[i] = inputString[j]
            i = i+1
            j = j+1
            spaceFound = False
        else:
            if not spaceFound:
                spaceFound = True
                j = j+1
                inputString[i] = inputString[j]
            else:
                j = j+1
    return inputString

print removeExtraSpaces('   Hello Geeks . Welcome   to  GeeksforGeeks   .    ')
