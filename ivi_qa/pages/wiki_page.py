from pages.google_page import BasePage
from selenium.webdriver.common.by import By


class WikiPage(BasePage):
    body_content = (By.ID, 'bodyContent')
    links = (By.CSS_SELECTOR, 'a')

    def get_body_content_links(self):
        bc = self.find_element(self.body_content)
        l = []
        items = bc.find_elements(By.CSS_SELECTOR, 'a')
        for item in items:
            if item:
                l.append(item.get_attribute("href"))
        return l
