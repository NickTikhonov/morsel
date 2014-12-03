import math
import random
import itertools

class Vector:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def get_length(self):
		return math.sqrt((self.x * self.x) + (self.y * self.y))

	def add(self, other):
		self.x += other.x
		self.y += other.y

	def __eq__(self, other):
		return other.x == self.x and other.y == self.y

	def __hash__(self):
		return hash("{} {}".format(self.x, self.y))

	def __str__(self):
		return self.get_json_string()

	def __repr__(self):
		return "Vector(x={}, y={})".format(self.x, self.y)

	@staticmethod
	def sum(s1, s2):
		return Vector(s1.x + s2.x, s1.y + s2.y)

	@staticmethod
	def sub(s1, s2):
		return Vector(s1.x - s2.x, s1.y - s2.y)

	@staticmethod
	def inverse(vec):
		return Vector(-vec.x, -vec.y)

	@staticmethod
	def mult_const(vec, length):
		return Vector(vec.x * length, vec.y * length)

	@staticmethod
	def scale(vec, length):
		return Vector.mult_const(vec, length/vec.get_length())

	@staticmethod
	def distance(v1, v2):
		return Vector.sub(v2, v1).get_length()

	def get_json_string(self):
		return "{ x: %s, y: %s }" % (self.x, self.y) 

class Triangle:
	def __init__(self, origin, r1, r2):
		self.origin = origin
		self.r1 = r1
		self.r2 = r2

	def get_sample_vector(self):
		while True:
			b1 = random.random()
			b2 = random.random()

			random_add = Vector.sum(Vector.mult_const(self.r1, b1), Vector.mult_const(self.r2, b2))
			vec = Vector.sum(self.origin, random_add)

			if self.inside_triangle(vec, self.origin, Vector.sum(self.origin, self.r1), Vector.sum(self.origin, self.r2)):
				return vec

	def inside_triangle(self, s, a, b, c):
		pt = [s.x, s.y]
		v1 = [a.x, a.y]
		v2 = [b.x, b.y]
		v3 = [c.x, c.y]

		return self.point_in_triangle(pt, v1, v2, v3)

	def sign(self, p1, p2, p3):
	  return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


	def point_in_aabb(self, pt, c1, c2):
	  return c2[0] <= pt[0] <= c1[0] and \
	         c2[1] <= pt[1] <= c1[1]

	def point_in_triangle(self, pt, v1, v2, v3):
	  b1 = self.sign(pt, v1, v2) <= 0
	  b2 = self.sign(pt, v2, v3) <= 0
	  b3 = self.sign(pt, v3, v1) <= 0

	  return ((b1 == b2) and (b2 == b3)) and \
	         self.point_in_aabb(pt, map(max, v1, v2, v3), map(min, v1, v2, v3))


class Quad:
	def __init__(self, v1, v2, v3, v4, num_samples, plt = None):
		self.sample_points = []

		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.v4 = v4

		self.generate_samples(num_samples)

		if plt:
			plt.plot([v1.x, v2.x] , [v1.y, v2.y], 'g-', lw=1)
			plt.plot([v2.x, v3.x] , [v2.y, v3.y], 'g-', lw=1)
			plt.plot([v3.x, v4.x] , [v3.y, v4.y], 'g-', lw=1)
			plt.plot([v4.x, v1.x] , [v4.y, v1.y], 'g-', lw=1)

	def generate_samples(self, num_samples):
		self.sample_points = []
		t1 = Triangle(self.v1, Vector.sub(self.v2, self.v1), Vector.sub(self.v4, self.v1))
		t2 = Triangle(self.v3, Vector.sub(self.v2, self.v3), Vector.sub(self.v4, self.v3))

		for x in range(0,num_samples):
			if random.random() >= 0.5:
				self.sample_points.append(t1.get_sample_vector())
			else:
				self.sample_points.append(t2.get_sample_vector())

	def get_samples(self):
		return self.sample_points

	def get_centerpoint(self):
		centroid_x = (self.v1.x + self.v2.x + self.v3.x + self.v4.x) / 4
		centroid_y = (self.v1.y + self.v2.y + self.v3.y + self.v4.y) / 4

		return Vector(centroid_x, centroid_y)
