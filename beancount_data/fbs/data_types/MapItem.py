# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MapItem(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MapItem()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMapItem(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MapItem
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MapItem
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MapItem
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # MapItem
    def StringValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MapItem
    def IntValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MapItem
    def BoolValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MapItem
    def JsonValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MapItem
    def BsonValue(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # MapItem
    def BsonValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # MapItem
    def BsonValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MapItem
    def BsonValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def MapItemStart(builder):
    builder.StartObject(7)

def Start(builder):
    MapItemStart(builder)

def MapItemAddKey(builder, key):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)

def AddKey(builder, key):
    MapItemAddKey(builder, key)

def MapItemAddType(builder, type):
    builder.PrependInt8Slot(1, type, 0)

def AddType(builder, type):
    MapItemAddType(builder, type)

def MapItemAddStringValue(builder, stringValue):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(stringValue), 0)

def AddStringValue(builder, stringValue):
    MapItemAddStringValue(builder, stringValue)

def MapItemAddIntValue(builder, intValue):
    builder.PrependInt32Slot(3, intValue, 0)

def AddIntValue(builder, intValue):
    MapItemAddIntValue(builder, intValue)

def MapItemAddBoolValue(builder, boolValue):
    builder.PrependBoolSlot(4, boolValue, 0)

def AddBoolValue(builder, boolValue):
    MapItemAddBoolValue(builder, boolValue)

def MapItemAddJsonValue(builder, jsonValue):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(jsonValue), 0)

def AddJsonValue(builder, jsonValue):
    MapItemAddJsonValue(builder, jsonValue)

def MapItemAddBsonValue(builder, bsonValue):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(bsonValue), 0)

def AddBsonValue(builder, bsonValue):
    MapItemAddBsonValue(builder, bsonValue)

def MapItemStartBsonValueVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartBsonValueVector(builder, numElems: int) -> int:
    return MapItemStartBsonValueVector(builder, numElems)

def MapItemEnd(builder):
    return builder.EndObject()

def End(builder):
    return MapItemEnd(builder)