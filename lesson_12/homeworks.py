#1 from HW 01/task 07
def tree_quantity(planted_apple):
    planted_pear = planted_apple + 5
    planted_plum = planted_apple - 2

    all_trees = (planted_apple, planted_pear, planted_plum)
    all_trees_quantity = sum(all_trees)

    return all_trees_quantity

#2 from HW 03/task 02
def count_apostrophes(alice_in_wonderland):
    count = 0

    for char in alice_in_wonderland:
        if char == "'":
            count += 1

    return count

#3 from HW 6.1
def check_unique_symbols(text):
    return len(set(text)) > 10

#4 from HW 6.2
def check_word(word):
    return "h" in word.lower()

#5 from HW 07/task 4
def reverse_text(text):
    return text[::-1]





