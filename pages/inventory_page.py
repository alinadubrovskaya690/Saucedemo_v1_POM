from pages.base_page import BasePage
from locators.inventory_locs import InventoryLocs


class InventoryPage(BasePage):
    def prod_lab(self):
        return self.is_visible(InventoryLocs.prod_label)

    def inventory_card(self):
        return self.find_el(InventoryLocs.inv_card)

    def inventory_cards(self):
        return self.find_elems(InventoryLocs.inv_card)

    def inventory_img(self):
        return self.find_el(InventoryLocs.inv_img)

    def inventory_imgs(self):
        return self.find_elems(InventoryLocs.inv_img)

    def inventory_name(self):
        return self.find_el(InventoryLocs.inv_name)

    def inventory_names(self):
        return self.find_elems(InventoryLocs.inv_name)

    def inventory_desc(self):
        return self.find_el(InventoryLocs.inv_desc)

    def inventory_descs(self):
        return self.find_elems(InventoryLocs.inv_desc)

    def inventory_price(self):
        return self.find_el(InventoryLocs.inv_price)

    def inventory_prices(self):
        return self.find_elems(InventoryLocs.inv_price)

    def inventory_add_item(self):
        return self.find_el(InventoryLocs.add_button)

    def inventory_add_items(self):
        return self.find_elems(InventoryLocs.add_button)

    def inventory_remove_item(self):
        return self.find_el(InventoryLocs.remove_button)

    def inventory_remove_items(self):
        return self.find_elems(InventoryLocs.remove_button)