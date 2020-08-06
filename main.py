import math
import argparse
import sys

parser = argparse.ArgumentParser(description='Credit calculator.')
parser.add_argument("--type", type=str,
                    help='Set type of calculator. Possible values are: annuity, diff')
parser.add_argument("--payment", type=float,
                    help='Monthly payment: positive integer')
parser.add_argument("--periods", type=int,
                    help='number of periods needed to repay the credit: positive integer')
parser.add_argument("--principal", type=float,
                    help='A sum of credit: positive integer')
parser.add_argument("--interest", type=float,
                    help='An interest of credit: positive integer without percentage sign')
args = parser.parse_args()

if len(sys.argv) != 5:
    # print('0 — There should be 4 arguments', '\n', args.type, '\n', sys.argv)
    print('Incorrect parameters')

elif args.type not in ['diff', 'annuity']:
    # print('1 — The --type argument should be set correctly', args)
    print('Incorrect parameters')

elif args.type == 'diff':
    if args.payment is not None:
        # print('diff 1 — The --payment argument shouldn\'t be set when --type=diff', args)
        print('Incorrect parameters')

    elif args.principal and args.principal > 0 \
            and args.periods and args.periods > 0 \
            and args.interest and args.interest > 0:
        P = args.principal
        n = args.periods
        i = args.interest / 12 / 100
        D_sum = 0
        for m in range(1, n + 1):
            D = math.ceil(P / n + i * (P - P * (m - 1) / n))
            D_sum += D
            print(f'Month {m}: paid out {D}')

        OP = math.ceil(D_sum - P)
        # print('diff 2 — Correct arguments', args)
        print(f'\nOverpayment = {OP}')

    else:
        print(args.type)
        print('Incorrect parameters')

elif args.type == 'annuity':
    if args.principal and args.principal > 0 \
            and args.payment and args.payment > 0 \
            and args.interest and args.interest > 0:
        P = args.principal
        A = args.payment
        i = args.interest / 12 / 100
        n = math.ceil(math.log(float(A / (A - i * P)), 1 + i))
        years = n // 12
        months = n % 12

        if years == 1:
            if months == 0:
                period = '1 year'
            elif months == 1:
                period = f'1 year and 1 month'
            else:
                period = f'1 year and {months} months'
        elif years < 0:
            if months != 1:
                period = f'{months} months'
            else:
                period = '1 month'
        elif years > 1:
            if months == 0:
                period = f'{years} years'
            elif months == 1:
                period = f'{years} years and 1 month'
            else:
                period = f'{years} years and {months} months'

        OP = math.ceil(A * n - P)
        # print('annuity 1 — Correct arguments', args)
        print(f'You need {period} to repay this credit!')
        print(f'Overpayment = {OP}')

    elif args.principal and args.principal > 0 \
            and args.periods and args.periods > 0 \
            and args.interest and args.interest > 0:
        P = args.principal
        n = args.periods
        i = args.interest / 12 / 100
        A = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        OP = math.ceil(A * n - P)
        # print('annuity 2 — Correct arguments', args)
        print(f'Your annuity payment = {A}!')
        print(f'Overpayment = {OP}')

    elif args.payment and args.payment > 0 \
            and args.periods and args.periods > 0 \
            and args.interest and args.interest > 0:
        A = args.payment
        n = args.periods
        i = args.interest / 12 / 100
        P = math.floor(A / (i * (1 + i) ** n) * ((1 + i) ** n - 1))
        OP = math.ceil(A * n - P)
        # print('annuity 3 — Correct arguments', args)
        print(f'Your credit principal = {P}!')
        print(f'Overpayment = {OP}')

    else:
        # print(args)
        print('Incorrect parameters')

else:
    # print(args.type)
    print('Incorrect parameters')
