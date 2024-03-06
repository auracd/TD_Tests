from carte_pizzeria_exception import cartePizzeriaException
from pizza import Pizza

class cartePizzeria(Pizza) : 

    def __init__(self):
        super().__init__()
        self._pizzas = []
    
    def __is_empty(self) : 

        if len(self._pizzas) == 0 : 
            print("La carte est vide") 
            return False 
        else : 
            print("La carte est remplie")
        return True 
    
    def __nb_pizzas(self) : 
        return len(self._pizzas)
    
    def add_pizza(self, Pizza) :

        self._pizzas.append(Pizza)

    def remove_pizza(self, name) : 
        try : 
            for p in self._pizzas : 
                if p.name == name : 
                    del p  
        except ValueError : 
            raise cartePizzeriaException("La pizza n'existe pas")