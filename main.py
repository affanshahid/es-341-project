import argparse
import sympy
import ode_methods.ode_range_methods as ode_methods


def parser_input():

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

    return parser.parse_args()


def run_ode(args):
    methods = {
        'euler': ode_methods.euler_range,
        'euler_mod': ode_methods.euler_modified_range,
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


def main():
    args = parser_input()

    if (args.command == 'ode'):
        run_ode(args)
    elif (args.command == 'iterative'):
        pass


if __name__ == '__main__':
    main()
