# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Event(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Event()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEvent(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Event
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Event
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Event
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def EventStart(builder):
    builder.StartObject(2)

def Start(builder):
    EventStart(builder)

def EventAddType(builder, type):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(type), 0)

def AddType(builder, type):
    EventAddType(builder, type)

def EventAddDescription(builder, description):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder, description):
    EventAddDescription(builder, description)

def EventEnd(builder):
    return builder.EndObject()

def End(builder):
    return EventEnd(builder)
