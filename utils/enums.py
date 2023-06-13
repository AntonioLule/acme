# Enum
from enum import Enum

# Categorias disponibles
class Category(Enum):
    GROCERY = 'ABARROTES'
    PHARMACY = 'FARMACIA'
    ELECTRONICS = 'ELECTRÓNICA'

# Tipo de operación
class TypeOperation(Enum):
    BUY = 'COMPRA'
    SALE = 'VENTA'