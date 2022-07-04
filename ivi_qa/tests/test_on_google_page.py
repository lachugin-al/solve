from pages.google_page import GooglePage
from pages.wiki_page import WikiPage
from pages.google_pictures_page import GooglePicturesPage


def test_1(browser):
    """ неавторизованный пользователь заходит в https://www.google.com/
        ищет ivi
        переходит в картинки
        выбирает большие 
        убеждается, что не менее 3 картинок в выдаче ведут на сайт ivi.ru """
    gpp = GooglePicturesPage(browser)
    gpp.search("ivi") \
        .choose_pictures_page() \
        .choose_picture_size_dd_menu_big()

    assert gpp.get_count_matched_links_with_text("ivi.ru") >= 3


def test_2(browser):
    """ неавторизованный пользователь заходит в https://www.google.com/
        ищет ivi
        на первых 5 страницах находит ссылки на приложение ivi в play.google.com
        убеждается, что рейтинг приложения на кратком контенте страницы совпадает с рейтингом "число между 3.5 и 4.9"

        Примечание: нет возможности проверить рейтинг на странице play.google.com"""
    gp = GooglePage(browser)
    google_rating = gp.search("ivi").get_rating_from_links_with_matched_url(url="play.google.com", pages=5)

    assert 3.5 <= google_rating <=4.9
    

def test_3(browser):
    """ неавторизованный пользователь заходит в https://www.google.com/
        ищет ivi
        на первых 5 страницах находит ссылку на статью в wikipedia об ivi
        убеждается, что в статье есть ссылка на официальный сайт ivi.ru """
    gp = GooglePage(browser)
    wk = WikiPage(browser)

    el = gp.search("ivi").get_links_with_matched_url("https://ru.wikipedia.org/wiki/Ivi.ru", 5)
    if el:
        browser.get(el)

    assert "https://www.ivi.ru/" in wk.get_body_content_links()
