def secant(f, f_prime, initial_first, initial_second, tolerance=10**(-7)):
    def next_val(prev_val, prev_prev_val):
        return prev_val - (f(prev_val) * (prev_val - prev_prev_val) /
                           (f(prev_val) - f(prev_prev_val)))
    vals = []
    prev_val = initial_second
    prev_prev_val = initial_first
    vals.append(prev_prev_val)

    while True:
        vals.append(prev_val)
        new_val = next_val(prev_val, prev_prev_val)
        
        if new_val is None:
            return None
        elif new_val == prev_val:
            break
        elif abs(new_val - prev_val) <= tolerance:
            vals.append(new_val)
            break
        prev_prev_val = prev_val
        prev_val = new_val

    return vals
