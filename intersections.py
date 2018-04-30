'''
Software Design Final Project: Trail Blazer

Intersections.py takes a bounding area, finds all of the paths in that area, and designates the parts of those paths as nodes and edges.
'''
import overpy
import geopy
from geopy.distance import VincentyDistance, vincenty
import geographiclib
from geographiclib.geodesic import Geodesic
import folium
import matplotlib.pyplot as plt
import mplleaflet
from edge import Edge
from graph import Graph

def get_nearest_node(api, lat, lng):
    G = Graph(api, lat, lng, 0.0015)
    G.get_ways_in_area()
    G.get_vertices()
    G.get_intersections()

    position = (lat, lng)
    first_try = (G.intersections[0].lat, G.intersections[0].lon)
    closest = [G.intersections[0], vincenty(first_try, position).km]
    for i in range(1, len(G.intersections)):
        coord = (G.intersections[i].lat, G.intersections[i].lon)
        distance = vincenty(coord, position).km
        if distance < closest[1]:
            closest[0] = G.intersections[i]
            closest[1] = distance
    return closest[0]

def graph_it(api, lat, lng, radius):
    start = get_nearest_node(api, lat, lng)
    G2 = Graph(api, lat, lng, radius)
    return G2.show_route(start)

if __name__ == "__main__":
    api = overpy.Overpass()
    graph_it(api, 42.292922, -71.263073, 0.04)
