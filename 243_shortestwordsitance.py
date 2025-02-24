def shortestDistance(wd, w1, w2):
    w1i = -1
    w2i = -1
    for i in range(len(wd)):
        if wd[i] == w1:
            w1i = i
        if wd[i] == w2:
            w2i = i
        if (w2i > - 1 and w1i > -1):
            cur_dis = abs(w2i - w1i + 1)
            min_dis = min(cur_dis, min_dis)
    return min_dis
