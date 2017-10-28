class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.children = 0

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        self.children = self.children + 1
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        self.children = self.children + 1
        return self.right


root = BinaryTreeNode(10)
left = root.insert_left(8)
left.insert_left(7)
left2 = left.insert_right(9)

right = root.insert_right(12)
right.insert_left(11)
right.insert_right(14)


def print_tree(current_node, indent="", last='updown'):
    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1

    size_branch = {child: nb_children(child) for child in current_node.children}
    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(current_node.name))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up':
        start_shape = '┌'
    elif last == 'down':
        start_shape = '└'
    elif last == 'updown':
        start_shape = ' '
    else:
        start_shape = '├'

    if up:
        end_shape = '┤'
    elif down:
        end_shape = '┐'
    else:
        end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.name, end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(current_node.name))
        print_tree(child, indent=next_indent, last=next_last)


def is_binary_search_tree(root):
    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # if this node is invalid, we return false right away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True


def is_binary_search_tree_rec(root,
                              lower_bound=-float('inf'),
                              upper_bound=float('inf')):
    if not root:
        return True

    if root.value >= upper_bound or root.value <= lower_bound:
        return False

    return is_binary_search_tree_rec(root.left, lower_bound, root.value) and is_binary_search_tree_rec(root.right, root.value, upper_bound)


print("iterative " + str(is_binary_search_tree(root)))
print("recursive " + str(is_binary_search_tree_rec(root)))
left.insert_right(100)
print("iterative false " + str(is_binary_search_tree(root)))
print("recursive false " + str(is_binary_search_tree_rec(root)))
# print_tree(root)
