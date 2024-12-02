# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# solve puzzle 1 by simply running the check
def solve_puzzle_1(data):
    number_of_safe_reports = 0
    unsafe_reports = []
    for line in data:
        report = list(map(int, line.split()))

        if is_safe(report):
            number_of_safe_reports += 1
        else:
            # save for later use in puzzle 2
            unsafe_reports.append(report)

    return number_of_safe_reports, unsafe_reports

# solve puzzle 2 by running the check on the unsafe reports after removing one element from those reports
def solve_puzzle_2(unsafe_reports):
    number_of_safe_reports = 0
    for report in unsafe_reports:
        # remove 1 element from the list and check if the remaining list is valid
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]

            # check if new report is safe
            if is_safe(new_report):
                number_of_safe_reports += 1
                break

    return number_of_safe_reports

"""
checks if the report is safe
criteria:
- the levels are either all increasing or all decreasing
- any two adjacent levels differ by at least one and at most three
"""
def is_safe(report):
    # check if the levels are either all increasing or all decreasing
    goes_up_or_down = all(report[i] < report[i+1] for i in range(len(report) - 1)) or \
                      all(report[i] > report[i+1] for i in range(len(report) - 1))
    # check if any two adjacent levels differ by at least one and at most three
    valid_differences = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))
    return goes_up_or_down and valid_differences

if __name__ == '__main__':

    data = read_input('input.txt')

    puzzle_1_count, unsafe_reports = solve_puzzle_1(data)
    print("Number of safe reports:", puzzle_1_count)
    puzzle_2_count = puzzle_1_count + solve_puzzle_2(unsafe_reports)
    print("Number of safe reports with dampener:", puzzle_2_count)
