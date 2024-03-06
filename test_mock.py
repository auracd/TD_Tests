
import unittest
from unittest.mock import Mock
from carte_pizzeria import cartePizzeria

class testMock(unittest.TestCase) : 
    def test_is_empty(self) : 
        pizza = Mock()
        carte_p = cartePizzeria()
        carte_p._pizzas = [pizza]
        assert not carte_p.is_empty()
        
        

