from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def parse_selenium_and_bs4(field1, field2, field3, field4, field5, field6, field7, field8):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.headless = True
    chrome_version = "97.0.4692.99"
    # Initialize Chrome driver with ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version=chrome_version).install()), options=chrome_options)

    # Navigate to the URL
    url = 'https://calc.halyklife.kz/Calc06.aspx'
    driver.get(url)

    # Find the element by ID and send keys
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_DateOfBirth_TextBox1').send_keys(
        field1)
    # Find the dropdown element by ID
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_Gend').send_keys(field2)

    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_covperiod_TextBox1').send_keys(
        field3)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_period_TextBox1').send_keys(field4)

    dropdown_element1 = driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_payperiod')
    select = Select(dropdown_element1)
    select.select_by_value(field5)

    dropdown_element2 = driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_ttsum')
    select = Select(dropdown_element2)
    select.select_by_value(field6)

    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_inssum_TextBox1').send_keys(field7)
    driver.find_element(by='id', value='ctl00_MainContent_calc06_MixedInsuranceCalc1_prem_TextBox1').send_keys(field8)

    # Find and click the button
    element = driver.find_element(by='id', value="ctl00_MainContent_calc06_MixedInsuranceCalc1_calcReverse")

    # Нажатие на элемент
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
    print(result_dict)

    driver.quit()
    return result_dict
