import math

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N

def calculate_mag(vector):
    return math.sqrt( vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2] )

def to_unit_vector(vector):
    v = [0, 0, 0]
    mag = calculate_mag(vector)
    v[0] = (vector[0])/mag
    v[1] = (vector[1])/mag
    v[2] = (vector[2])/mag
    return v

def calculate_dot_product(a, b):
    a = to_unit_vector(a)
    b = to_unit_vector(b)

    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
