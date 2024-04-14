from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.stor_id, products.price_per_unit, stor.stor_name "
        "FROM products INNER JOIN stor ON products.stor_id = stor.stor_id")

    cursor.execute(query)

    response = []

    for (product_id, name, stor_id, price_per_unit, stor_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'stor_id': stor_id,
                'price_per_unit': price_per_unit,
                'stor_name': stor_name
            }
        )


    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, stor_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['stor_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 11))