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
	Vector(0,5), 
	Vector(5,10.1), 
	Vector(10.1,5), 
	Vector(5,0))

#Step 2: Generate 7 sample points:
simple_random_samples = sample_field.get_simple_random_samples(1000)

#Step 3: View samples:
print 'Simple random samples:'
print_samples(simple_random_samples)

#---How to generate stratified systematic samples inside a field: ---
stratified_systematic_samples = sample_field.get_stratified_systematic_samples(30)
print 'Stratified systematic samples:'
print_samples(stratified_systematic_samples)

#---How to generate stratified random samples inside a field: ---
stratified_random_samples = sample_field.get_stratified_random_samples(15, 1)
print 'Stratified random samples:'
print_samples(stratified_random_samples)

import matplotlib.pyplot as plt
plot_x = []
plot_y = []

for sample in stratified_random_samples:
	plot_x.append(sample.x)
	plot_y.append(sample.y)

path = Pathfinder.slow_greedy_path(stratified_random_samples, end_size=8)
for i in range(len(path) - 1):
	plt.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'k-', lw=2)

plt.plot(plot_x, plot_y, 'ro')
plt.show()