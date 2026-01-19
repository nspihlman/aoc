from math import sqrt

class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.connected = []


def are_connected(p: Point, q: Point):
    return q in p.connected


def connect_points(p: Point, q: Point):
    for point in p.connected:
        if q not in point.connected and q != point:
            point.connected.append(q)
        if point not in q.connected and point != q:
            q.connected.append(point)
    for point in q.connected:
        if p not in point.connected and p != point:
            point.connected.append(p)
        if point not in p.connected and point != p:
            p.connected.append(point)
    p.connected.append(q)
    q.connected.append(p)


def calculate_distance(p: Point, q: Point) -> float:
    return sqrt(pow(p.x - q.x, 2) + pow(p.y - q.y, 2) + pow(p.z - q.z, 2))


def multiply_circuits(points: list[Point]) -> int:
    circ1 = 0
    circ1_mem = []
    circ2 = 0
    circ2_mem = []
    circ3 = 0
    circ3_mem = []
    for p in points:
        if len(p.connected) > circ1 and p not in circ1_mem:
            circ3 = circ2
            circ3_mem = circ2_mem
            circ2 = circ1
            circ2_mem = circ1_mem
            circ1 = len(p.connected)
            circ1_mem = p.connected
        elif len(p.connected) > circ2 and p not in circ2_mem:
            circ3 = circ2
            circ3_mem = circ2_mem
            circ2 = len(p.connected)
            circ2_mem = p.connected
        elif len(p.connected) > circ3 and p not in circ3_mem:
            circ3 = len(p.connected)
            circ3_mem = p.connected
    return circ1 * circ2 * circ3

def main():
    all_points: list[Point] = []
    distances: list[tuple[float, Point, Point]] = []
    with open('tmp.txt') as f:
        for line in f:
            vals = [int(x) for x in line.split(',')]
            all_points.append(Point(vals[0], vals[1], vals[2]))

    for i in range(len(all_points)):
        p = all_points[i]
        for j in range(i+1, len(all_points)):
            q = all_points[j]
            distances.append((calculate_distance(p, q), p, q))
    distances = sorted(distances, key=lambda x: x[0])
    total_ops = 10
    ops_done = 0
    d_place = 0
    while ops_done < total_ops:
        d = distances[ops_done]
        if are_connected(d[1], d[2]) or are_connected(d[2], d[1]):
            ops_done += 1
            continue
        else:
            connect_points(d[1], d[2])
            ops_done += 1
            d_place += 1
    print(multiply_circuits(all_points))


if __name__ == '__main__':
    main()