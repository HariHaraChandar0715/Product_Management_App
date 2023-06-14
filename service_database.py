import mysql.connector


class ProductServiceDatabase():

    def __init__(
            self
    ):
        self.host = "localhost"
        self.user_name = "root"
        self.password = "Hari@2002"
        self.database = "Product"
        self.database_connection = None
        try:
            self.database_connection = mysql.connector.connect(
                host=self.host, user=self.user_name,
                password=self.password, database=self.database
            )
        except Exception as exception:
            print("exception :", exception)

    def insert(
            self, product
    ) -> None:
        self.product = product
        self.mycursor = self.database_connection.cursor()
        self.product_name = self.product.get_product_name()
        self.product_type = self.product.get_product_type()
        self.product_place = self.product.get_product_place()
        self.product_warrenty = self.product.get_product_warrenty()
        self.query = "INSERT INTO product_info(product_name,product_type,product_place,product_warrenty)VALUES(%s,%s,%s,%s)"
        self.values = (self.product_name, self.product_type,
                       self.product_place, self.product_warrenty)
        self.mycursor.execute(self.query, self.values)
        self.database_connection.commit()
        self.database_connection.close()
        print("Added Sucessfully!!!!")

    def view(
            self
    ):
        self.return_products = []
        self.mydict_cursor = self.database_connection.cursor(dictionary=True)
        self.query = "SELECT * FROM product_info"
        self.mydict_cursor.execute(self.query)
        # Fetching result
        self.return_products = self.mydict_cursor.fetchall()
        return self.return_products
