from utils import frange
from .midpoint import midpoint
from .euler import euler
from .euler_modified import euler_modified
from .runge_kutta_4 import runge_kutta_4


def range(ode_method, ode, initial_val, start, end, step_size=0.01):
    values = []
    old_val = initial_val

    for t in frange(start, end + step_size, step_size):
        values.append((t, old_val))
        new_val = ode_method(ode, old_val, t, step_size)
        old_val = new_val

    return values


def euler_range(ode, initial_val, start, end, step_size):
    return range(euler, ode, initial_val, start, end, step_size)


def midpoint_range(ode, initial_val, start, end, step_size):
    return range(midpoint, ode, initial_val, start, end, step_size)


def euler_modified_range(ode, initial_val, start, end, step_size):
    return range(euler_modified, ode, initial_val, start, end, step_size)


def runge_kutta_4_range(ode, initial_val, start, end, step_size):
    return range(runge_kutta_4, ode, initial_val, start, end, step_size)
