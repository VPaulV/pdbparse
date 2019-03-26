from construct import *
from io import BytesIO

_strarray = GreedyRange(CString("utf8"))

class StringArrayAdapter(Adapter):
    def _encode(self, obj, context, path):
        return _strarray._build(BytesIO(obj), context, path)
    def _decode(self, obj, context, path):
        a = _strarray._parse(BytesIO(obj), context, path)

def GUID(name):
    return name/Struct(
        "time_low"/Int32ul,
        "time_mid"/Int16ul,
        "time_hi_and_version"/Int16ul,
        "clock_seq"/Int16ul,
        "node"/Bytes(6),
    )

Info = "Info"/Struct(
    "Version"/Int32ul,
    "TimeDateStamp"/Int32ul,
    "Age"/Int32ul,
    GUID("GUID"),
    "cbNames"/Int32ul,
    "names"/StringArrayAdapter(Bytes(lambda ctx: ctx.cbNames)),
)

def parse_stream(stream):
    #dir(stream)
    return Info.parse_stream(stream)

def parse(data):
    return Info.parse(data)

