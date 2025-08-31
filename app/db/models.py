from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Boolean, Enum, DateTime, Text
from datetime import datetime
import enum

class Base(DeclarativeBase): pass

class DocType(str, enum.Enum):
    contract = "contract"
    invoice = "invoice"
    act = "act"
    taxinvoice = "taxinvoice"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    full_name: Mapped[str | None] = mapped_column(String(255))
    iin: Mapped[str | None] = mapped_column(String(12))
    phone10: Mapped[str | None] = mapped_column(String(10))
    email: Mapped[str | None] = mapped_column(String(255))
    google_connected: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

class Company(Base):
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(255))
    bin_iin: Mapped[str] = mapped_column(String(12))
    bank: Mapped[str | None] = mapped_column(String(255))
    bik: Mapped[str | None] = mapped_column(String(20))
    kbe: Mapped[str | None] = mapped_column(String(4))
    iban: Mapped[str | None] = mapped_column(String(34))
    is_default: Mapped[bool] = mapped_column(Boolean, default=False)

class Counterparty(Base):
    __tablename__ = "counterparties"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(255))
    bin_iin: Mapped[str] = mapped_column(String(12))
    bank: Mapped[str | None] = mapped_column(String(255))
    iban: Mapped[str | None] = mapped_column(String(34))
    contact: Mapped[str | None] = mapped_column(String(255))

class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    company_id: Mapped[int | None] = mapped_column(ForeignKey("companies.id"))
    counterparty_id: Mapped[int | None] = mapped_column(ForeignKey("counterparties.id"))
    doc_type: Mapped[DocType] = mapped_column(Enum(DocType))
    number: Mapped[str | None] = mapped_column(String(64))
    amount: Mapped[int | None] = mapped_column()
    vat_mode: Mapped[str | None] = mapped_column(String(16))
    gdrive_path: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(32), default="issued")
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
