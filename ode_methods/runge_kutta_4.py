def runge_kutta_4(ode, prev_val, t, step_size):
    k1 = step_size * ode(t, prev_val)
    k2 = step_size * ode(t + step_size / 2, prev_val + k1 / 2)
    k3 = step_size * ode(t + step_size / 2, prev_val + k2 / 2)
    k4 = step_size * ode(t + step_size, prev_val + k3)

    return prev_val + (k1 + 2 * k2 + 2 * k3 + k4) / 6
