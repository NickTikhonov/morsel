#Import the library
from morsel.entities import Vector, Triangle, Quad
from morsel.quad_field import Field
from morsel.pathfinder import Pathfinder

#function to help us visualise sampler output
def print_samples(samples):
	for sample in samples:
		print sample.get_json_string()

#---How to generate simple random samples inside a 4 sided field: ---
#Step 1: Instantiate field with corner coordinates in clockwise or counterclockwise order
sample_field = Field(
	Vector(1,6), 
	Vector(6,11.1), 
	Vector(11.2,6), 
	Vector(6,1))

#---How to generate stratified random samples inside a field: ---

import matplotlib.pyplot as plt
stratified_random_samples = sample_field.get_stratified_random_samples(10, 1, plt = plt)
print 'Stratified random samples:'
print_samples(stratified_random_samples)

plot_x = []
plot_y = []

for sample in stratified_random_samples:
	plot_x.append(sample.x)
	plot_y.append(sample.y)

path = Pathfinder.slow_greedy_path(stratified_random_samples, end_size=8)
for i in range(len(path) - 1):
	plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'r--', lw=2)

improved_path = Pathfinder.improve_tour(path, len(path)*100)
print("Improved path: ", improved_path)
for j in range(len(improved_path) - 1):
	plt.plot([improved_path[j].x, improved_path[j + 1].x], [improved_path[j].y, improved_path[j + 1].y], 'k-', lw=3)

plt.plot(plot_x, plot_y, 'ro')
plt.show()
