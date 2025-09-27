from builders.automovil_builder import AutomovilBuilder
from enums import TipoMotor, Color, TipoLlantas, SistemaSonido, Interiores
from domain.automovil import Automovil

class AutomovilDirector:
    def __init__(self, builder: AutomovilBuilder) -> None:
        self.builder = builder

    def deportivo(self) -> Automovil:
        return (
            self.builder
            .set_motor(TipoMotor.V8)
            .set_color(Color.ROJO)
            .set_llantas(TipoLlantas.DEPORTIVAS)
            .set_sonido(SistemaSonido.BOSE)
            .set_interiores(Interiores.CUERO)
            .set_techo_solar(True)
            .build()
        )

    def eco(self) -> Automovil:
        return (
            self.builder
            .set_motor(TipoMotor.ELECTRICO)
            .set_color(Color.AZUL)
            .set_llantas(TipoLlantas.ESTANDAR)
            .set_gps(True)
            .build()
        )
