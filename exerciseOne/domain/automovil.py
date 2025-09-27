from dataclasses import dataclass
from typing import Optional
from enums import (
    TipoMotor, Color, TipoLlantas, SistemaSonido, Interiores
)

@dataclass(frozen=True, slots=True)
class Automovil:
    motor: Optional[TipoMotor] = None
    color: Optional[Color] = None
    llantas: Optional[TipoLlantas] = None
    sonido: Optional[SistemaSonido] = None
    interiores: Optional[Interiores] = None
    gps: bool = False
    techo_solar: bool = False

    def __str__(self) -> str:
        return (
            f"Automóvil(motor={self.motor.value if self.motor else None}, "
            f"color={self.color.value if self.color else None}, "
            f"llantas={self.llantas.value if self.llantas else None}, "
            f"sonido={self.sonido.value if self.sonido else None}, "
            f"interiores={self.interiores.value if self.interiores else None}, "
            f"gps={self.gps}, techo_solar={self.techo_solar})"
        )
