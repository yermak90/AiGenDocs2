from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def reserve_number(db: AsyncSession, company_id: int, kind: str) -> str:
    # простая маска: <Префикс>/<Год>/<Счётчик>
    year = datetime.utcnow().year
    q = text("""
        INSERT INTO numerators(company_id, kind, year, counter)
        VALUES (:company_id, :kind, :year, 1)
        ON CONFLICT (company_id, kind, year)
        DO UPDATE SET counter = numerators.counter + 1
        RETURNING counter
    """)
    res = await db.execute(q, {"company_id": company_id, "kind": kind, "year": year})
    counter = res.scalar_one()
    prefix = {"contract":"CTR","invoice":"INV","act":"ACT","taxinvoice":"TI"}.get(kind, "DOC")
    return f"{prefix}/{year}/{counter:05d}"
