from distance_meter_1 import Point


class DistanceMeterException(Exception):
    pass


class DistanceMeter:
    def __init__(self):
        self.points = []

    def add(self, other: Point):
        if not isinstance(other, Point):
            raise DistanceMeterException("Wrong argument: should be Point type")
        self.points.append(other)

    def measure(self):
        result = 0
        if len(self.points) < 1:
            raise DistanceMeterException("No Points to measure")
        elif len(self.points) == 1:
            return result
        else:
            for i in range(len(self.points) - 1):
                result += self.points[i].distance_to(self.points[i + 1])
            return result

    def __str__(self):
        out = 'Points: '
        for i in self.points:
            out += '(' + str(i.x) + ',' + str(i.y) + ') '
        return out


if __name__ == '__main__':

    # FOR TESTS

    p1 = Point(0, 0)
    p2 = Point(0, 1)

    meter = DistanceMeter()
    meter.add(p1)
    meter.add(p2)
    meter.add(Point(2, 0))
    # print(p2.distance_to(Point(2, 0)))
    print(meter)  # >>> Points: (0,0) (0,1) (2,0)
    print(meter.measure())  # >>> 3.23606797749979
