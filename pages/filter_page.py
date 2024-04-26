from pages.base_page import BasePage
from locators.filter_locs import FitlerLocs


class FilterMod(BasePage):
    def filter_az(self):
        return self.is_visible(FitlerLocs.filter_az_button)

    def filter_za(self):
        return self.is_visible(FitlerLocs.filter_za_button)

    def filter_lohi(self):
        return self.is_visible(FitlerLocs.filter_lowhigh_button)

    def filter_hilo(self):
        return self.is_visible(FitlerLocs.filter_highlow_button)