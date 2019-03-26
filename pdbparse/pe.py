#!/usr/bin/env python

from construct import *

IMAGE_SECTION_HEADER = "IMAGE_SECTION_HEADER"/Struct(
    "Name"/PaddedString(8, "ascii"),
    "Misc"/Union(None,
        "PhysicalAddress"/Int32ul,
        "VirtualSize"/Int32ul,
    ),
    "VirtualAddress"/Int32ul,
    "SizeOfRawData"/Int32ul,
    "PointerToRawData"/Int32ul,
    "PointerToRelocations"/Int32ul,
    "PointerToLinenumbers"/Int32ul,
    "NumberOfRelocations"/Int32ul,
    "NumberOfLinenumbers"/Int32ul,
    "Characteristics"/Int32ul,
)

Sections = GreedyRange(IMAGE_SECTION_HEADER)
