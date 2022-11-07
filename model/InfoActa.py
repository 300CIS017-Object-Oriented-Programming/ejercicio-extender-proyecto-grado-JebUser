"""
Contiene la clase InfoActa e
internamente tiene sus respectivos atributos.
Asignatura: POO
"""


class InfoActa:

    # Constructor
    def __init__(self, criterios) -> None:
        super().__init__()

        # Datos del acta
        self.autor = ""
        self.fecha_acta = ""
        self.nombre_trabajo = ""
        self.tipo_trabajo = ""
        self.director = ""
        self.codirector = " "
        self.jurado1 = ""
        self.jurado2 = ""
        self.jurado1EST = ""
        self.jurado2EST = ""
        self.nota_final = 0.0
        self.criterios = criterios
        self.estado = False
        self.fecha_presentacion = ""
        self.visto = False
