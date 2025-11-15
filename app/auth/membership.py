# app/auth/membership.py
from datetime import date
from fastapi import HTTPException


def validate_membership(user: dict):
    inicio = date.fromisoformat(user["membership_start"])
    fin = date.fromisoformat(user["membership_end"])
    hoy = date.today()

    if hoy < inicio:
        raise HTTPException(
            status_code=403,
            detail="⛔ La membresía aún no está activa."
        )

    if hoy > fin:
        raise HTTPException(
            status_code=403,
            detail="⛔ Tu membresía expiró. Renueva para continuar."
        )

    return True
