from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage(BasePage):
    search_field = (By.NAME, 'q') # поисковая строка
    pictures_link = (By.CSS_SELECTOR, '[data-hveid="CAIQBQ"]') # ссылка на категорию "Картинки"
    tools_button = (By.CSS_SELECTOR, '[jsname="I4bIT"]') # Кнопка "Инструменты"
    content_link = (By.CSS_SELECTOR, 'a[data-ved]') # Информация по ссылкам на странице
    rating_stars = (By.CSS_SELECTOR, '.fG8Fp.uo4vr') # Информация по рейтингу к контенту
    rating_stars_text = (By.CSS_SELECTOR, 'g-review-stars > span') # Текст к рейтингу к контенту
    next_page = (By.ID, 'pnnext') # Локатор переключения на следующую страницу в поиске
    ulr_vidget = (By.CSS_SELECTOR, '.g') # Локатор для поиска блоков с сылками


    def search(self, text: str):
        """ Ввод данных в строку поиска """
        el = self.find_element(self.search_field)
        el.send_keys(text)
        el.send_keys(Keys.ENTER)
        return self


    def choose_pictures_page(self):
        """ Выбрать категорию "Картинки" """
        el = self.find_element(self.pictures_link)
        el.click()
        return self
    

    def get_links_with_matched_url(self, url: str, pages=5):
        """ Получаем список ссылок на 5-ти страницах (по умолчанию), 
            достаем аттрибут href и сравниваем в введенным url """
        for page in range(pages - 1):
            els = self.find_elements(self.content_link)

            for el in els:
                attribute_href = el.get_attribute("href")
                if attribute_href and url in attribute_href:
                    return attribute_href
            self.select_next_page()
            

    def get_rating_from_links_with_matched_url(self, url: str, pages=5):
        """ Получить числовое значение рейтинга из ресурса """
        for page in range(pages - 1):
            els = self.find_elements(self.ulr_vidget)
            for item in els:
                if item is not None:
                    text = item.text
                    if url in text:
                        strip_text = text.strip().splitlines()
                        rating_number = strip_text[-1].split(" ·")
                        return float(rating_number[0].replace("Рейтинг: ", "").replace(",", "."))
            self.select_next_page()
    

    def select_next_page(self):
        el = self.find_element(self.next_page)
        el.click()
        return self
        