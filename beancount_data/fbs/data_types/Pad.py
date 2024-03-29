# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Pad(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Pad()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPad(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Pad
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Pad
    def Account(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Pad
    def SourceAccount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def PadStart(builder):
    builder.StartObject(2)

def Start(builder):
    PadStart(builder)

def PadAddAccount(builder, account):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(account), 0)

def AddAccount(builder, account):
    PadAddAccount(builder, account)

def PadAddSourceAccount(builder, sourceAccount):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(sourceAccount), 0)

def AddSourceAccount(builder, sourceAccount):
    PadAddSourceAccount(builder, sourceAccount)

def PadEnd(builder):
    return builder.EndObject()

def End(builder):
    return PadEnd(builder)
