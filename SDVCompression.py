import numpy as np
from urllib.request import urlopen
from scipy import misc
import matplotlib.pyplot as plt
from os import stat

def show(f):
    plt.imshow(f, cmap=plt.cm.gray)
    plt.show()

"""
kth_svd
given an m x n image, 

"""

def kth_svd(image, k):
    """

    :param image: image is a w by h numpy.array
    :param k: We will return the kth svd reconstruction of image
    :return: l, s, r, w, h, k
        l is an h by k numpy array
        s is a k length numpy array
        r is a k by w array
        w original image width
        h original image height
        k original k
    """
    h = image.shape[0]
    w = image.shape[1]
    l, s, r = np.linalg.svd(image)
    if k <= 0:
        k = len(s)
    return l[:, :k], s[:k], r[:k, :], w, h, k

def compress(image, k, out_file_name='compressed'):
    l, s, r, w, h, k = kth_svd(image, k)
    data = np.concatenate((l.flatten(), s.flatten(), r.flatten()))
    with open(out_file_name, 'wb') as output_file:
        np.array((w,h,k), dtype='uint32').tofile(output_file)
        data.tofile(output_file)
    return int(stat(out_file_name).st_size)


def extract(input_file_path):
    input_file_path = 'compressed'
    input_file = open(input_file_path, 'rb')
    w, h, k = np.fromfile(input_file, 'uint32', 3)

    l = np.fromfile(input_file, 'float32', h * k)
    l = l.reshape([h, k])
    l = np.pad(l, [(0, 0), (0, h-k)], 'constant', constant_values=0)

    s = np.fromfile(input_file, 'float32', k)
    s = s * np.identity(k)
    s = np.pad(s, [(0, h - k), (0, w - k)], 'constant', constant_values=0)

    r = np.fromfile(input_file, 'float32', k * w)
    r = r.reshape([k, w])
    r = np.pad(r, [(0, w-k), (0, 0)], 'constant', constant_values=0)

    input_file.close()

    return l.dot(s.dot(r))

def show_image_and_compressed_image(
        url='https://www.gettyimages.com/gi-resources/images/Embed/new/embed2.jpg',
        k=50):
    with urlopen(url) as file:
        image = misc.imread(file, mode='L', flatten=True)
    show(image)
    file_name = 'compressed'
    original_size = image.size # one byte per pixes
    compressed_size = compress(image, k, file_name)
    extracted = extract(file_name)
    show(extracted)
    print("compression factor: %f" % (compressed_size / original_size))

'''
l, s, r, compression = svd(image, k)
print("compressed by a factor of %f" % compression)
image_compressed = l.dot(s.dot(r))
show(image_compressed)
'''
show_image_and_compressed_image(k=20)