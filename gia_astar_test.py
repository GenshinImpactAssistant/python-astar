import astar, math

class GenshinNavigationPoint():
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.links = []

NAVIGATION_POINTS = {}
ps = {
    '1':{
        "position":[0,0],
        "links":['2']
    },
    '2':{
        "position":[10,10],
        "links":['3']
    },
    '3':{
        "position":[20,20],
        "links":['4','6']
    },
    '4':{
        "position":[30,30],
        "links":['5']
    },
    '5':{
        "position":[10,40],
        "links":['1']
    },
    '6':{
        "position":[40,10],
        "links":['1','5']
    },
}

def build_navigation_points(ps:dict):
    for i in ps:
        inti = int(i)
        NAVIGATION_POINTS[i] = GenshinNavigationPoint(i, position=ps[i]['position'])
    for i in NAVIGATION_POINTS:
        for ii in ps[i]['links']:
            NAVIGATION_POINTS[i].links.append(NAVIGATION_POINTS[ii])
    return NAVIGATION_POINTS

def get_path(n1, n2):
    def distance(n1, n2):
        """computes the distance between two stations"""
        latA, longA = n1.position
        latB, longB = n2.position
        # convert degres to radians!!
        latA, latB, longA, longB = map(
            lambda d: d * math.pi / 180, (latA, latB, longA, longB))
        x = (longB - longA) * math.cos((latA + latB) / 2)
        y = latB - latA
        return math.hypot(x, y)
    return astar.find_path(n1, n2, neighbors_fnct=lambda s: s.links, heuristic_cost_estimate_fnct=distance, distance_between_fnct=distance)
build_navigation_points(ps)
print([f"{i.id}" for i in get_path(NAVIGATION_POINTS['1'], NAVIGATION_POINTS['5'])])
print()


