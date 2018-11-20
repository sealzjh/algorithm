# -*- encoding: utf8 -*-

import glob
import os
import sys

from PIL import Image

class ImageHash(object):

    def __init__(self):
        self.EXTS = 'jpg', \
                    'jpeg', \
                    'JPG', \
                    'JPEG', \
                    'gif', \
                    'GIF', \
                    'png', \
                    'PNG'

    def avhash(self, image):
        im = Image.open(image)
        im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, im.getdata()) / 64.

        return reduce(lambda x, (y, z): x | (z << y),
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),
                  0)

    def hamming(self, h1, h2):
        h, d = 0, h1 ^ h2
        while d:
            h += 1
            d &= d - 1
        return h

    def run(self, image1, image2):
        h1 = self.avhash(image1)
        h2 = self.avhash(image2)
        print self.hamming(h1, h2)


if __name__ == "__main__":
    ImageHash().run(sys.argv[1], sys.argv[2])
