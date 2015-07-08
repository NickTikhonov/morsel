
from entities import Vector
import itertools
import scipy.spatial as spatial
import numpy as np
import networkx as nx

from google.apputils import app
from ortools.constraint_solver import pywrapcp
import random


class Path:
    """
    Abstracts over finding the shortest path between N Vector objects

    'complexity' - defines how much to improve the tour once it has
        been calculated using a greedy algorithm
    """

    def __init__(self, samples, start=None, complexity=0):
        self.samples = samples
        greedy_tour = Pathfinder.slow_greedy_path(samples, start)
        self.tour = Pathfinder.improve_tour(
            greedy_tour, num_fails=len(greedy_tour) * 4)
        self.length = Pathfinder.length(self.tour)


class Pathfinder:

    @staticmethod
    def get_array(vec_list):
        array = np.zeros((len(vec_list), 2))
        for i, vec in enumerate(vec_list):
            array[i][0] = vec.x
            array[i][1] = vec.y
        return array

    @staticmethod
    def get_nn_roadmap(vec_list, k):
        data = Pathfinder.get_array(vec_list)
        tree = spatial.KDTree(data)
        G = nx.Graph()
        for i, vec in enumerate(data):
            ds, inds = tree.query(vec, k=k)
            for d, j in zip(ds, inds):
                G.add_edge(i, j, weight=d)
        return G

    @staticmethod
    def get_distance_func(vec_list):
        def __inner(from_node, to_node):
            return Vector.distance(vec_list[from_node], vec_list[to_node])
        return __inner

    @staticmethod
    def tsp_path(vec_list):
        param = pywrapcp.RoutingParameters()
        param.use_light_propagation = False
        pywrapcp.RoutingModel.SetGlobalParameters(param)
        routing = pywrapcp.RoutingModel(len(vec_list), 1)
        parameters = pywrapcp.RoutingSearchParameters()
        # parameters.first_solution = 'Savings'
        parameters.no_lns = False
        parameters.no_tsp = False
        parameters.no_tsplns = True
        func = Pathfinder.get_distance_func(vec_list)
        routing.SetArcCostEvaluatorOfAllVehicles(func)

        # Solve, returns a solution if any.
        path = list()
        assignment = routing.SolveWithParameters(parameters, None)
        if assignment:
            route_number = 0
            node = routing.Start(route_number)
            while not routing.IsEnd(node):
                path.append(vec_list[node])
                node = assignment.Value(routing.NextVar(node))
            return path
        else:
            return list()

    @staticmethod
    def greedy_ts_path(vec_list):
        graph = dict()
        used = []
        current = vec_list[0]
        # print vec_list

        while len(used) + 1 < len(vec_list):
            used.append(current)

            min_dist = None
            nearest_neighbour = None

            for potential in vec_list:
                if potential not in used:
                    dist_to = Vector.distance(current, potential)
                    if min_dist is None or dist_to < min_dist:
                        min_dist = dist_to
                        nearest_neighbour = potential
            graph[current] = nearest_neighbour
            current = nearest_neighbour
        return graph

    @staticmethod
    def nearest_neighbour(start_point, vectors):
        min_dist = None
        nearest = None

        for potential in vectors:
            dist_to = Vector.distance(start_point, potential)
            if min_dist is None or dist_to < min_dist:
                min_dist = dist_to
                nearest = potential
        return nearest

    @staticmethod
    def length(tour):
        length = 0
        for i in range(len(tour) - 1):
            length += Vector.distance(tour[i], tour[i + 1])
        return length

    @staticmethod
    def shortest(tour_list):
        shortest = None
        return_list = None
        for tour in tour_list:
            tour_length = Pathfinder.length(tour)
            if shortest is None or tour_length < shortest:
                shortest = tour_length
                return_list = tour

        return return_list

    @staticmethod
    def slow_greedy_path(vec_list, start=None, end_size=8):
        if start is None:
            start = vec_list[0]
        tour = [start]
        unvisited = []
        unvisited.extend(vec_list)
        unvisited.remove(start)

        while len(unvisited) > end_size:
            C = Pathfinder.nearest_neighbour(tour[-1], unvisited)
            tour.append(C)
            unvisited.remove(C)

        ends = map(list, itertools.permutations(unvisited))
        best = Pathfinder.shortest([tour[0], tour[-1]] + end for end in ends)

        return tour + best[2:]

    @staticmethod
    def random_swap(path_in):
        path = []
        path.extend(path_in)

        rand1 = random.randint(0, len(path) - 1)
        rand2 = random.randint(0, len(path) - 1)

        path[rand1], path[rand2] = path[rand2], path[rand1]

        return path

    @staticmethod
    def improve_tour(path, num_fails=None):
        if num_fails is None:
            num_fails = len(path) * 4

        path_length = Pathfinder.length(path)
        while num_fails > 0:
            trial = Pathfinder.random_swap(path)
            trial_length = Pathfinder.length(trial)

            if trial_length < path_length:
                # print("Path improved! ", trial_length, " < ", path_length)
                path = trial
                path_length = trial_length
            else:
                num_fails -= 1

        return path
