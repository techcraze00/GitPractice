'''
Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list
of positive integers representing different flux converters - which returns a list of integers p where each
element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there
is no such converter. For example, solution(3, [1, 4, 7]) would return the converters above the converters at
indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root,
h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree 
with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p 
contain at least one but no more than 10000 distinct integers, all of which will be between 1
and 2^h-1, inclusive
'''

def solution(h, q):
    nodes = 2 ** h - 1  # Total number of nodes in the perfect binary tree
    results = []

    for node_label in q:
        if node_label < 1 or node_label >= nodes:
            results.append(-1)  # Invalid node label
        else:
            parent = find_parent(node_label, nodes)
            results.append(parent)

    return results

# Return the list 

def find_parent(node_label, nodes):
    if node_label == nodes:
        return -1  # The root has no parent

    left_child = node_label * 2
    right_child = node_label * 2 + 1

    if left_child >= nodes or right_child >= nodes:
        return -1  # Node has no children, so no parent

    if left_child < nodes and node_label != nodes:
        return left_child  # Left child is the parent of the current node

    if right_child < nodes and node_label != nodes:
        return right_child  # Right child is the parent of the current node


print(solution(3, [1, 4, 7]))  #returns the soltuion
