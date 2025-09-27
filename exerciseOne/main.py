from builders.automovil_builder import AutomovilBuilder
from directors.automovil_director import AutomovilDirector
from enums import TipoMotor, Color


def main() -> None:
    # Usando director (presets)
    director = AutomovilDirector(AutomovilBuilder())
    auto_deportivo = director.deportivo()
    print(auto_deportivo)

    # Configuración ad-hoc con el builder
    auto_personalizado = (
        AutomovilBuilder()
        .set_motor(TipoMotor.ELECTRICO)
        .set_color(Color.NEGRO)
        .set_gps()
        .build()
    )
    print(auto_personalizado)

if __name__ == "__main__":
    main()
