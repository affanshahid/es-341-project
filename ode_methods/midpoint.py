from .euler import euler


def midpoint(ode, prev_val, t, step_size):
    w_half = euler(ode, prev_val, t, step_size / 2)
    return euler(ode,
                 step_size=step_size,
                 t=(t + step_size / 2),
                 prev_val=w_half)
