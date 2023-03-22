import datetime
import decimal
import enum
import typing

import pydantic
from pydantic import Field


Account = str
Flag = str
Meta = typing.Dict[str, typing.Any]


@enum.unique
class Booking(enum.Enum):
    STRICT = "STRICT"
    NONE = "NONE"
    AVERAGE = "AVERAGE"
    FIFO = "FIFO"
    LIFO = "LIFO"


@enum.unique
class EntryType(enum.Enum):
    OPEN = "open"
    CLOSE = "close"
    COMMODITY = "commodity"
    PAD = "pad"
    BALANCE = "balance"
    TRANSACTION = "transaction"
    NOTE = "note"
    EVENT = "event"
    PRICE = "price"
    DOCUMENT = "document"
    CUSTOM = "custom"


class BaseModel(pydantic.BaseModel):
    class Config:
        orm_mode = True


class Amount(BaseModel):
    number: typing.Optional[decimal.Decimal]
    currency: str


class EntryBase(BaseModel):
    meta: Meta
    date: datetime.date


class Cost(BaseModel):
    number: decimal.Decimal
    currency: str
    date: datetime.date
    label: typing.Optional[str]


class CostSpec(BaseModel):
    number_per: typing.Optional[decimal.Decimal]
    number_total: typing.Optional[decimal.Decimal]
    currency: typing.Optional[str]
    date: datetime.date
    label: typing.Optional[str]
    merge: typing.Optional[bool]


class Open(EntryBase):
    entry_type: EntryType = Field(EntryType.OPEN, const=EntryType.OPEN)
    account: Account
    currencies: typing.Optional[typing.List[str]]
    booking: typing.Optional[Booking]


class Close(EntryBase):
    entry_type: EntryType = Field(EntryType.CLOSE, const=EntryType.CLOSE)
    account: Account


class Commodity(EntryBase):
    entry_type: EntryType = Field(EntryType.COMMODITY, const=EntryType.COMMODITY)
    currency: str


class Pad(EntryBase):
    entry_type: EntryType = Field(EntryType.PAD, const=EntryType.PAD)
    account: Account
    source_account: str


class Balance(EntryBase):
    entry_type: EntryType = Field(EntryType.BALANCE, const=EntryType.BALANCE)
    account: Account
    amount: Amount
    tolerance: typing.Optional[decimal.Decimal]
    diff_amount: typing.Optional[Amount]


class Posting(BaseModel):
    account: Account
    units: Amount
    cost: typing.Optional[typing.Union[Cost, CostSpec]]
    price: typing.Optional[Amount]
    flag: typing.Optional[Flag]
    meta: typing.Optional[Meta]


class Transaction(EntryBase):
    entry_type: EntryType = Field(EntryType.TRANSACTION, const=EntryType.TRANSACTION)
    flag: Flag
    payee: typing.Optional[str]
    narration: str
    tags: typing.Set[str]
    links: typing.Set[str]
    postings: typing.List[Posting]


class Note(EntryBase):
    entry_type: EntryType = Field(EntryType.NOTE, const=EntryType.NOTE)
    account: Account
    comment: str
    tags: typing.Set[str]
    links: typing.Set[str]


class Event(EntryBase):
    entry_type: EntryType = Field(EntryType.EVENT, const=EntryType.EVENT)
    type: str
    description: str


class Price(EntryBase):
    entry_type: EntryType = Field(EntryType.PRICE, const=EntryType.PRICE)
    currency: str
    amount: Amount


class Document(EntryBase):
    entry_type: EntryType = Field(EntryType.DOCUMENT, const=EntryType.DOCUMENT)
    account: Account
    filename: str
    tags: typing.Set[str]
    links: typing.Set[str]


class Custom(EntryBase):
    entry_type: EntryType = Field(EntryType.CUSTOM, const=EntryType.CUSTOM)
    type: str
    values: typing.List[typing.Union[Amount, decimal.Decimal, str, bool]]


EntryUnion = typing.Union[
    Open,
    Close,
    Commodity,
    Pad,
    Balance,
    Transaction,
    Note,
    Event,
    Price,
    Document,
    Custom,
]


class ValidationError(BaseModel):
    source: Meta
    message: str
    entry: typing.Optional[EntryUnion]


class ValidationResult(BaseModel):
    errors: typing.List[ValidationError]
