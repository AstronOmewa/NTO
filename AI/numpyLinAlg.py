import numpy as np

def cumulative_mean_2d(a):
    size = (len(a),len(a[0]))
    a = np.cumsum(a).reshape(*size)
    # a = np.reshape(size)
    b = a * np.array([[1/(i+1) for i in range(j*size[1],size[1]*(j+1))] for j in range(size[0])]).reshape(*size)

    return

print(cumulative_mean_2d(np.array([1, 1.5, 7./3, -0.5, 1, 1, 1, 1]).reshape(2,4)),
      np.cumsum(np.array([1, 1.5, 7./3, -0.5, 1, 1, 1, 1])).reshape(2,4))

