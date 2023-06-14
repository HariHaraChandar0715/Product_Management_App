class Product():
    def __init__(
            self,
            product_name: str,
            product_type: str,
            product_place: str,
            product_warrenty: int
    ) -> None:
        self.__product_name = product_name
        self.__product_type = product_type
        self.__product_place = product_place
        self.__product_warrenty = product_warrenty

    def set_product_name(
            self,
            product_name: str
    ) -> None:
        """It sets the instance attribute product name"""
        self.__product_name = product_name

    def get_product_name(
            self
    ) -> str:
        """It gets the instance attribute product name"""
        return self.__product_name

    def set_product_type(
            self,
            product_type: str
    ) -> None:
        """It sets the instance attribute product type"""
        self.__product_type = product_type

    def get_product_type(
            self
    ) -> str:
        """It gets the instance attribute proudct type"""
        return self.__product_type

    def set_product_place(
            self,  product_place: str
    ) -> None:
        """It sets the instance attribute proudct place"""
        self.__product_place = product_place

    def get_product_place(
            self
    ) -> str:
        """It gets the instance attribute proudct place"""
        return self.__product_place

    def set_product_warrenty(
            self,  product_warrenty: int
    ) -> None:
        """It sets the instance attribute proudct warrenty"""
        self.__product_warrenty = product_warrenty

    def get_product_warrenty(
            self
    ) -> str:
        """It gets the instance attribute proudct warrenty"""
        return self.__product_warrenty
