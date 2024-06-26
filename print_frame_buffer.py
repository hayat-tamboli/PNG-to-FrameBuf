#!/usr/bin/env python

import sys
import os

def main():

    with open('image.pbm', 'rb') as fd:
        pbm_format = fd.readline().strip()
        if pbm_format != b'P4':
            print("ERROR: input file must be binary PBM (type P4)",
                  file = "image.pbm")
            return 1
        pbm_dims = [int(d) for d in fd.readline().strip().split()]
        pbm_data = fd.read()

    fbbase = "fb_{0}".format(os.path.basename("image.pbm"))
    fbname = os.path.splitext(fbbase)[0]
    with sys.stdout as fd:
        f = "{0} = framebuf.FrameBuffer(bytearray({1}), {2}, {3}, framebuf.MONO_HLSB)\n"
        fd.write(f.format(fbname, str(pbm_data), pbm_dims[0], pbm_dims[1]))


def usage():
    print("""usage: {0} PBM_FILE""".format(os.path.basename("image.pbm")),
          file = sys.stderr)

if __name__ == '__main__':
    main()