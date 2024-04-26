class ItemLinks:
    item1_name_link = ('xpath', '//a[@id="item_4_title_link"]')
    item1_img_link = ('xpath', '//a[@id="item_4_img_link"]')

    item2_name_link = ('xpath', '//a[@id="item_0_title_link"]')
    item2_img_link = ('xpath', '//a[@id="item_0_img_link"]')

    item3_name_link = ('xpath', '//a[@id="item_1_title_link"]')
    item3_img_link = ('xpath', '//a[@id="item_1_img_link"]')

    item4_name_link = ('xpath', '//a[@id="item_5_title_link"]')
    item4_img_link = ('xpath', '//a[@id="item_5_img_link"]')

    item5_name_link = ('xpath', '//a[@id="item_2_title_link"]')
    item5_img_link = ('xpath', '//a[@id="item_2_img_link"]')

    item6_name_link = ('xpath', '//a[@id="item_3_title_link"]')
    item6_img_link = ('xpath', '//a[@id="item_3_img_link"]')

class ItemLocs:
    item_name = ('xpath', '//*[@class="inventory_details_name"]')
    item_desc = ('xpath', '//*[@class="inventory_details_desc"]')
    item_price = ('xpath', '//*[@class="inventory_details_price"]')
    item_img = ('xpath', '//*[@class="inventory_details_img"]')
    back_button = ('xpath', '//*[@class="inventory_details_back_button"]')
    add_button = ('xpath', '//*[@class="btn_primary btn_inventory"]')
    remove_button = ('xpath', '//*[@class="btn_secondary btn_inventory"]')

class ItemData:
    item1_name = 'Sauce Labs Backpack'
    item1_img = 'https://www.saucedemo.com/v1/img/sauce-backpack-1200x1500.jpg'
    item1_desc = ('carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising '
                  'style with unequaled laptop and tablet protection.')
    item1_price = '$29.99'

    item2_name = 'Sauce Labs Bike Light'
    item2_img = 'https://www.saucedemo.com/v1/img/bike-light-1200x1500.jpg'
    item2_desc = ("A red light isn't the desired state in testing but it sure helps when riding your bike "
                  "at night. Water-resistant with 3 lighting modes, 1 AAA battery included.")
    item2_price = '$9.99'

    item3_name = 'Sauce Labs Bolt T-Shirt'
    item3_img = 'https://www.saucedemo.com/v1/img/bolt-shirt-1200x1500.jpg'
    item3_desc = ("Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, "
                  "100% ringspun combed cotton, heather gray with red bolt.")
    item3_price = '$15.99'

    item4_name = 'Sauce Labs Fleece Jacket'
    item4_img = 'https://www.saucedemo.com/v1/img/sauce-pullover-1200x1500.jpg'
    item4_desc = ("It's not every day that you come across a midweight quarter-zip fleece jacket capable of "
                  "handling everything from a relaxing day outdoors to a busy day at the office.")
    item4_price = '$49.99'

    item5_name = 'Sauce Labs Onesie'
    item5_img = 'https://www.saucedemo.com/v1/img/red-onesie-1200x1500.jpg'
    item5_desc = ("Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap "
                  "bottom closure, two-needle hemmed sleeved and bottom won't unravel.")
    item5_price = '$7.99'

    item6_name = 'Test.allTheThings() T-Shirt (Red)'
    item6_img = 'https://www.saucedemo.com/v1/img/red-tatt-1200x1500.jpg'
    item6_desc = ("This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate "
                  "a few tests. Super-soft and comfy ringspun combed cotton.")
    item6_price = '$15.99'