def newton(f, f_prime, initial, tolerance=10**-7):
    def next_val(prev_val):
        if f_prime(prev_val) != 0:
            return prev_val - (f(prev_val) / f_prime(prev_val))

    vals = []
    prev_val = initial

    while True:
        vals.append(prev_val)
        new_val = next_val(prev_val)
        if new_val is None:
            return None
        elif new_val == prev_val:
            break
        elif abs(new_val - prev_val) <= tolerance:
            vals.append(new_val)
            break
        prev_val = new_val

    return vals
