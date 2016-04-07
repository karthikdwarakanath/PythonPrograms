def isSubString(stringInp, mainString):
    if stringInp in mainString:
        return True
    return False

def main():
    mainString = raw_input("Enter main string : ")
    stringInp = raw_input("Enter substring: ")
    if isSubString(stringInp, mainString):
        print "it is a substring"
    else:
        print "Not a substring"
    return

if __name__ == "__main__":
    main()
