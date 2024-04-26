from pages.base_page import BasePage
from locators.cart_locs import CartLocs
from locators.inventory_locs import InventoryLocs


class CartPage(BasePage):
    def cart_header(self):
        return self.is_visible(CartLocs.cart_header)

    def cart_count(self):
        return self.is_visible(CartLocs.cart_count)

    def cart_count_invisible(self):
        return self.is_invisible(CartLocs.cart_count)

    def cart_container(self):
        return self.is_visible(CartLocs.cart_container)

    def cart_quantity(self):
        return self.find_el(CartLocs.cart_quantity)

    def cart_quantities(self):
        return self.find_elems(CartLocs.cart_quantity)

    def cart_btn(self):
        return self.find_el(CartLocs.cart_button)

    def cart_btns(self):
        return self.find_elems(CartLocs.cart_button)

    def cart_remove_item(self):
        return self.find_el(CartLocs.remove_button_cart)

    def cart_remove_items(self):
        return self.find_elems(CartLocs.remove_button_cart)

    def cart_item_name(self):
        return self.find_el(InventoryLocs.inv_name)

    def cart_item_names(self):
        return self.find_elems(InventoryLocs.inv_name)

    def cart_item_desc(self):
        return self.find_el(InventoryLocs.inv_desc)

    def cart_item_descs(self):
        return self.find_elems(InventoryLocs.inv_desc)

    def cart_item_price(self):
        return self.find_el(InventoryLocs.inv_price)

    def cart_item_prices(self):
        return self.find_elems(InventoryLocs.inv_price)

    def cart_return_to_shop(self):
        return self.is_visible(CartLocs.cart_continue)

    def cart_checkout(self):
        return self.is_visible(CartLocs.cart_checkout)

