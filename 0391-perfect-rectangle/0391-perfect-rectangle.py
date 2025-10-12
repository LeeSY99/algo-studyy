class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = float('inf')
        min_y = float('inf')
        max_x = 0
        max_y = 0
        sub_rec_area = 0
        points = set()

        for x1,y1, x2,y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            sub_rec_area += (x2-x1) * (y2-y1)

            if (x1,y1) not in points:
                points.add((x1,y1))
            else:
                points.remove((x1,y1))

            if (x2,y1) not in points:
                points.add((x2,y1))
            else:
                points.remove((x2,y1))

            if (x1,y2) not in points:
                points.add((x1,y2))
            else:
                points.remove((x1,y2))

            if (x2,y2) not in points:
                points.add((x2,y2))
            else:
                points.remove((x2,y2))
        
        print(points)
        print(min_x, max_x, min_y, max_y)
        if len(points) != 4:
            return False
        expected = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        }
        if points != expected:
            return False
        return (max_x - min_x) * (max_y - min_y) == sub_rec_area