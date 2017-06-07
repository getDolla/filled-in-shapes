import math

e = 1
V = [0, 0, 1]

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

def scalar_mult(vector, scalar):
    return [ scalar * i for i in vector ]

def vector_subtraction(a, b):
    return [ (a[0] - b[0]), (a[1] - b[1]), (a[2] - b[2]) ]

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

def i_ambient(A, K_a):
    return A * K_a

def i_diffuse(L_c, K_d, N, L):
    p = calculate_dot_product(N, L)
    return L_c * K_d * p

def i_specular(L_c, K_s, N, L):
    N_L = calculate_dot_product(N, L)
    p = scalar_mult(N, 2)
    p = scalar_mult(p, N_L)
    d = vector_subtraction(p, L)
    p = calculate_dot_product(d, V)
    
    return L_c * K_d * (p ** e)

def intensity(i_ambient, i_diffuse, i_specular):
    return i_ambient + i_diffuse + i_specular
