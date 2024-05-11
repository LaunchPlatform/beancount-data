import datetime
import decimal
import enum
import typing

import pydantic
from pydantic import ConfigDict
from typing import Literal


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
    model_config = ConfigDict(from_attributes=True)


class Amount(BaseModel):
    number: typing.Optional[decimal.Decimal] = None
    currency: str


class EntryBase(BaseModel):
    meta: Meta
    date: datetime.date


class Cost(BaseModel):
    number: decimal.Decimal
    currency: str
    date: datetime.date
    label: typing.Optional[str] = None


class CostSpec(BaseModel):
    number_per: typing.Optional[decimal.Decimal] = None
    number_total: typing.Optional[decimal.Decimal] = None
    currency: typing.Optional[str] = None
    date: datetime.date
    label: typing.Optional[str] = None
    merge: typing.Optional[bool] = None


class Open(EntryBase):
    entry_type: Literal[EntryType.OPEN] = EntryType.OPEN
    account: Account
    currencies: typing.Optional[typing.List[str]] = None
    booking: typing.Optional[Booking] = None


class Close(EntryBase):
    entry_type: Literal[EntryType.CLOSE] = EntryType.CLOSE
    account: Account


class Commodity(EntryBase):
    entry_type: Literal[EntryType.COMMODITY] = EntryType.COMMODITY
    currency: str


class Pad(EntryBase):
    entry_type: Literal[EntryType.PAD] = EntryType.PAD
    account: Account
    source_account: str


class Balance(EntryBase):
    entry_type: Literal[EntryType.BALANCE] = EntryType.BALANCE
    account: Account
    amount: Amount
    tolerance: typing.Optional[decimal.Decimal] = None
    diff_amount: typing.Optional[Amount] = None


class Posting(BaseModel):
    account: Account
    units: Amount
    cost: typing.Optional[typing.Union[Cost, CostSpec]] = None
    price: typing.Optional[Amount] = None
    flag: typing.Optional[Flag] = None
    meta: typing.Optional[Meta] = None


class Transaction(EntryBase):
    entry_type: Literal[EntryType.TRANSACTION] = EntryType.TRANSACTION
    flag: Flag
    payee: typing.Optional[str] = None
    narration: str
    tags: typing.Set[str]
    links: typing.Set[str]
    postings: typing.List[Posting]


class Note(EntryBase):
    entry_type: Literal[EntryType.NOTE] = EntryType.NOTE
    account: Account
    comment: str
    tags: typing.Set[str]
    links: typing.Set[str]


class Event(EntryBase):
    entry_type: Literal[EntryType.EVENT] = EntryType.EVENT
    type: str
    description: str


class Price(EntryBase):
    entry_type: Literal[EntryType.PRICE] = EntryType.PRICE
    currency: str
    amount: Amount


class Document(EntryBase):
    entry_type: Literal[EntryType.DOCUMENT] = EntryType.DOCUMENT
    account: Account
    filename: str
    tags: typing.Set[str]
    links: typing.Set[str]


class Custom(EntryBase):
    entry_type: Literal[EntryType.CUSTOM] = EntryType.CUSTOM
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
    entry: typing.Optional[EntryUnion] = None


class ValidationResult(BaseModel):
    errors: typing.List[ValidationError]
