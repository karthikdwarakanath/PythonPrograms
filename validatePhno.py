import re

def validatePh(phnoList):
    for no in phnoList:
        match = re.search(r'[789]\d\d\d\d\d\d\d',no)
        if match:
            print 'YES'
        else:
            print 'NO'
    return

def main():
    noPhs = raw_input()
    phList = []
    for i in range(0, noPhs):
        phList.append(raw_input())
    validatePh(phList)
    return

if __name__=='__main__':
    main()
