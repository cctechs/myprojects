#encoding=utf-8

import os
import struct
import numpy as np

def load_mnist(path, kind='train'):
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte'%kind)

    image_path = os.path.join(path, '%s-images-idx3-ubyte'%kind)

    print(labels_path)
    print(image_path)

    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>||', lbpath.read(8))

        labels = np.fromfile(lbpath, dtype=np.uint8)

    with open(image_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>|||', imgpath.read(16))

        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels



if __name__ == '__main__':
    a, b = load_mnist('./mnist')
    print(a, b)