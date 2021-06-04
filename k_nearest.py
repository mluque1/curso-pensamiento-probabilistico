import math
import random
import collections
from bokeh.plotting import figure, show


class Point:
    def __init__(self, x, y, tag = 'No Tag'):
        self.x = x
        self.y = y
        self.tag = tag
    
    def get_coords(self):
        return (self.x, self.y)

    def set_tag(self, tag):
        self.tag = tag

    def __str__(self):
        return f'X:{self.x}, Y:{self.y}, | {self.tag}'

def gen_points(x_mean, y_mean, tag, n):
    points = []
    for _ in range(n):
        rand_x = x_mean + (random.random() * random.choice([x/100 for x in range(-95, 95, 1)]))
        rand_y = y_mean + (random.random() * random.choice([y/100 for y in range(-95, 95, 1)]))
        temp_point = Point(rand_x, rand_y, tag)
        points.append(temp_point)
    return points

def gen_proof_points(n):
    points = []
    for _ in range (n):
        rand_x = random.uniform(0.0, 4.0)
        rand_y = random.uniform(0.0, 4.0)
        temp_point = Point(rand_x, rand_y)
        points.append(temp_point)
    return points


def euclidean_distance(point_1, point_2):
    a, b = point_1.get_coords()
    c, d = point_2.get_coords()
    return math.sqrt(math.pow(a - c, 2) + math.pow(b - d, 2))

def graph(houses, houses_names, houses_colors, alph=0.5, p = figure(plot_width=900, plot_height=900, title="Houses of Hogwarts")):
    for index, house in enumerate(houses):
        x_values = [point.x for point in house]
        y_values = [point.y for point in house]
        p.circle(x_values, y_values, size=15, color=houses_colors[index], alpha=alph, legend_label=houses_names[index])
    
    return p

def find_farthest_distance(distances):
    max_distance = float('-inf')
    max_index = -1
    for index, distance in enumerate(distances):
        if(distance > max_distance):
            max_distance = distance
            max_index = index
    return max_index


def find_k_nearest_tags(initial_points, point, k):
    distances = []
    ind = []
    for index, initial in enumerate(initial_points):
        distance = euclidean_distance(initial, point)
        distances.append(distance)
        ind.append(index)
        if(len(distances) > k):
            index_remove = find_farthest_distance(distances)
            del distances[index_remove]
            del ind[index_remove]
    k_nearest_tags = []
    for i in ind:
        k_nearest_tags.append(initial_points[i].tag)
    return k_nearest_tags

def find_tag_by_nearest(k_nearest_tags):
    counter = dict(collections.Counter(k_nearest_tags))

    max_value = float('-inf')
    final_tag = ''
    for key, value in counter.items():
        if(value > max_value):
            max_value = value
            final_tag = key
    return final_tag

def evaluate(initial_points, proof_points):
    for proof in proof_points:
        k_nearest_tags = find_k_nearest_tags(initial_points, proof,5)
        new_tag = find_tag_by_nearest(k_nearest_tags)
        proof.set_tag(new_tag)
        initial_points.append(proof)
    
    houses = []
    for _ in range(4):
        houses.append([])
    for proof in proof_points:
        if(proof.tag == 'Hufflepuff'):
            houses[0].append(proof)
        elif(proof.tag == 'Ravenclaw'):
            houses[1].append(proof)
        elif(proof.tag == 'Gryffindor'):
            houses[2].append(proof)
        elif(proof.tag == 'Slytherin'):
            houses[3].append(proof)

    houses_names = [ 'Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin']
    houses_colors = [ '#FFFF00', '#0004FF','#FF0000', '#009E0E']
    p = graph(houses, houses_names, houses_colors, alph=0.1)
    show(p)


def all_points(houses):
    points = []
    for house in houses:
        for h in house:
            points.append(h)
    return points

def main():
    hufflepuff = gen_points(1,1,'Hufflepuff', 50)
    ravenclaw = gen_points(3,1,'Ravenclaw', 50)
    gryffindor = gen_points(1,3,'Gryffindor', 50)
    slytherin = gen_points(3,3,'Slytherin', 50)
    houses = [ hufflepuff, ravenclaw, gryffindor, slytherin]
    houses_names = [ 'Hufflepuff', 'Ravenclaw', 'Gryffindor', 'Slytherin']
    houses_colors = [ '#d39427', '#1a6da8','#9d0f41', '#1d7452']
    p1 = graph(houses, houses_names, houses_colors)
    show(p1)
    input()
    initial_points = all_points(houses)
    proof_points = gen_proof_points(200)
    evaluate(initial_points, proof_points)

    

if __name__=='__main__':
    main()
    