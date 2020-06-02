"""
"""

def rectangle_area(rectangles):
    N = len(rectangles)

    xVals = sorted({rec[0] for rec in rectangles} | {rec[2] for rec in rectangles})
    yVals = sorted({rec[1] for rec in rectangles} | {rec[3] for rec in rectangles})

    iMapx = {i: x for i, x in enumerate(xVals)}
    jMapy = {j: y for j, y in enumerate(yVals)}

    xMapi = {x: i for i, x in enumerate(xVals)}
    yMapj = {y: j for j, y in enumerate(yVals)}

    area = 0
    grid = [[0 for _ in range(len(xVals))]
            for _ in range(len(yVals))]

    for x1, y1, x2, y2 in rectangles:
        for i in range(xMapi[x1], xMapi[x2]):
            for j in range(yMapj[y1], yMapj[y2]):

                if grid[j][i] == 1: continue
                grid[j][i] = 1

                dx = iMapx[i+1] - iMapx[i]
                dy = jMapy[j+1] - jMapy[j]
                area += dx * dy

    return area


if __name__ == '__main__':
    rectangles = []
    rectangle_area()