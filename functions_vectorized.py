import numpy as np


def prod_non_zero_diag(x):
    diagonal = np.diag(x)
    non_zero_diag = diagonal[np.diagonal != 0]
    return np.prod(non_zero_diag)


def are_multisets_equal(x, y):
    x = np.sort(x)
    y = np.sort(y)
    return np.array_equal(x,y)



def max_after_zero(x):
    res = np.where(x[:-1])[0]
    return x[res + 1].max()


def convert_image(img, coefs):
    return np.dot(img,coefs)


def run_length_encoding(x):
    x = np.array(x)
    y = np.insert(x,0,0)
    y = y[:-1]
    z = x - y
    z = np.where(z != 0)[0]
    typ = np.append(z,len(x))
    typ = typ[1:]
    return x[z], typ - z



def pairwise_distance(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    return np.sum((x[:, np.newaxis, :] - y[np.newaxis, :, :]) ** 2, axis=2)
