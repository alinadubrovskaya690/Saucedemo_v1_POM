from pages.base_page import BasePage
from locators.items_locs import ItemLocs, ItemData


class ItemsPage(BasePage):
    def item_add(self):
        return self.find_el(ItemLocs.add_button)

    def items_add(self):
        return self.find_elems(ItemLocs.add_button)

    def item_remove(self):
        return self.find_el(ItemLocs.remove_button)

    def items_remove(self):
        return self.find_elems(ItemLocs.remove_button)

    def items_img(self):
        return self.find_el(ItemLocs.item_img)

    def items_imgs(self):
        return self.find_elems(ItemLocs.item_img)

    def items_name(self):
        return self.find_el(ItemLocs.item_name)

    def items_names(self):
        return self.find_elems(ItemLocs.item_name)

    def items_desc(self):
        return self.find_el(ItemLocs.item_desc)

    def items_descs(self):
        return self.find_elems(ItemLocs.item_desc)

    def items_price(self):
        return self.find_el(ItemLocs.item_price)

    def items_prices(self):
        return self.find_elems(ItemLocs.item_price)