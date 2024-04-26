from pages.base_page import BasePage
from locators.sidebar_locs import SidebarLocs


class SidebarMod(BasePage):
    def sidebar_menu(self):
        return self.find_el(SidebarLocs.side_menu_button)

    def sidebar_all_items(self):
        return self.is_clickable(SidebarLocs.all_items_button)

    def sidebar_about(self):
        return self.is_clickable(SidebarLocs.about_button)

    def sidebar_logout(self):
        return self.is_clickable(SidebarLocs.logout_button)

    def sidebar_reset(self):
        return self.is_clickable(SidebarLocs.reset_button)

    def sidebar_close(self):
        return self.is_clickable(SidebarLocs.close_button)