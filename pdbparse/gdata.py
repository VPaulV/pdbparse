# Python 2 and 3
from io import BytesIO

from construct import *
from pdbparse.tpi import merge_subcon

gsym = "global"/Struct(
    "leaf_type"/Int16ul,
    "data"/Embed(Switch(lambda ctx: ctx.leaf_type,
        {
            0x110E : "data_v3"/Struct(,
                "symtype"/Int32ul,
                "offset"/Int32ul,
                "segment"/Int16ul,
                "name"/CString("utf8"),

            ),
            0x1009 : "data_v2"/Struct(
                "symtype"/Int32ul,
                "offset"/Int32ul,
                "segment"/Int16ul,
                "name"/PascalString(VarInt, "utf8"),
            ),
        },
        default = Pass,
    ))
)

#GlobalsData = OptionalGreedyRange(
#    Tunnel(
#        PascalString(VarInt, "utf16"),
#        gsym,
#    )
#)

GlobalsData = GreedyRange(
    PascalString(VarInt, "utf16"),
    gsym,
)

def parse(data):
    con = GlobalsData.parse(data)
    return con

def parse_stream(stream):
    con = GlobalsData.parse_stream(stream)
    return con
