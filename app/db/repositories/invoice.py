from sqlalchemy.orm import Session

from app.db.models import Invoice


def create_invoice(db: Session, invoice: Invoice) -> Invoice:
    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice