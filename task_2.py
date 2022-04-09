# 2. Закодируйте любую строку по алгоритму Хаффмана.

class HuffmanNode:
    def __init__(self, symbol, freq, left=None, right=None, code=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.code = code

    def __str__(self):
        return f'"{self.symbol}"'


def get_symbol_freq(in_str: str) -> list:
    checked_letters = []
    nodes = []

    for letter in in_str:
        if letter not in checked_letters:
            checked_letters.append(letter)

            nodes.append(HuffmanNode(letter, in_str.count(letter)))

    return nodes


def huffman_make_tree(nodes: list) -> HuffmanNode:

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        l_node = nodes[0]
        r_node = nodes[1]

        l_node.code = 0
        r_node.code = 1

        node = HuffmanNode(l_node.symbol+r_node.symbol, l_node.freq+r_node.freq, l_node, r_node)

        nodes.append(node)
        nodes.remove(l_node)
        nodes.remove(r_node)

    return nodes[0]


def get_code(root, code):
    result_code = code

    if root.code != None:
        result_code += str(root.code)

    if root.left:
        get_code(root.left, result_code)

    if root.right:
        get_code(root.right, result_code)

    if root.right == None and root.left == None:
        codes[root.symbol] = result_code


def encode(in_str: str) -> str:
    result = ''
    for s in in_str:
        result += codes[s] + ' '

    return result


def decode(in_str: str) -> str:
    decodes = {}
    for k, v in codes.items():
        decodes[v] = k

    splitted = in_str.split()

    result = ''
    for i in splitted:
        result += str(decodes[i])

    return result


def print_tree(node, level):
    if level == 0:
        result = f'."{node.symbol}"' + '\n'
    else:
        result = '  '*(level - 1) + '..' + f'code = {node.code} symbol = "{node.symbol}"\n'

    if node.left:
        result += print_tree(node.left, level+1)

    if node.right:
        result += print_tree(node.right, level + 1)

    return result


#       test 1
# test_str_1 = 'beep boop beer!'
# test_str_1 = 'abrakadabra'
# test_str_1 = 'hello world!'
# test_str_1 = 'абыр валг'
# test_str_1 = '11111' #тут проблема, если только один символ
# test_str_1 = '!"№;%:?*()_+'
# test_str_1 = '12'



print('-' * 15 + 'test string' + '-' * 15)
print(f'"{test_str_1}"\n')

nodes = get_symbol_freq(test_str_1)
root = huffman_make_tree(nodes)

print('-' * 15 + 'Huffman tree' + '-' * 15)
print(print_tree(root, 0))

print('-' * 15 + 'Codes' + '-' * 15)
codes = {}
get_code(root, '')
for k, v in codes.items():
    print(f'"{k}" - {v}')

print('-' * 15 + 'encoded string' + '-' * 15)
encoded_str = encode(test_str_1)
print(f'"{test_str_1}" = {encoded_str}')

print('-' * 15 + 'deccoded string' + '-' * 15)
print(f'"{decode(encoded_str)}"')

print('-' * 50)




