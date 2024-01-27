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


def navigate_and_fill_fields(driver, field1, field2, field3, field4, field5, field6, field7, field8):
    """
    Переход по URL и заполнение полей формы предоставленными значениями.
    """
    url = 'https://calc.halyklife.kz/Calc06.aspx'
    driver.get(url)

    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_DateOfBirth_TextBox1').send_keys(
        field1)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_Gend').send_keys(field2)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_covperiod_TextBox1').send_keys(
        field3)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_period_TextBox1').send_keys(field4)

    dropdown_element1 = driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_payperiod')
    select_dropdown_option(dropdown_element1, field5)

    dropdown_element2 = driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_ttsum')
    select_dropdown_option(dropdown_element2, field6)

    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_inssum_TextBox1').send_keys(field7)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_prem_TextBox1').send_keys(field8)


def select_dropdown_option(dropdown_element, value):
    """
    Выбор опции в выпадающем списке по её значению.
    """
    select = Select(dropdown_element)
    select.select_by_value(value)


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


def parse_selenium_and_bs4(field1, field2, field3, field4, field5, field6, field7, field8):
    """
    Основная функция для выполнения всего процесса.
    """
    driver = initialize_driver()

    try:
        navigate_and_fill_fields(driver, field1, field2, field3, field4, field5, field6, field7, field8)
        result_dict = click_and_parse_result(driver)
    finally:
        driver.quit()

    return result_dict


# Пример использования с предоставленными данными
example_data = {
    "field1": "10.09.1990",
    "field2": "1",
    "field3": "10",
    "field4": "30",
    "field5": "1",
    "field6": "200000",
    "field7": "200000",
    "field8": "500000"
}

# Для теста
# result = parse_selenium_and_bs4(**example_data)
# print(result)
