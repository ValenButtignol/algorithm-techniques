import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return "(" + str(self.x) + " ," + str(self.y) + ")"


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))


#Closest pair of points.
def closest_pair_of_points(points):
    px = sorted(points, key=lambda x: x.x)
    py = sorted(points, key=lambda x: x.y)
    return closest_pair(px, py)

def closest_pair(px, py):
    length_px = len(px)
    if length_px <= 3:
        return brute(px) 
    
    mid = length_px // 2
    qx = px[mid:]
    rx = px[:mid]
    
    # Determine midpoint on x-axis
    midpoint = px[mid].x
    qy = list()
    ry = list()
    for p in py:  # split ay into 2 arrays using midpoint
        if p.x <= midpoint:
           qy.append(p)
        else:
           ry.append(p)
    
    
    # Determine qx, qy, rx, ry from px and py
    p1 = closest_pair(qx, qy)
    p2 = closest_pair(rx, ry)
    
    best = p2
    delta = dist(p2[0], p2[1])
    if dist(p1[0], p1[1]) < delta:
        best = p1
        delta = dist(p1[0], p1[1])
    
    p3 = closest_split_pair(px, py, delta)  # Must be linear, and its like merge.
    
    return p3 if p3 and dist(best[0], best[1]) > dist(p3[0], p3[1]) else best



def brute(points):
    length = len(points)
    closest = []
    min_delta = math.inf
    for i in range(length):
        for j in range(i+1, length):
            if dist(points[i], points[j]) < min_delta:
                closest = [points[i], points[j]]
                min_delta = dist(points[i], points[j])
                
    return closest


def closest_split_pair(px, py, delta):
    length = len(px)
    midpoint = px[length // 2].x  # select midpoint on x-sorted array   
    # Create a subarray of points not further than delta from midpoint on x-sorted array    
    s_y = [p for p in py if midpoint - delta <= p.x <= midpoint + delta]
    
    ln_y = len(s_y)
    closest_split = None
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < delta:
                closest_split = [p, q]
                
    return closest_split