from .euler import euler


def euler_modified(ode, prev_val, t, step_size):
    simple = euler(ode, prev_val, t, step_size)
    return (simple + prev_val + (step_size * ode(t + step_size, simple))) / 2
