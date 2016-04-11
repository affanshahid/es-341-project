def frange(x, y, jump):
    while round(x, 5) < y:
        yield x
        x += jump
