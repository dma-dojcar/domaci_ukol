products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "BMW",
        "price": 30,
    },
    {
        "name": "Audi",
        "price": 32
    }
]

def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")

def add_product():
    product_name = input("Název produktu: ")
    product_price = float(input("Cena produktu: "))  # Opraveno na float
    product2 = {
        'name': product_name,
        'price': product_price
    }
    products.append(product2)

def find_products():
    finder = input("Zadejte název produktu, který chcete najít: ")
    for product in products:
        if finder.lower() in product["name"].lower():  # Hledání bez ohledu na velikost písmen
            print(product)

def min_price():
    min_price = float('inf')  # Inicializace na nekonečno
    for product in products:
        if product["price"] < min_price:
            min_price = product["price"]
   
    print("Nejlevnější produkt/produkty jsou:")
    for product in products:
        if min_price == product["price"]:
            print(f"Produkt: {product['name']} Cena: {product['price']} $")

def max_price():
    max_price = float('-inf')  # Inicializace na -nekonečno
    for product in products:
        if product["price"] > max_price:  # Hledáme maximální cenu
            max_price = product["price"]
   
    print("Nejdražší produkt/produkty jsou:")
    for product in products:
        if max_price == product["price"]:
            print(f"Produkt: {product['name']} Cena: {product['price']} $")

def average_price():
    total_price = 0
    count = 0
    for product in products:
        total_price += product["price"]
        count += 1
    if count > 0:
        average = total_price / count
        print(f"Průměrná cena je {average:.2f} $")
    else:
        print("Žádné produkty k výpočtu průměrné ceny.")

def remove_product():
    print("Zadejte číslo produktu, který chcete odstranit:")
    print_products()  # Zobrazí seznam produktů
    try:
        remove_number_index = int(input("Číslo produktu: ")) - 1  # Uživatel zadá číslo, které se převede na index
        if 0 <= remove_number_index < len(products):
            removed_product = products.pop(remove_number_index)  # Odstranění produktu
            print(f"Odstraněn produkt: {removed_product['name']}, Cena: {removed_product['price']} $")
        else:
            print("Neplatný index. Zadejte číslo v rozsahu dostupných produktů.")
    except ValueError:
        print("Prosím, zadejte platné číslo.")

def menu():
    while True:
        print("Vítej ve skladu")
        print("###################\n")
        print("1. Výpis položek")
        print("2. Přidání položky")
        print("3. Najít položku")
        print("4. Najít nejlevnější auto")
        print("5. Najít průměrnou cenu")
        print("6. Odstranit produkt")
        print("7. Najít nejdražší auto")
        print("8. Konec")

        choice = int(input("Volba: "))

        if choice == 1:
            print("Položky na skladě jsou:")
            print_products()
            print("")

        elif choice == 2:
            print("Přidání položky:")
            add_product()
            print("")

        elif choice == 3:
            print("Napište, co chcete najít:")
            find_products()
            print("")

        elif choice == 4:
            min_price()
            print("")

        elif choice == 5:
            average_price()
            print("")

        elif choice == 6:
            print("Odstranění produktu:")
            remove_product()
            print("")

        elif choice == 7:
            max_price()
            print("")

        elif choice == 8:
            print("Děkujeme za použití programu!")
            break

        else:
            print("Zadal jsi špatně!\n")

menu()
