# app/auth/membership.py
from datetime import date
from fastapi import HTTPException


def validate_membership(user: dict):
    inicio = date.fromisoformat(user["FechaInicioMembresia"])
    fin = date.fromisoformat(user["FechaFinMembresia"])
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
