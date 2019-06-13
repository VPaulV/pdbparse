#!/usr/bin/env python
from __future__ import print_function

import sys
import pdbparse
from optparse import OptionParser

from pdbparse.pe import Sections
from pdbparse.omap import Omap

from pprint import pprint

class DummyOmap(object):

    def remap(self, addr):
        return addr


def cstring(str):
    return str.split('\0')[0]


def main(filename, base_address):
    pdb = pdbparse.parse(filename)
    imgbase = int(base_address, 0)
    try:
        sects = pdb.STREAM_SECT_HDR_ORIG.sections
        omap = pdb.STREAM_OMAP_FROM_SRC
    except AttributeError as e:
        sects = pdb.STREAM_SECT_HDR.sections
        omap = DummyOmap()

    gsyms = pdb.STREAM_GSYM

    for sym in gsyms.globals:
        try:
            off = sym.offset
            virt_base = sects[sym.segment - 1].VirtualAddress
            nm = cstring(sects[sym.segment - 1].Name)
            print("%s,%#x,%d" % (sym.name, imgbase + omap.remap(off + virt_base), sym.symtype))
        except:
            pass


if __name__ == '__main__':

    parser = OptionParser()
    (opts, args) = parser.parse_args()
	
    #filename and address
    main(args[0], args[1])
