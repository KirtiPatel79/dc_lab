from scipy.fftpack import dct
import heapq
from PIL import Image
import numpy as np

img = Image.open("034.jpg").convert("L")
img = np.array(img)
def zigzag(input):
    return np.concatenate([np.diagonal(input[::-1,:], i)[::(2*(i % 2)-1)] for i in range(1-
    input.shape[0], input.shape[0])]) 
def rle_encode(arr):
    rle = []
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
        else:
            rle.append(count)
            rle.append(arr[i])
            count = 0 
    rle.append(count) 
    return rle
def huffman_encoding(arr):
    freq_dict = {}
    for i in range(len(arr)):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = 1
        else:
            freq_dict[arr[i]] += 1
    heap = [[freq, [val, ""]] for val, freq in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    huff_dict = dict(heapq.heappop(heap)[1:])
    huff_encoded = ""
    for i in range(len(arr)):
        huff_encoded += huff_dict[arr[i]]
    return huff_encoded, huff_dict
height, width = img.shape
if height % 8 != 0:
    pad_height = 8 - (height % 8)
else:
    pad_height = 0
if width % 8 != 0:
    pad_width = 8 - (width % 8)
else:
    pad_width = 0
img = np.pad(img, ((0, pad_height), (0, pad_width)), mode='constant')
dct_blocks = np.zeros(img.shape)
for i in range(0, img.shape[0], 8):
    for j in range(0, img.shape[1], 8):
        dct_blocks[i:i+8, j:j+8] = dct(dct(img[i:i+8, j:j+8].T).T)
quant = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],[72, 92, 95, 98, 112, 100, 103, 99]])
quant_blocks = np.zeros(img.shape)
for i in range(0, img.shape[0], 8):
    for j in range(0, img.shape[1], 8):
        quant_blocks[i:i+8, j:j+8] = np.round(dct_blocks[i:i+8, j:j+8] / quant)
rle_compressed = []
for i in range(0, img.shape[0], 8):
    for j in range(0, img.shape[1], 8):
        rle_block = rle_encode(zigzag(quant_blocks[i:i+8, j:j+8]))
rle_compressed.extend(rle_block)
huff_encoded, huff_dict = huffman_encoding(rle_compressed)
with open("huff_dict.txt", "w") as f:
    for key, value in huff_dict.items():
        f.write(str(key) + ":" + str(value) + "\n")
binary_encoded = ""
for char in huff_encoded:
    binary_encoded += huff_dict[int(char)]
while len(binary_encoded) % 8 != 0:
    binary_encoded += "0"
with open("output.bin", "wb") as f:
    for i in range(0, len(binary_encoded), 8):
        f.write(bytes([int(binary_encoded[i:i+8], 2)]))
