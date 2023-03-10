import heapq
from collections import Counter, namedtuple
class HuffmanNode(namedtuple("HuffmanNode", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")
class LeafNode(namedtuple("LeafNode", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), LeafNode(ch)))
# Build heap
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, HuffmanNode(left, right)))
        count += 1
    code = {}
    if h:
         [(_freq, _count, root)] = h
         root.walk(code, "")
    return code
def compress(text):
    huff = huffman_encode(text)
    encoded = "".join(huff[ch] for ch in text)
    ratio = len(encoded) / ( 8.0 * len(text))
    return encoded, huff, ratio
def decompress(encoded, huff):
    reverse_huff = {huff[ch]: ch for ch in huff}
    current_code = ""
    decoded = ""
    for bit in encoded:
        current_code += bit
        if current_code in reverse_huff:
            character = reverse_huff[current_code]
            decoded += character
            current_code = ""
        return decoded
def main():
    file_name = input("Enter a filename: ")
    with open(file_name) as f:
        text = f.read()
    encoded, huff, ratio = compress(text)
    print("Compression ratio: %f" % ratio)
    with open("encoded.bin", "wb") as f:
        f.write(bytes(encoded, "utf-8"))
    with open("code_table.txt", "w") as f:
        for char in huff:
            f.write("%s: %s\n" % (char, huff[char]))
    decoded = decompress(encoded, huff)
    with open("decoded.txt", "w") as f:
        f.write(decoded)
main()