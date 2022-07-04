from pages.google_page import GooglePage
from selenium.webdriver.common.by import By


class GooglePicturesPage(GooglePage):
    picture_size_dd_menu = (By.CSS_SELECTOR, '[jsname="wLFV5d"]') # Выпадающее меню "Размер"
    picture_size_dd_menu_any = (By.CSS_SELECTOR, 'a.MfLWbb[aria-label="Any size"]') # Выпадающее меню "Размер" - "Любой"
    picture_size_dd_menu_big = (By.CSS_SELECTOR, 'a.MfLWbb[aria-label="Large"]') # Выпадающее меню "Размер" - "Большой"
    picture_size_dd_menu_avr = (By.CSS_SELECTOR, 'a.MfLWbb[aria-label="Medium"]') # Выпадающее меню "Размер" - "Средний"
    picture_size_dd_menu_icons = (By.CSS_SELECTOR, 'a.MfLWbb[aria-label="Icon"]') # Выпадающее меню "Размер" - "Значки"
    get_links = (By.CSS_SELECTOR, '[jsname="uy6ald"]') # Получение ссылок на странице

    def choose_picture_size_dd_menu_big(self):
        """ Выбрать в фильтре "Большие" картинки """
        el = self.find_element(self.tools_button)
        el.click()
        el = self.find_element(self.picture_size_dd_menu)
        el.click()
        el = self.find_element(self.picture_size_dd_menu_big)
        el.click()
        return self
    
    def get_count_matched_links_with_text(self, text: str):
        """ Получаем колиство ссылок содержащих в себе text"""
        count = 0
        els = self.find_elements(self.get_links)
        for el in els:
            if text in el.text:
                count +=1
        return count
        