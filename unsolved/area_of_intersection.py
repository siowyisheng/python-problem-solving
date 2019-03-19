# Given two rectangles on a 2D graph, return the area of their intersection. If the
# rectangles don't intersect, return 0.

# For example, given the following rectangles:

# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and

# {
#     "top_left": (0, 5),
#     "dimensions" (4, 3) # width, height
# }

# return 6.

# NOTE: CURRENT CODE IS FAILING


def intersection_area(r1, r2):
    # 4 cases
    results = {}
    r1_points = _points(r1)
    r2_points = _points(r2)
    for point_name, point in r1_points.items():
        results[point_name] = _point_within_rect_range(point, r2)
    # case 1: no points within rect_range
    if results.values().count(True) == 0:
        return 0
    # case 2: 1 point within rect_range
    if results.values().count(True) == 1:
        if results.keys()[results.values().index(True)] == 'top_left':
            # compare with bottom right of r2
            return (
                r2_points['bottom_right'][0] - r1_points['top_left'][0]) * (
                    r1_points['top_left'][1] - r2_points['bottom_right'][1])
    # case 3: 2 points within rect_range
    if results.values().count(True) == 2:
        results.index(True)
    # case 4: 4 points within rect_range
    return r1['dimensions'][0] * r2['dimensions'][1]


def _point_within_rect_range(point, r):
    rect_leftmost_point = r['top_left'][0]
    rect_rightmost_point = r['top_left'][0] + r['dimensions'][0]
    rect_topmost_point = r['top_left'][1]
    rect_bottommost_point = r['top_left'][1] + r['dimensions'][1]
    if (rect_leftmost_point < point[0] < rect_rightmost_point) and (
            rect_topmost_point < point[1] < rect_bottommost_point):
        return True
    return False


def _points(r):
    return {
        'top_left': r['top_left'],
        'top_right': (r['top_left'][0] + r['dimensions'][0], r['top_left'][1]),
        'bottom_left': (r['top_left'][0],
                        r['top_left'][1] + r['dimensions'][1]),
        'bottom_right': (r['top_left'][0] + r['dimensions'][0],
                         r['top_left'][1] + r['dimensions'][1])
    }