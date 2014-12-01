#Import the library
from morsel.entities import Vector, Triangle, Quad
from morsel.quad_field import Field

#function to help us visualise sampler output
def print_samples(samples):
	for sample in samples:
		print sample.get_json_string()

#---How to generate simple random samples inside a 4 sided field: ---
#Step 1: Instantiate field with corner coordinates in clockwise or counterclockwise order
sample_field = Field(
	Vector(0,0), 
	Vector(10.9,0), 
	Vector(10,10), 
	Vector(0,10))

#Step 2: Generate 7 sample points:
simple_random_samples = sample_field.get_simple_random_samples(7)

#Step 3: View samples:
print 'Simple random samples:'
print_samples(simple_random_samples)

#---How to generate stratified systematic samples inside a field: ---
stratified_systematic_samples = sample_field.get_stratified_systematic_samples(5)
print 'Stratified systematic samples:'
print_samples(stratified_systematic_samples)

#---How to generate stratified random samples inside a field: ---
stratified_random_samples = sample_field.get_stratified_random_samples(5, 2)
print 'Stratified random samples:'
print_samples(stratified_random_samples)