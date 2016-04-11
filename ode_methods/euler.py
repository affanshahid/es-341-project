def euler(ode, prev_val, t, step_size):
    return prev_val + (step_size * ode(t, prev_val))
