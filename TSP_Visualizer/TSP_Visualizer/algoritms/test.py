import numpy as np

def step_gd(current_b, current_m, points, lr):
    b_gradient =0
    m_gradient =0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient += -((2/N) *((current_m * x) + current_b))
        m_gradient += -(2/N) * x * (y- ((current_m + x) + current_b))
    new_b = current_b -(lr * b_gradient)
    new_m = current_m -(lr * m_gradient)
    return [new_b, new_m]
    pass

def gd(points, st_b,st_m,r,i):
    b = st_b
    m = st_m
    for i in range(iter):
        b, m
    return [b,m]
    pass

if __name__=="__main__":
    print("hello")
    points = np.genfromtxt("./data/data.csv", delimiter=",")
    print(points)

    learning_rate = 0.001
    init_b = 0
    init_m =0
    num_iter = 1000
    b, m =gd(points, init_b, init_m, learning_rate, num_iter)
    print(b, m)