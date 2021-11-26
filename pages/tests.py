from PromuaPage import SearchHelper
from ProductPage import Product_page

def test_prom_search(browser):
    """Documentation:
    The test for counter of the favorite button counter. If the user clicks the favorite button a few times, the counter 
    shows both increase and decrease of the counter.
    ==Steps:==
    1. Go to main page of "Velosipednye-shiny"
    2. Authorize as a user with email button
    3. Input the product name at search field and push search button
    4. Assert the first product card is "Покришка Schwalbe Marathon Supreme 42-622 Evolution OneStar "
    5. Push 11 times (without timesleep) favorite button
    6. Assert the favorite counter shows "1"
    7. Assert the chosen product is shown at the "favorites" page at the user`s cabinet
    """
    prom_main_page = SearchHelper(browser)
    prom_main_page.go_to_site()
    prom_main_page.login_button()
    prom_main_page.search_product("Покришка Schwalbe Marathon Supreme 42-622 Evolution OneStar")

    #prom_main_page.parse_product_cart()
    prom_product_page = Product_page(browser)
    prom_product_page.go_to_product_url()
    prom_product_page.favorite_button()
    prom_product_page.favorite_count()
    prom_product_page.go_to_favorite_url()

    #assert True