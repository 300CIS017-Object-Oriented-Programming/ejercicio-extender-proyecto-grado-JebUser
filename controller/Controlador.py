"""
Contiene la clase controlador e
internamente funcionalidades del criterio y otras.
Asignatura: POO
"""

from model.Criterio import Criterio


class Controlador:

    # Constructor
    def __init__(self) -> None:
        super().__init__()
        self.actas = []

        # Inicializa los criterios de evaluacion de bse
        self.__inicializar_criterios()

    # Método para agregar los objetos a la lista
    def agregar_evaluacion(self, info_acta_obj):
        self.actas.append(info_acta_obj)

    # Método privado con la información de la lista criterio
    def __inicializar_criterios(self):

        self.criterios = [Criterio("Desarrollo y profundidad en el tratamiento del tema", 0.2),
                 Criterio("Desafío académico y científico del tema", 0.15),
                 Criterio("Cumplimiento de los objetivos propuestos", 0.1),
                 Criterio("Creatividad e innovación de las soluciones y desarrollos propuestos", 0.1),
                 Criterio("Validez de los resultados y conclusiones", 0.2),
                 Criterio("Manejo y procesamiento de la información y bibliografía", 0.1),
                 Criterio("Calidad y presentación del documento escrito", 0.075),
                 Criterio("Presentación oral", 0.075)]

    def mostrar_de_numero_a_palabras(self, numero):
        """
        FIXME: mejorar la logica
        :param numero:
        :return:
        """
        numero = str(numero)
        primero = ""
        segundo = ""

        if numero[0] == "0":
            primero = "Cero"
        elif numero[0] == "1":
            primero = "Uno"
        elif numero[0] == "2":
            primero = "Dos"
        elif numero[0] == "3":
            primero = "Tres"
        elif numero[0] == "4":
            primero = "Cuatro"
        elif numero[0] == "5":
            primero = "Cinco"

        if numero[2] == "0":
            segundo = "cero"
        elif numero[2] == "1":
            segundo = "uno"
        elif numero[2] == "2":
            segundo = "dos "
        elif numero[2] == "3":
            segundo = "tres "
        elif numero[2] == "4":
            segundo = "cuatro "
        elif numero[2] == "5":
            segundo = "cinco "
        elif numero[2] == "6":
            segundo = "seis "
        elif numero[2] == "7":
            segundo = "siete "
        elif numero[2] == "8":
            segundo = "ocho"
        elif numero[2] == "9":
            segundo = "nueve"

        palabra = primero + " punto " + segundo
        return palabra


