class OrderLocs:
    checkout_button = ('xpath', '//*[@class="btn_action checkout_button"]')
    fname_field = ('xpath', '//*[@data-test="firstName"]')
    lname_field = ('xpath', '//*[@data-test="lastName"]')
    postal_field = ('xpath', '//*[@data-test="postalCode"]')
    cancel_button = ('xpath', '//*[@class="cart_cancel_link btn_secondary"]')
    continue_button = ('xpath', '//*[@type="submit"]')
    finish_button = ('xpath', '//*[@class="btn_action cart_button"]')
    order_success_header = ('xpath', '//h2')
    order_success_text = ('xpath', '//*[@class="complete_text"]')
    order_success_logo = ('xpath', '//*[@class="pony_express"]')
    subtotal = ('xpath', '//div[@class="summary_subtotal_label"]')
    tax = ('xpath', '//div[@class="summary_tax_label"]')
    total = ('xpath', '//div[@class="summary_total_label"]')
    quantity = ('xpath', '//div[@class="summary_quantity"]')

class OrderData:
    valid_fname = 'Alina'
    valid_lname = 'Dubrovskaya'
    valid_postal = '246023 Gomel BY'
    invalid_fname = 'X'
    invalid_lname = 'q'
    invalid_postal = 'f'
    order_success_header = 'THANK YOU FOR YOUR ORDER'
    order_success_text = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    order_success_image = 'https://www.saucedemo.com/v1/img/pony-express.png'
    order_error_message1 = 'Error: First Name is required'
    order_error_message2 = 'Error: Last Name is required'
    order_error_message3 = 'Error: Postal Code is required'
    tax_rate = 0.0800266755585195