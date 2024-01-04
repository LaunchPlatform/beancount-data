# automatically generated by the FlatBuffers compiler, do not modify

# namespace: data_types

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Open(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Open()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOpen(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Open
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Open
    def Account(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Open
    def Currencies(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Open
    def CurrenciesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Open
    def CurrenciesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Open
    def Booking(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def OpenStart(builder):
    builder.StartObject(3)

def Start(builder):
    OpenStart(builder)

def OpenAddAccount(builder, account):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(account), 0)

def AddAccount(builder, account):
    OpenAddAccount(builder, account)

def OpenAddCurrencies(builder, currencies):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(currencies), 0)

def AddCurrencies(builder, currencies):
    OpenAddCurrencies(builder, currencies)

def OpenStartCurrenciesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartCurrenciesVector(builder, numElems: int) -> int:
    return OpenStartCurrenciesVector(builder, numElems)

def OpenAddBooking(builder, booking):
    builder.PrependInt8Slot(2, booking, 0)

def AddBooking(builder, booking):
    OpenAddBooking(builder, booking)

def OpenEnd(builder):
    return builder.EndObject()

def End(builder):
    return OpenEnd(builder)