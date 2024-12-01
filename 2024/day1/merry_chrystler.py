# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

# solve puzzle 1 by getting total distance between each pair of numbers after sorting
def solve_puzzle_1(data):
    # Split the input into two lists
    left = []
    right = []
    for line in data:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    # Calculate the differences and total distance
    total_distance = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

    return total_distance

# solve puzzle 2 by calculating the similarity score (left number * # of occurrences of left on the right)
def solve_puzzle_2(data):
    # Split the input into two collections
    left = set()
    right = {}
    for line in data:
        l, r = map(int, line.split())
        left.add(l)
        right[r] = right.get(r, 0) + 1

    similarity_score = 0

    # Calculate the similarity score.
    for l in left:
        similarity_score += l * right.get(l, 0) + 1

    return similarity_score

if __name__ == '__main__':

    data = read_input('input.txt')

    print("Total distance:", solve_puzzle_1(data))
    print("Similarity score:", solve_puzzle_2(data))
