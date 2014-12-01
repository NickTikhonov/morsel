import math
import random
import itertools
from entities import Vector, Triangle, Quad

class Field:
	def __init__(self, v1, v2, v3, v4):
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.v4 = v4

	def generate_rects(self, length_divisions, num_samples):
		self.sub_fields = []

		horiz1 = Vector.sub(self.v2, self.v1)
		horiz2 = Vector.sub(self.v3, self.v4)

		step1 = horiz1.get_length()/length_divisions
		step2 = horiz2.get_length()/length_divisions

		points = [[0 for x in range(length_divisions + 1)] for x in range(length_divisions + 1)]

		for i in range(length_divisions + 1):
			current1 = Vector.sum(self.v1, Vector.scale(horiz1, i * step1))
			current2 = Vector.sum(self.v4, Vector.scale(horiz2, i * step2))

			current_vert = Vector.sub(current2, current1)
			current_step = current_vert.get_length()/length_divisions

			for j in range(length_divisions + 1):
				point_pos = Vector.sum(current1, Vector.scale(current_vert, j * current_step))
				points[i][j] = point_pos

		for x in range(length_divisions):
			for y in range(length_divisions):
				self.sub_fields.append(Quad(points[x][y], points[x + 1][y], points[x + 1][y + 1], points[x][y + 1], num_samples))

	#	Returns a list of Vector objects containing samples generated in a stratified, staggered manner.
	#	length_divisions -> When set to N, N * N rectangles are created by dividing the field equally into a grid
	#	num_samples -> the number of random samples to be generated from each rectangle
	#	Total number of samples returned -> length_division^2 * num_samples
	def get_stratified_random_samples(self, length_divisions, num_samples):
		self.generate_rects(length_divisions, num_samples)

		samples = []
		for sub_field in self.sub_fields:
			samples.extend(sub_field.get_samples())

		return samples


	#	Returns a list of Vector objects containing samples generated in a stratified, systematic manner
	#	length_divisions -> When set to N, N * N rectangles are created by dividing the field equally into a grid
	#	Total number of samples returned -> length_division^2
	def get_stratified_systematic_samples(self, length_divisions):
		self.generate_rects(length_divisions, 1)

		samples = []
		for sub_field in self.sub_fields:
			samples.append(sub_field.get_centerpoint())

		return samples

	#	Returns Vector instances representing random points inside this Field instance
	#	num_samples -> number of samples to be returned
	def get_simple_random_samples(self, num_samples):
		self.generate_rects(1, num_samples)

		samples = []
		for sub_field in self.sub_fields:
			samples.extend(sub_field.get_samples())

		return samples