from fastapi import FastAPI

from app.schemas.invoice import InvoiceCreate


app = FastAPI(
    title="Invoice Automation API",
    description="API for automated invoice processing",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Invoice Automation API is running"}


@app.post("/invoices")
def create_invoice(invoice: InvoiceCreate):
    return invoice