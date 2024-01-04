# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Custom(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Custom()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCustom(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Custom
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Custom
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Custom
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from beancount_data.fbs.data_types.CustomValue import CustomValue
            obj = CustomValue()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Custom
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Custom
    def ValuesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def CustomStart(builder):
    builder.StartObject(2)

def Start(builder):
    CustomStart(builder)

def CustomAddType(builder, type):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(type), 0)

def AddType(builder, type):
    CustomAddType(builder, type)

def CustomAddValues(builder, values):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)

def AddValues(builder, values):
    CustomAddValues(builder, values)

def CustomStartValuesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartValuesVector(builder, numElems: int) -> int:
    return CustomStartValuesVector(builder, numElems)

def CustomEnd(builder):
    return builder.EndObject()

def End(builder):
    return CustomEnd(builder)