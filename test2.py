from product import Product
from product_service import ProductService

if __name__ == "__main__":
    service = ProductService()
    print("==============================================")
    print("             Product Management App           ")
    print("===============================================")
    print("       1. List products                        ")
    print("       2. Update Product                       ")
    print("       3. Add Product                          ")
    print("       4. Delete Product                       ")
    print("===============================================")
    print(" ")
    choice = int(input("Enter your choice :"))
    if (choice == 1):
        print("==============================================")
        print("             Listing Products                 ")
        print("===============================================")
        print("       1. View All Products                    ")
        print("       2. View Particular Product              ")
        print("================================================")
        print(" ")
        print(" ")
        list_choice = int(input("Enter your viewing choice :"))
        print(" ")
        products = []
        if (list_choice == 1):
            products = service.get_all_products()
            # print(products)
            print("=============================================")
            print("      View All Product details               ")
            print("=============================================")
            for product in products:
                print(" ")
                print(" 1. Product Name : ", product["product_name"])
                print(" 2. Product Type : ", product["product_type"])
                print(" 3. Product Place : ", product["product_place"])
                print(" 4. Product Warrenty : ", product["product_warrenty"])
                print(" ")

        else:
            product = service.get_product()
    elif (choice == 2):
        product_name = input("Enter Your Product Name :")
        product = service.get_product(product_name)
        print("=============================================")
        print("          Product details                    ")
        print("=============================================")
        print(" 1. Product Name : ", product.get_product_name())
        print(" 2. Product Type : ", product.get_product_type())
        print(" 3. Product Place : ", product.get_product_place())
        print(" 4. Product Warrenty : ", product.get_product_warrenty())
        print("=============================================")
        print(" ")
    else:
        pass
