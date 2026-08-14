from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class InvoiceCreate(BaseModel):
    supplier: str
    invoice_number: str
    invoice_date: date
    subtotal: Decimal
    tax: Decimal
    total: Decimal
    currency: str