from service_database import ProductServiceDatabase


class ProductService():

    def add_product(
            self, product
    ) -> None:
        self.product = product
        productservice = ProductServiceDatabase()
        productservice.insert(self.product)

    def get_all_products(
            self
    ) -> dict:
        productservice = ProductServiceDatabase()
        return productservice.view()

    def get_product(
            self, product_name: str
    ) -> list:
        return self.products
