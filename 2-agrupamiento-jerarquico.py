import random
import math
import functools

class Cluster:
    def __init__(self, inital_point):
        self.points = []
        self.points.append(inital_point)
    
    def get_center_point(self):
        list_x = [point.x for point in self.points]
        list_y = [point.y for point in self.points]
        avg_x = functools.reduce(lambda a, b : a + b, list_x) / len(list_x)
        avg_y = functools.reduce(lambda a, b : a + b, list_y) / len(list_y)
        temp_point = Point(avg_x, avg_y)
        return temp_point
    
    def eat_cluster(self, other_cluster):
        other_points = other_cluster.points
        for other_point in other_points:
            self.points.append(other_point)
    
    def __str__(self):
        ps = self.points
        s = '['
        for p in ps:
            s = f'{s}| {p} '
        s = s + '|] '
        center = self.get_center_point()
        s = f'{s} \t {center}\n'
        return s


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_coords(self):
        return (self.x, self.y)

    def __str__(self):
        return f'X:{self.x}, Y:{self.y}'

def random_points(n):
    points = []
    for _ in range(n):
        rand_x = random.randint(0, 10)
        rand_y = random.randint(0, 10)
        temp_point = Point(rand_x, rand_y)
        points.append(temp_point)
    return points

def euclidean_distance(point_1, point_2):
    a, b = point_1.get_coords()
    c, d = point_2.get_coords()
    return math.sqrt(math.pow(a - c, 2) + math.pow(b - d, 2))

def get_min_distance_clusters_indexs(clusters):
    len_clt = len(clusters)
    min_distance = float('inf')
    min_i = -1
    min_j = -1
    for i in range(len_clt):
        clt_i = clusters[i]
        point_i = clt_i.get_center_point()
        for j in range (i+1, len_clt, 1):
            clt_j = clusters[j]
            point_j = clt_j.get_center_point()
            distance = euclidean_distance(point_i, point_j)
            if(distance < min_distance):
                min_distance = distance
                min_i = i
                min_j = j
    return (min_i, min_j)
    
def cluster_union_by_index(clusters, index_1, index_2):
    cluster_1 = clusters[index_1]
    cluster_2 = clusters[index_2]

    cluster_1.eat_cluster(cluster_2)
    del clusters[index_2]
    return clusters

def main(clusters):
    for cluster in clusters:
        print(cluster)
    print('*'*200)
    while len(clusters) > 1:
        index_1, index_2 = get_min_distance_clusters_indexs(clusters)
        clusters = cluster_union_by_index(clusters, index_1, index_2)
        for cluster in clusters:
            print(cluster)
        print('*'*200)



if __name__ == '__main__':
    points = random_points(10)
    clusters = []
    for p in points:
        temp_clust = Cluster(p)
        clusters.append(temp_clust)
    main(clusters)


