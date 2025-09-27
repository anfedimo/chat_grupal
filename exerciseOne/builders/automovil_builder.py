from __future__ import annotations
from typing import Optional
from enums import (
    TipoMotor, Color, TipoLlantas, SistemaSonido, Interiores
)
from domain.automovil import Automovil
from exceptions import ValidacionConfiguracionError

class AutomovilBuilder:
    def __init__(self) -> None:
        self._motor: Optional[TipoMotor] = None
        self._color: Optional[Color] = None
        self._llantas: Optional[TipoLlantas] = None
        self._sonido: Optional[SistemaSonido] = None
        self._interiores: Optional[Interiores] = None
        self._gps: bool = False
        self._techo_solar: bool = False

    # Métodos "fluent"
    def set_motor(self, motor: TipoMotor) -> "AutomovilBuilder":
        self._motor = motor
        return self

    def set_color(self, color: Color) -> "AutomovilBuilder":
        self._color = color
        return self

    def set_llantas(self, llantas: TipoLlantas) -> "AutomovilBuilder":
        self._llantas = llantas
        return self

    def set_sonido(self, sonido: SistemaSonido) -> "AutomovilBuilder":
        self._sonido = sonido
        return self

    def set_interiores(self, interiores: Interiores) -> "AutomovilBuilder":
        self._interiores = interiores
        return self

    def set_gps(self, flag: bool = True) -> "AutomovilBuilder":
        self._gps = flag
        return self

    def set_techo_solar(self, flag: bool = True) -> "AutomovilBuilder":
        self._techo_solar = flag
        return self

    def _validar(self) -> None:
        if self._motor == TipoMotor.ELECTRICO and self._llantas == TipoLlantas.TODO_TERRENO:
            raise ValidacionConfiguracionError(
                "Configuración no válida: motor eléctrico con llantas todo terreno."
            )

    def build(self) -> Automovil:
        self._validar()
        return Automovil(
            motor=self._motor,
            color=self._color,
            llantas=self._llantas,
            sonido=self._sonido,
            interiores=self._interiores,
            gps=self._gps,
            techo_solar=self._techo_solar,
        )