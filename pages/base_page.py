from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    # Открывает страницу
    def open_page(self):

        self.browser.get(self.link)

    # Возвращается объект WebElement на основе заданного критерия поиска
    def element_is_present(self, method, locator):

        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # Возвращается список WebElements, соответствующий критериям поиска
    def elements_are_present(self, method, locator):
        try:
            return self.browser.find_elements(method, locator)
        except NoSuchElementException:
            return NoSuchElementException

    # Возвращается элемент или запускается ожидание timeout секунд
    # появления элемента
    # до того, как вернется исключение TimeoutException,
    # если не появится элемент за timeout
    def element_is_visible(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    # Возвращаются элементы или запускается ожидание timeout
    # секунд до того,
    # как вернется исключение TimeoutException,
    # если не найдет элемент за timeout
    def elements_are_located(self, locator, timeout=5):
        return Wait(self.browser, timeout).until(
            EC.presence_of_all_elements_located((locator))
        )

    # Проверяет, что текущая страница соответствует требованиям
    def should_be_link(self, link):
        assert link in self.browser.current_url, "wrong url"

    # Проверяет, что текст элемента заглавия страницы
    def should_be_page_title(self, title, method, locator):
        el_title = self.browser.find_element(method, locator)
        # Получает элемент заглавия страницы
        assert el_title, "there is no title"
        # Проверяет, что текст элемента заглавия страницы
        # соответствует требованиям
        assert title == el_title.text, "wrong title"

    # Возвращает с указанного индекса i текст элементов,
    # соответствующий требованиям
    def get_text(self, i, method, locator):
        return self.browser.find_element(method, locator).text.split("\n")[i:]
