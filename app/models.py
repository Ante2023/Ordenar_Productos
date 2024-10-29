"""
    Módulo donde se definen las clases y sus atributos para instancias objetos. Paradigma de POO  
    
    __init__: Es un método especial que se ejecuta al instanciar la clase creando un objeto.   
"""
class ProductSales:
    
    
    def __init__(self, productId, sales):
        self.productId = productId
        self.sales = sales


class ProductStock:
    def __init__(self, productId, stock):
        self.productId = productId
        self.stock = stock