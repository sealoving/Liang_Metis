# make sure to pip install fiona and pip install shapely

import fiona
from shapely import geometry

def shaper():
    shapes = []
    points = []
    d = []
    with fiona.open("data/nyu_2451_34513.shp") as fiona_collection:
    
        #put all shapes in list
        for record in fiona_collection:
            shape = geometry.asShape( record['geometry'] )
            shapes.append(shape)
    
    with open('data/DOITT_SUBWAY_STATION_01_13SEPT2010.csv','r') as f:

        for index, line in enumerate(f):
            if index > 0:
                split_line = line.split(",")
                m  = tuple(map(float, split_line[3][7:-1].split()))#[::-1]
                point = geometry.Point(m) #lon, lat
                points.append(point)

    
    for s in shapes:
        for p in points:
            d.append([s,[]])
            if s.contains(p):
                d[-1][1].append(p)
    

    for x in d:
        print(x)
    
    #print(shapes)
    #print(points)
    return d


if __name__ == "__main__":
    shaper()

