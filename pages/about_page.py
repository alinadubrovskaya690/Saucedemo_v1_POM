from pages.base_page import BasePage
from locators.about_locs import AboutLocs

class AboutPage(BasePage):
    @staticmethod
    def exp_title():
        return AboutLocs.exp_title