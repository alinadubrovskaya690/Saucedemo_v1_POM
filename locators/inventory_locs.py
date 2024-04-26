class InventoryLocs:
    prod_label = ('xpath', '//div[@class="product_label"]')
    inv_card = ('xpath', '//div[@class="inventory_item"]')
    inv_name = ('xpath', '//div[@class="inventory_item_name"]')
    inv_desc = ('xpath', '//div[@class="inventory_item_desc"]')
    inv_price = ('xpath', '//div[@class="inventory_item_price"]')
    inv_img = ('xpath', '//img[@class="inventory_item_img"]')
    add_button = ('xpath', '//*[@class="btn_primary btn_inventory"]')
    remove_button = ('xpath', '//*[@class="btn_secondary btn_inventory"]')