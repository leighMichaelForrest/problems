import sys

OVERTIME_FACTOR = 1.5

def payroll(wage, hours):
    """Determine the gross pay. Hours over 40 pay time and a half plus 40 hours
    regular time.
    wage: The hourly wage of employee.
    hours: The number of hours worked."""
    try:
        wage = float(wage); hours = float(hours)
        regular = 0; overtime = 0

        if hours <= 40:
            regular = hours
        else:
            regular = 40
            overtime = hours - 40

    except ValueError:
        print("ValueError")
        wage = 0; hours = 0

    return (regular * wage) + (overtime * wage * OVERTIME_FACTOR)\


if __name__ == '__main__':
    wage, hours = float(sys.argv[1]), float(sys.argv[2])
    print(f"The gross pay of ${'%5.2f' % wage} and {'%5.2f' % hours} hours is ${'%5.2f' % payroll(wage, hours)}")
