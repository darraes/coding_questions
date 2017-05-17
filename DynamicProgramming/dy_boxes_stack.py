# Craking the Code Interview - Dynamic Programming
# http://www.careercup.com/question?id=5712696989188096

class Box:
    def __init__(self, width, height, depth):
        self._width = width
        self._height = height
        self._depth = depth

    def __eq__(self, other):
        if type(other) is type(self):
            return self._width == other._width and self._height == other._height and self._depth == other._depth
        return False

    def __str__(self):
        return "W {} H {} D {}".format(self._width, self._height, self._depth)

    def __hash__(self):
        return hash((self._width, self._height, self._depth))

    def is_allowed_above(self, bottom):
        if bottom is None: 
            return True
        if self == bottom: 
            return False
        return self._width <= bottom._width \
            and self._height <= bottom._height \
            and self._depth <= bottom._depth

    def create_rotations(self):
        return [self, \
                Box(self._width, self._depth, self._height),\
                Box(self._depth, self._height, self._width),\
                Box(self._depth, self._width, self._height),\
                Box(self._height, self._width, self._depth),\
                Box(self._height, self._depth, self._width),\
                ]


def calculate_height(boxes):
    sum = 0
    for box in boxes:   
        sum += box._height
    return sum


def max_stack(boxes, bottom, cache, in_use):
    if boxes is None or cache is None: raise

    if bottom is not None and cache.has_key(bottom):
        return cache[bottom]
             
    max_st = []
    for i in range(len(boxes)):
        if not in_use[i]:
            box = boxes[i]
            in_use[i] = True

            # Rotates for all dimensions (They all can be the height)
            rotations = box.create_rotations() 
            for box_rotation in rotations:
                if box_rotation.is_allowed_above(bottom):
                    
                    max_sub = max_stack(boxes, box_rotation, cache, in_use)

                    # Since we have all possible rotations, we can assume that
                    # the height will always be placed on the same index (considering
                    # an array as dimensions)
                    if calculate_height(max_sub) > calculate_height(max_st):
                        max_st = []
                        max_st.extend(max_sub)

            in_use[i] = False

    if bottom is not None:
        max_st.append(bottom)

    cache[bottom] = max_st
    return max_st


boxes = [Box(3, 3, 3), Box(2, 2, 4), Box(4, 4, 4), Box(5, 5, 3), Box(9, 9, 9), Box(7, 7, 7), Box(8, 8, 8)]
for b in max_stack(boxes, None, dict(), [0]*len(boxes)):
    print b

    