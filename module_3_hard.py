
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                      ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):

    for item in data_structure:
        if isinstance(item, list):
            calculate_structure_sum(item)
        elif isinstance(item, set):
            calculate_structure_sum(item)
        elif isinstance(item, tuple):
            calculate_structure_sum(item)
        elif isinstance(item, dict):
            for value, key in item.items():
                print(len(value))
                print(key)
        elif isinstance(item, str):
            print(len(item))
        elif isinstance(item, int):
            print(item)

calculate_structure_sum(data_structure)

