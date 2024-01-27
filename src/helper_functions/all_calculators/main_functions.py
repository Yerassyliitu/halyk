from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def initialize_driver():
    """
    Инициализация безголового (headless) браузера Chrome с необходимыми опциями.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.headless = True

    # Используем ChromeDriverManager для автоматической загрузки и управления исполняемым файлом ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return driver


def click_and_parse_result(driver):
    """
    Нажатие кнопки расчета, разбор результата и возврат его в виде словаря.
    """
    element = driver.find_element(by='id', value="ctl00_MainContent_calc06_MixedInsuranceCalc1_calcReverse")
    element.click()

    page_source_after_reload = driver.page_source

    if page_source_after_reload:
        result_dict = {}
        soup = BeautifulSoup(page_source_after_reload, 'html.parser')
        for row in soup.select('.formTable_result tr'):
            columns = row.find_all(['th', 'td'])
            key = columns[0].get_text(strip=True)
            value = columns[1].get_text(strip=True).replace('\xa0', '')
            result_dict[key] = value
    else:
        result_dict = None

    return result_dict


def select_dropdown_option(dropdown_element, value):
    """
    Выбор опции в выпадающем списке по её значению.
    """
    select = Select(dropdown_element)
    select.select_by_value(value)
