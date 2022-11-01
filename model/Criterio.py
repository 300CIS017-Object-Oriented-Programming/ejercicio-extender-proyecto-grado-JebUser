"""
Contiene la clase criterio,
que a su vez tiene un constructor con parámetros.
"""


class Criterio:

    # Constructor con parámetros
    def __init__(self, descripcion, porcentaje=0.0, nota=0.0, observacion=""):
        # Datos de criterio
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.nota = nota
        self.observacion = observacion
