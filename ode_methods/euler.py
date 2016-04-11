# Returns array of values calculated using Euler
from utils import frange


def euler(ode, initial_val, start, end, step_size=0.01):
    values = []
    old_val = initial_val

    for t in frange(start, end, step_size):
        new_val = old_val + (step_size * ode(t, old_val))
        values.append((t, new_val))
        old_val = new_val

    return values
