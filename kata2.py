'''


'''

def test_chop():
  assert (-1 == chop(3, []))
  assert (-1 == chop(3, [1]))
  assert (0 == chop(1, [1]))
  #
  assert (0 == chop(1, [1, 3, 5]))
  assert (1 == chop(3, [1, 3, 5]))
  assert (2 == chop(5, [1, 3, 5]))
  assert (-1 == chop(0, [1, 3, 5]))
  assert (-1 == chop(2, [1, 3, 5]))
  assert (-1 == chop(4, [1, 3, 5]))
  assert (-1 == chop(6, [1, 3, 5]))
  #
  assert (0 == chop(1, [1, 3, 5, 7]))
  assert (1 == chop(3, [1, 3, 5, 7]))
  assert (2 == chop(5, [1, 3, 5, 7]))
  assert (3 == chop(7, [1, 3, 5, 7]))
  assert (-1 == chop(0, [1, 3, 5, 7]))
  assert (-1 == chop(2, [1, 3, 5, 7]))
  assert (-1 == chop(4, [1, 3, 5, 7]))
  assert (-1 == chop(6, [1, 3, 5, 7]))
  assert (-1 == chop(8, [1, 3, 5, 7]))

def chop(num, arrs):
    if len(arrs) == 0:
        return -1
    if num > arrs[len(arrs)-1] or num < arrs[0]:
        return -1
    left = 0
    right = len(arrs) - 1
    mid = int(left / 2 + right / 2)
    while left < right:
        if num == arrs[mid]:
            return mid
        if num < arrs[mid]:
            right = mid
        else:
            left = mid + 1
        mid = ((left + right )/ 2)
    if num == arrs[mid]:
        return mid
    return -1

def main():
    test_chop()

if __name__ == '__main__':
    main()


'''
Errors:
No element in array
1 element in array and it is the key
check if num equals mid before calculating the next mid
Loop termination clause
calculation of mid
'''
