import re

# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# solve puzzle 1 by extracting the numbers to multiply, multiplying them and then adding together
def solve_puzzle_1(data):

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    result = 0
    for line in data:
        matches = re.findall(pattern, line)
        result += sum([int(a) * int(b) for a, b in matches])

    return result

# solve puzzle 2 by filtering out sections of the data we don't want to use then using solution 1 to solve the puzzle
def solve_puzzle_2(data):

    filtered_parts = []
    include = True  # Start by including data
    dont_or_do = {"don't()": False, "do()": True}
    for line in data:
        parts = re.split(r"(don't\(\)|do\(\))", line)

        for part in parts:
            include = dont_or_do.get(part, include)
            if include:
                filtered_parts.append(part)

    # reuse the solve_puzzle_1 function to solve the puzzle with the filtered data
    filtered_data_result = solve_puzzle_1(filtered_parts)

    return filtered_data_result

if __name__ == '__main__':

    data = read_input('input.txt')

    print(f"puzzle 1 result: {solve_puzzle_1(data)}")
    print(f"puzzle 2 result: {solve_puzzle_2(data)}")
