# Proyecto: Sistema de Ordenamiento de Productos v.1.0.0

## El Problema:
Una pequeña empresa de venta de productos en línea ofrece una amplia variedad de artículos en categorías como libros, videoconsolas y ropa. Recientemente, ha cerrado acuerdos con cinco proveedores de productos comestibles, ampliando las categorías. Hasta ahora, el departamento de marketing organizaba los productos manualmente, utilizando criterios intuitivos para maximizar las ventas. Con la expansión, marketing ha solicitado al departamento de sistemas que automatice este proceso de ordenación.

## Plantéo de la solución:
   1. Crear un endpoint que reciba datos de productos y devuelva una
     lista ordenada de productos según ciertos criterios.

        1.1 Entrada del Endpoint:
        - Dos listas en formato JSON:
            * ProductSales: productos con ventas en euros (€) en las
                últimas 72 horas.
            * ProductStock: productos con su stock actual
                (número de unidades).

        1.2 Salida del Endpoint:
        - Lista ordenada de identificadores de productos, de mayor a menor
            prioridad.

   2. Criterios de Ordenación:
        - Basar la ordenación en ventas recientes y stock disponible.
        - Las ponderaciones de ventas y stock deben ser configurables (ej. 25% para ventas y 75% para stock).

   3. Configurabilidad:
        - El endpoint debe permitir configurar ponderaciones para ventas y stock.

## Resultados de la implenetación.

### API de Ordenación de Productos

Esta es una API RESTful construida con el microframework Flask que permite ordenar productos según el valor de sus ventas y stock. 

### Instalación

1. Clonar el repositorio.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux o Mac
   venv\Scripts\activate     # En Windows

4. Instala las dependencias

    ```bash 
    pip install -r requirements.txt
    ```
5. Ejecución: Ejecuta la aplicación con el siguiente comando:
    ```bash 
    python main.py
    ```

6. Uso del Endpoint: Para probar el endpoint, usa el siguiente cURL:

```bash 
curl -X POST 'http://localhost:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000},
    {"productId": "2", "sales": 100000},
    {"productId": "3", "sales": 100000},
    {"productId": "4", "sales": 75000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000},
    {"productId": "2", "stock": 400000},
    {"productId": "3", "stock": 200000},
    {"productId": "4", "stock": 300000}
  ]
}'
```
7. Respuesta: La respuesta será una lista de identificadores de productos ordenada de mayor a menor prioridad.

```bash
@mihp:~$ curl -X POST 'http://localhost:8080/sort-products' -H 'Content-Type: application/json' -d '{
  "salesWeight": 0.5,
  "stockWeight": 0.5,
  "productSales": [
    {"productId": "1", "sales": 50000},
    {"productId": "2", "sales": 100000},
    {"productId": "3", "sales": 100000},
    {"productId": "4", "sales": 75000}
  ],
  "productStock": [
    {"productId": "1", "stock": 100000},
    {"productId": "2", "stock": 400000},
    {"productId": "3", "stock": 200000},
    {"productId": "4", "stock": 300000}
  ]
}'
#output
[
  "2",
  "4",
  "3",
  "1"
]
```

### Conclusión

Con esta estructura, se obtiene una API RESTful básica usando Flask y cumpliendo con los requisitos de la especificación de alineamiento. 

