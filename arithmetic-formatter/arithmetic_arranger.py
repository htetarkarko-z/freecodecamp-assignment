def arithmetic_arranger(problems, solve=False):
    first = ''
    second = ''
    operator = ''
    first_line = ''
    second_line = ''
    anwser = ''
    line = ''

    if len(problems) > 5:
        return "Error: Too many problems."

    for char in problems:
        problem = char.split()
        first = problem[0]
        second = problem[2]
        operator = problem[1]

        if not first.isnumeric() or not second.isnumeric():
            return "Error: Numbers must only contain digits."

        if (len(first) > 4 or len(second) > 4):
            return "Error: Numbers cannot be more than four digits."

        if (operator == '+' or operator == '-'):
            if operator == '+':
                sums = str(int(first) + int(second))
            else:
                sums = str(int(first) - int(second))

            length = max(len(first), len(second)) + 2
            first_line += str(first).rjust(length) + '    '
            second_line += operator + str(second).rjust(length - 1) + '    '
            line += length * '-' + '    '
            anwser += str(sums).rjust(length) + '    '
        else:
            return "Error: Operator must be '+' or '-'."
    if solve:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + line.rstrip() + '\n' + anwser.rstrip()
    else:
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + line.rstrip()

    return arranged_problems
