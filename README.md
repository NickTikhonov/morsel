morsel
======
Morsel is a Python & Java library that generates sampling strategies for parameterised 2D space. This library currently supports several methods of sampling quadralateral shapes defined by x and y coordinates, including:

- random sampling: generating N random points inside a quad
- stratified systematic sampling: generating an N by N grid inside the quad and returning the centerpoint of each strum
- stratified random sampling: generating an N by N grid inside the quad and selecting M random points inside each stratum

In addition to generating samples, Morsel contains tools that can be used to generate an efficient path that visits every sample point. 

![Stratified random sampling and shortest path](http://i.imgur.com/uDPYIXz.png)

### Python example
```python
from morsel.entities import Vector, Triangle, Quad
from morsel.quad_field import Field

sample_field = Field(
	Vector(0,0), 
	Vector(10.9,0), 
	Vector(10,10), 
	Vector(0,10))

# Generate a list of Vector objects containing x and y coordinates of samples
simple_random_samples = sample_field.get_simple_random_samples(7)
```

### Java example
```java
Field demo = new Field(
	new Vector(0.0, 0.0),
	new Vector(0.0, 10.0),
	new Vector(10.0, 10.0),
	new Vector(10.0, 0.0));
	
demo.generateRects(2, 2);

ArrayList<Vector> samples = demo.getSamples();
```

### Planned features

- [ ] stratified sampling of irregular shapes - Voronoi/Decomposition
- [X] shortest path algorithm to allow for efficient sampling of generated points
- [ ] RESTful api wrapper for improved integration
- [X] python support

### Example application
Stratified soil sampling using an android application:

![Use within an Android application](http://i.imgur.com/ls1rRtb.png)
