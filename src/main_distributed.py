import utils
from algorithms import *

data_workers, y, lenet5, data, labels,  test_x, test_y = utils.get_data()

M = 10  # workers

# adjacency matrix
A = np.array([
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
])

D = np.diag(np.sum(A, axis=0))
L = D - A
D_half = np.linalg.inv(D**(1/2))  # diagonal matrix
W = np.identity(M) - np.dot(D_half, np.dot(L, D_half))
J = np.full((M, M), 1/M)
norm = np.linalg.norm(W - np.full((M, M), 1/M))
print('norm: ', norm)
d = 784
m = 15
T = 20  # T=50, T=100
epsilon = 0.25

delta_bar = distributed_zo_FW(data_workers, y, lenet5.negative_loss, T, M, d, epsilon, m, A)
np.save(f'../data/perturbations/distributed/report_distributed_delta_{T}_{m}', delta_bar)
