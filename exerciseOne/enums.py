from enum import Enum

class TipoMotor(Enum):
    V8 = "V8"
    ELECTRICO = "ELECTRICO"
    HIBRIDO = "HIBRIDO"

class Color(Enum):
    ROJO = "ROJO"
    AZUL = "AZUL"
    NEGRO = "NEGRO"
    BLANCO = "BLANCO"

class TipoLlantas(Enum):
    DEPORTIVAS = "DEPORTIVAS"
    TODO_TERRENO = "TODO_TERRENO"
    ESTANDAR = "ESTANDAR"

class SistemaSonido(Enum):
    BOSE = "BOSE"
    HARMAN = "HARMAN"
    ESTANDAR = "ESTANDAR"

class Interiores(Enum):
    CUERO = "CUERO"
    TELA = "TELA"
    MIXTO = "MIXTO"
