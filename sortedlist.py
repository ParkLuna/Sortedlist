def sort_by_last_element(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list

# Example input
input_tuples = [(2,5),(1,2),(4,4),(2,3),(2,1)]

sorted_tuples = sort_by_last_element(input_tuples)
print("Sorted Tuples:", sorted_tuples)
