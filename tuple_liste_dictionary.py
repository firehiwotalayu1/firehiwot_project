def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count

my_tuple = (1, 2, 3, 4, 5)
print("Length of tuple:", tuple_length(my_tuple))
my_tuple = (10, 20, 30, 40, 50)
print("Maximum value:", max(my_tuple))
print("Minimum value:", min(my_tuple))
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)
my_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in my_list]
print("Squared elements:", squared_list)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)
my_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {v: k for k, v in my_dict.items()}
print("Swapped dictionary:", swapped_dict)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
    n = 10
triplets = [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a**2 + b**2 == c**2]
print("Pythagorean triplets:", triplets)


print("Fibonacci number at position 5:", fibonacci(5))
def filter_even_numbers(t):
    return tuple(x for x in t if x % 2 == 0)

my_tuple = (1, 2, 3, 4, 5, 6)
even_tuple = filter_even_numbers(my_tuple)
my_tuple = [('a', 3), ('b', 1), ('c', 2)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print("Sorted list:", sorted_list)

print("Even numbers:", even_tuple)
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

my_nested_list = [[1, 2], [3, 4]]
flat_list = flatten_list(my_nested_list)
print("Flattened list:", flat_list)
def remove_element(lst, element):
    return [x for x in lst if x != element]

my_list = [1, 2, 2, 3, 4, 2]
new_list = remove_element(my_list, 2)
print("List after removal:", new_list)
from collections import defaultdict

def invert_dict(d):
    inverted_dict = defaultdict(list)
    for k, v in d.items():
        inverted_dict[v].append(k)
    return dict(inverted_dict)

my_dict = {'a': 1, 'b': 2, 'c': 1}
inverted = invert_dict(my_dict)
print("Inverted dictionary:", inverted)
students_marks = {
    'Alice': [90, 80, 85],
    'Bob': [70, 75, 80],
    'Charlie': [100, 95, 90]
}

def find_top_student(marks):
    averages = {student: sum(scores) / len(scores) for student, scores in marks.items()}
    top_student = max(averages, key=averages.get)
    return top_student, averages[top_student]

top_student, top_score = find_top_student(students_marks)
print(f"Top student: {top_student} with an average score of {top_score}")

