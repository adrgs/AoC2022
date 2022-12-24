import re

def md(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

# given a point, the manhatten distance and y, find the two x coordinates of the other point
def find_x(sensor, distance, y):
    r = distance - abs(sensor[1] - y)
    return (sensor[0] - r, sensor[0] + r)

def solve(lines):
    r = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    sensors = []
    min_x, max_x = float('inf'), float('-inf')
    y = 2000000
    ans = 0

    subtracted = set()

    for line in lines:
        line = line.strip()
        if line:
            m = r.match(line)
            groups = m.groups()
            sensor = (int(groups[0]), int(groups[1]))
            min_x = min(min_x, sensor[0])
            max_x = max(max_x, sensor[0])
            beacon = (int(groups[2]), int(groups[3]))
            if sensor not in subtracted and sensor[1] == y:
                ans -= 1
                subtracted.add(sensor)
            if beacon not in subtracted and beacon[1] == y:
                ans -= 1
                subtracted.add(beacon)

            sensors.append((sensor, md(sensor, beacon)))

    intervals = []

    for sensor_dist in sensors:
        sensor, dist = sensor_dist
        x1, x2 = find_x(sensor, dist, y)
        if md((x1, y), sensor) > dist:
            continue
        
        intervals.append((x1, x2))

    intervals.sort()
    # merge intervals
    i = 0

    while i < len(intervals)-1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i] = (intervals[i][0], max(intervals[i][1], intervals[i+1][1]))
            intervals.pop(i+1)
        else:
            i += 1

    for interval in intervals:
        ans += interval[1] - interval[0] + 1
    
    print(ans)


def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()