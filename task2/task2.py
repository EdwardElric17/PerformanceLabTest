file1 = str(input())
file2 = str(input())
coordinates_center = list()
coordinates = list()

with open(file1, 'r') as inf1:
    elem = inf1.readline()
    coordinates_center = elem.split()
    x0 = float(coordinates_center[0])
    y0 = float(coordinates_center[1])
    elem = inf1.readline()
    radius = int(elem)

with open(file2, 'r') as inf2:
    for line in inf2:
        coordinates = line.split()
        x = float(coordinates[0])
        y = float(coordinates[1])
        if (((x - x0)**2) + ((y - y0)**2)) == radius**2:
            print(0)
        elif (((x - x0)**2) + ((y - y0)**2)) < radius**2:
            print(1)
        elif (((x - x0)**2) + ((y - y0)**2)) > radius**2:
            print(2)