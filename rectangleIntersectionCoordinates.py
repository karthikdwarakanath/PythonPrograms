#rect1 = {'left_x': 1,
#    ''bottom_y'': 5,
#
#    # width and height
#    'width': 10,
#    'height': 4,
#}
#logic:
#max of the bottom left x of both rects should be <= min of top right x of both rects
#max of right top y should be <= min of left bottom y
def findCoordinates(rect1, rect2):
    resultRect = {}
    if max(rect1['left_x'], rect2['left_x']) > min((rect1['left_x'] + rect1['width']), (rect2['left_x'] + rect2['width'])):
        return {}
    if max(rect1['bottom_y'], rect2['bottom_y']) > min((rect1['bottom_y'] + rect1['height']), (rect2['bottom_y'] + rect2['height'])):
        return {}
    resultRect['left_x'] = max(rect1['left_x'], rect2['left_x'])
    resultRect['bottom_y'] = max(rect1['bottom_y'], rect2['bottom_y'])
    resultRect['width'] = min(rect1['left_x'] + rect1['width'], rect2['left_x'] + rect2['width']) - max(rect1['left_x'], rect2['left_x'])
    resultRect['height'] = min(rect1['bottom_y'] + rect1['height'], rect2['bottom_y'] + rect2['height']) - max(rect1['bottom_y'], rect2['bottom_y'])
    return resultRect

rect1 = {'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,
}
rect2 = {'left_x': 11,
    'bottom_y': 5,

    # width and height
    'width': 5,
    'height': 4,
}
print findCoordinates(rect1, rect2)
