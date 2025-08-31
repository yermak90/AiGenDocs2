async def ensure_user_tree(google_creds, full_name: str) -> dict:
    # Drive:/Users/{ФИО}/(ID|Contracts|Invoices|Acts|TaxInvoices|Counterparties|Uploads)
    # Верните id созданных папок; сохраняйте в БД.
    return {"root_id": "drv_root_id"}
