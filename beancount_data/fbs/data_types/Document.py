# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Document(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Document()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDocument(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Document
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Document
    def Account(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Document
    def Filename(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Document
    def Tags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Document
    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Document
    def TagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Document
    def Links(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Document
    def LinksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Document
    def LinksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def DocumentStart(builder):
    builder.StartObject(4)

def Start(builder):
    DocumentStart(builder)

def DocumentAddAccount(builder, account):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(account), 0)

def AddAccount(builder, account):
    DocumentAddAccount(builder, account)

def DocumentAddFilename(builder, filename):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(filename), 0)

def AddFilename(builder, filename):
    DocumentAddFilename(builder, filename)

def DocumentAddTags(builder, tags):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tags), 0)

def AddTags(builder, tags):
    DocumentAddTags(builder, tags)

def DocumentStartTagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartTagsVector(builder, numElems: int) -> int:
    return DocumentStartTagsVector(builder, numElems)

def DocumentAddLinks(builder, links):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(links), 0)

def AddLinks(builder, links):
    DocumentAddLinks(builder, links)

def DocumentStartLinksVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartLinksVector(builder, numElems: int) -> int:
    return DocumentStartLinksVector(builder, numElems)

def DocumentEnd(builder):
    return builder.EndObject()

def End(builder):
    return DocumentEnd(builder)