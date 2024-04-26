class CartLocs:
    cart_button = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
    cart_count = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')
    cart_header = ('xpath', '//div[@class="subheader"]')
    cart_container = ('xpath', '//div[@id="cart_contents_container"]')
    remove_button_cart = ('xpath', '//button[@class="btn_secondary cart_button"]')
    cart_quantity = ('xpath', '//div[@class="cart_quantity"]')
    cart_continue = ('xpath', '//a[@class="btn_secondary"]')
    cart_checkout = ('xpath', '//a[@class="btn_action checkout_button"]')