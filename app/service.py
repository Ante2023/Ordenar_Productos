def sort_products(sales_weight, stock_weight, product_sales, product_stock):
    # Nos aseguramos que la suma de sales_weight y stock_weight sea 1
    if sales_weight + stock_weight != 1:
        raise ValueError("La suma de salesWeight y stockWeight debe ser 1.")
    scores={}
    
    #Buscamos desde 2 listas diferentes un mimo producto por el mismo id
    for sale in product_sales:
        product_id = sale['productId']
        sales = sale['sales']
        stock = 0  
        for item in product_stock:
            if item['productId'] == product_id:
                stock = item['stock']
                break  # Rompo bucle cuando coinciden ambos ids
            
    # Calculamos la puntuación en función de ponderación y valor
        score = (sales * sales_weight) + (stock * stock_weight)
        scores[product_id] = score

    # Ordenamos los productos según la puntuación
    sorted_products = sorted(scores, key=scores.get, reverse=True)
    
    return sorted_products