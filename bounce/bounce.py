import sys

def bounce(start, bounces):
    """Determine the distance a ball travels after number of bounces.
    cum: cumulator
    back: return units
    start: starting height
    bounces: number of bounces to calculate"""
    cum = 0; back = 0; start = float(start);

    for i in range(bounces):
        cum += start
        back = .6 * start
        cum += back
        start = back

    return cum


if __name__ == '__main__':
    height, bounces = float(sys.argv[1]), int(sys.argv[2])

    print(f"The distance traveled from height {height}, bouncing {bounces} times is")
