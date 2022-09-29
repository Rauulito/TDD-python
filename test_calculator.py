# Cargamos el módulo unittest
import unittest

#importamos la clase calculadora
from calculator import Calculator
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
# Creamos una prueba para probar un valor inicial
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)



