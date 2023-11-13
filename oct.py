def frequency_counter(text: str) -> dict:
    frequencies = {}

    for char in text:
        if char not in frequencies:
            frequencies[char] = 1
            continue
        frequencies[char] += 1 

    return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)


class NodeTree:
    def __init__(self, left = None, right = None) -> None:
        self.right = right
        self.left = left

    def children(self):
        return (self.left, self.right)
    
    def __str__(self) -> str:
        return f"0:{str(self.left)}  1:{str(self.right)}"
    

def huffman_tree(node, bin_string: str='') -> dict:
    if type(node) is str:
        return {node: bin_string}
    
    (l, r) = node.children()
    tree = dict()
    tree.update(huffman_tree(l, bin_string + '0'))
    tree.update(huffman_tree(r, bin_string + '1'))
    return tree


def creat_tree(nodes: list):
    print(nodes)
    while len(nodes) > 1:
        first = nodes[-1]
        second = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(first[0], second[0])
        print(node)
        nodes.append((node, first[1] + second[1]))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    
    return nodes[0][0]


if __name__ == '__main__':
    print(huffman_tree(creat_tree(frequency_counter('hello_world'))))
