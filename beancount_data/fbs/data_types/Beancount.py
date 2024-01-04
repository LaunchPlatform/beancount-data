# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Beancount(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Beancount()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBeancount(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Beancount
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Beancount
    def ExporterVersion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Beancount
    def Entries(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from beancount_data.fbs.data_types.Entry import Entry
            obj = Entry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Beancount
    def EntriesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Beancount
    def EntriesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def BeancountStart(builder):
    builder.StartObject(2)

def Start(builder):
    BeancountStart(builder)

def BeancountAddExporterVersion(builder, exporterVersion):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(exporterVersion), 0)

def AddExporterVersion(builder, exporterVersion):
    BeancountAddExporterVersion(builder, exporterVersion)

def BeancountAddEntries(builder, entries):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(entries), 0)

def AddEntries(builder, entries):
    BeancountAddEntries(builder, entries)

def BeancountStartEntriesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartEntriesVector(builder, numElems: int) -> int:
    return BeancountStartEntriesVector(builder, numElems)

def BeancountEnd(builder):
    return builder.EndObject()

def End(builder):
    return BeancountEnd(builder)