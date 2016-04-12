import argparse
import sympy
import ode_methods
import iterative_methods
import math


def parse_input():

    parser = argparse.ArgumentParser(
        description='Apply ODE and Iterative methods')
    parser.add_argument('-f',
                        '--func',
                        metavar='f(x)',
                        type=str,
                        required=True,
                        help='an ODE or sequence function in terms of (t, y) '
                        'for ODEs and (y) for sequences')
    subparsers = parser.add_subparsers(dest='command', title='sub-commands')

    ode_parser = subparsers.add_parser(
        'ode',
        help='Approximate output using an ODE over a range')
    ode_parser.add_argument('-s',
                            '--start',
                            required=True,
                            type=float,
                            help='initial value of t')
    ode_parser.add_argument('-e',
                            '--end',
                            type=float,
                            required=True,
                            help='end-range value of t')
    ode_parser.add_argument('-i',
                            '--initial',
                            type=float,
                            required=True,
                            help='initial absolute value')
    ode_parser.add_argument('-d',
                            '--step',
                            type=float,
                            required=True,
                            help='initial value of t')

    ode_parser.add_argument('-m',
                            '--method',
                            type=str,
                            required=True,
                            choices=['midpoint', 'euler', 'euler-mod', 'rk4'],
                            help='which ODE method to use')
    ode_parser.add_argument('-t',
                            '--tol',
                            type=float,
                            required=True,
                            help='tolerance')

    iter_parser = subparsers.add_parser('iterative',
                                        help='Approximate root of a function')

    iter_parser.add_argument('-t',
                             '--tol',
                             type=float,
                             required=True,
                             help='tolerance')
    iter_parser.add_argument('-i',
                             '--initial',
                             type=float,
                             required=True,
                             help='initial guess')
    iter_parser.add_argument('-k',
                             '--initial2',
                             type=float,
                             required=True,
                             help='second gues required for secant method')

    iter_parser.add_argument('-m',
                             '--method',
                             type=str,
                             required=True,
                             choices=['newton', 'secant', 'newton-mod'],
                             help='which iterative method to use')

    return parser.parse_args()


def run_ode(args):
    methods = {
        'euler': ode_methods.euler_range,
        'euler-mod': ode_methods.euler_modified_range,
        'midpoint': ode_methods.midpoint_range,
        'rk4': ode_methods.runge_kutta_4_range
    }

    t = sympy.Symbol('t')
    y = sympy.Symbol('y')
    expr = sympy.sympify(args.func)

    def wrapper(t_val, y_val):
        return expr.subs({t: t_val, y: y_val})

    vals = methods[args.method](wrapper, args.initial, args.start, args.end,
                                args.step)

    for t, y in vals:
        print('f({:.4f}) = {}'.format(t, y))


def run_iterative(args):
    x = sympy.Symbol('x')
    expr = sympy.sympify(args.func)
    expr_prime = expr.diff(x)

    def wrapper(x_val):
        return expr.subs({x: x_val})

    def wrapper_prime(x_val):
        return expr_prime.subs({x: x_val})

    vals = []

    if args.method == 'newton':
        vals.extend(iterative_methods.newton(wrapper, wrapper_prime,
                                             args.initial, args.tol))
    elif args.method == 'newton-mod':
        expr_2prime = expr_prime.diff(x)

        def wrapper_2prime(x_val):
            return expr_2prime.subs({x: x_val})

        vals.extend(iterative_methods.newton_modified(
            wrapper, wrapper_prime, wrapper_2prime, args.initial, args.tol))
    elif args.method == 'secant':
        vals.extend(iterative_methods.secant(
            wrapper, wrapper_prime, args.initial, args.initial2, args.tol))

    for i, x in enumerate(vals):
        print('x_{} = {}'.format(i, x))


def main():
    args = parse_input()

    if args.command == 'ode':
        run_ode(args)
    elif args.command == 'iterative':
        run_iterative(args)


if __name__ == '__main__':
    main()
