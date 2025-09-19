def prod_non_zero_diag(x):
    prod = 1

    for i in range(len(x)):
        if (i >= len(x[i])):
            break
        if (x[i][i] != 0):
            prod *= x[i][i]
    return prod


def are_multisets_equal(x, y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    for i in range(len(x)):
        if (x[i] != y[i]):
           return False
    return True


def max_after_zero(x):
    res = 0
    for i in range(len(x)-1):
        if (x[i] == 0):
            res = max(res,x[i+1])
    return res


def convert_image(img, coefs):
    arr = []
    for i in range(len(img)):
        arr.append([])
        for j in range(len(img[0])):
            res = 0
            arr[i].append(0)
            for k in range(3):
                res += img[i][j][k]*coefs[k]
            arr[i][j] = res
    return arr
    


def run_length_encoding(x):
    arr = []
    numb = []
    count = 1
    for i in range(1,len(x)):
        if (x[i] != x[i-1]):
            numb.append(count)
            arr.append(x[i-1])
            count = 0
        count += 1
    arr.append(x[len(x)-1])
    numb.append(count)
    return arr,numb


def pairwise_distance(x, y):
    arr = []
    for i in range(len(x)):
        arr.append([])
        for j in range(len(y)):
            res = 0
            for k in range(len(x[0])):
                res += (x[i][k] - y[j][k]) * (x[i][k] - y[j][k])
            arr[i].append(res)
    return arr
