"""
PROYECTO FINAL POO
Autores: Miguel Angel Nivia y Jose Manuel García
Códigos: 8958691, 8959600
Funcionalidad General: Archivo.py que contiene la clase de Exampletest,
para respectivas pruebas unitarias.
Asignatura: POO
"""


import unittest

import utils


class ExampleTest(unittest.TestCase):

    # aserción/test de verificación = 1
    def test_acumulado_porcentaje(self):
        self.assertEqual(utils.acumulado_porcentaje(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2), True)

    # aserción/test de verificación = número
    def test_numero_a_palabra(self):
        self.assertTrue(utils.numero_a_palabras(0.5))
        self.assertTrue(utils.numero_a_palabras(1.8))
        self.assertTrue(utils.numero_a_palabras(2.4))
        self.assertTrue(utils.numero_a_palabras(3.3))
        self.assertTrue(utils.numero_a_palabras(4.6))

    # Aserción/test de mirar si es igual
    def test_igualdad_descripcion(self):
        self.assertTrue(utils.igualdad_descripcion("Criterio Viejo", "Criterio Nuevo"))

    # Aserción/test de mirar si el nombre es un string o no
    def test_agregar_acta_nombre(self):
        self.assertFalse(utils.agregar_acta_nombre(0.0))

    # Aserción/test de mirar si es mayor a 3.5
    def test_nota_final(self):
        self.assertLess(utils.nota_final(4.0), 3.6)


if __name__ == '__main__':
    unittest.main()
