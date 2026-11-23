# Planar Euclidean distance, with coordinates in kilometres.
def analyse(points):
    if len(points) < 2:
        print('At least two points required')
        return
    maximum = -1
    longest = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print('Segment', i + 1, ':', round(distance, 2), 'km')
        if distance > maximum:
            maximum, longest = distance, i + 1
    print('Longest segment:', longest, 'distance:', round(maximum, 2), 'km')

analyse([(0, 0), (3, 4), (3, 16)])
analyse([(0, 0)])
