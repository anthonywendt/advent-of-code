# read input
def read_input(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def parse_rules_and_page_lists(input_data):
    rules_section, page_lists_section = input_data.strip().split("\n\n")
    return [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()], \
            [list(map(int, line.split(","))) for line in page_lists_section.splitlines()]

def satisfies_rules(list, rules):
    for a, b in rules:
        # Both numbers must be present in the list
        if a in list and b in list:
            # If `a` appears after `b`, the rule is violated
            if list.index(a) > list.index(b):
                return False
    return True

# sum middle numbers from page lists that satisfy the rules
def sum_middle_numbers(rules, page_lists):
    total = 0
    for list in page_lists:
        if satisfies_rules(list, rules):
            if len(list) % 2 == 1:  # Ensure the list has a single middle element
                middle_index = len(list) // 2
                total += list[middle_index]
    return total

# fix a page list repeatedly until it satisfies all rules
def fix_list(list, rules):
    while not satisfies_rules(list, rules):
        for a, b in rules:
            if a in list and b in list:
                if list.index(a) > list.index(b):  # If `a` is after `b`
                    list.remove(a)
                    list.insert(list.index(b), a)  # Place `a` just before `b`
    return list

# fix incorrect lists and sum their middle numbers
def sum_fixed_middle_numbers(rules, page_lists):
    total = 0
    for list in page_lists:
        if not satisfies_rules(list, rules):
            fixed_list = fix_list(list[:], rules)
            if len(fixed_list) % 2 == 1:  # Ensure it has a single middle element
                middle_index = len(fixed_list) // 2
                total += fixed_list[middle_index]
    return total

if __name__ == '__main__':

    data = read_input('input.txt')
    rules, page_lists = parse_rules_and_page_lists(data)

    print(f"Sum of all satisfied middle numbers: {sum_middle_numbers(rules, page_lists)}")
    print(f"Sum of all fixed middle numbers: {sum_fixed_middle_numbers(rules, page_lists)}")
