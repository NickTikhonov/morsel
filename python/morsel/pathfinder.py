from entities import Vector
import itertools
import random

class Pathfinder:

	@staticmethod
	def greedy_ts_path(vec_list):
		graph = dict()
		used = []
		current = vec_list[0]

		while len(used) + 1 < len(vec_list):
			used.append(current)

			min_dist = None
			nearest_neighbour = None

			for potential in vec_list:
				if potential not in used:
					dist_to = Vector.distance(current, potential)
					if min_dist == None or dist_to < min_dist:
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
			if min_dist == None or dist_to < min_dist:
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
	def slow_greedy_path(vec_list, start = None, end_size = 8):
		if start is None: start = vec_list[0]
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
	def improve_tour(path, num_fails = None):
		if num_fails is None: num_fails = len(path) * 4
		path_length = Pathfinder.length(path)

		while num_fails > 0:
			trial = Pathfinder.random_swap(path)
			trial_length = Pathfinder.length(trial)

			if trial_length < path_length:
				print("Path improved! ", trial_length, " < ", path_length)
				path = trial
				path_length = trial_length
			else:
				num_fails -= 1

		return path

