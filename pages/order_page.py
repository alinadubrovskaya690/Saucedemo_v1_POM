from pages.base_page import BasePage
from locators.order_locs import OrderLocs, OrderData


class OrderPage(BasePage):
    def input_fname(self):
        return self.is_visible(OrderLocs.fname_field)

    def input_lname(self):
        return self.is_visible(OrderLocs.lname_field)

    def input_zip(self):
        return self.is_visible(OrderLocs.postal_field)

    def checkout_btn(self):
        return self.is_clickable(OrderLocs.checkout_button)

    def continue_btn(self):
        return self.is_clickable(OrderLocs.continue_button)

    def finish_btn(self):
        return self.is_clickable(OrderLocs.finish_button)

    def cancel_btn(self):
        return self.is_clickable(OrderLocs.cancel_button)

    def subtotal(self):
        return self.is_visible(OrderLocs.subtotal)

    def tax(self):
        return self.is_visible(OrderLocs.tax)

    def total(self):
        return self.is_visible(OrderLocs.total)

    def success_img(self):
        return self.is_visible(OrderLocs.order_success_logo)

    def order_item_quantity(self):
        return self.find_el(OrderLocs.quantity)

    def order_item_quantities(self):
        return self.find_elems(OrderLocs.quantity)

    @staticmethod
    def success_msg():
        return OrderData.order_success_header

    @staticmethod
    def error_msg1():
        return OrderData.order_error_message1

    @staticmethod
    def error_msg2():
        return OrderData.order_error_message2

    @staticmethod
    def error_msg3():
        return OrderData.order_error_message3