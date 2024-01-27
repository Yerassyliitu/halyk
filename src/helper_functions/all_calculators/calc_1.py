from src.helper_functions.all_calculators.main_functions import select_dropdown_option, initialize_driver, \
    click_and_parse_result


def navigate_and_fill_fields(driver, date_of_birth, gender, insurance_coverage_duration_years,
                             premium_payment_period_years, premium_payment_frequency, tt_insurance_sum,
                             total_insurance_sum, insurance_premium):
    """
    Переход по URL и заполнение полей формы предоставленными значениями.
    """
    url = 'https://calc.halyklife.kz/Calc06.aspx'
    driver.get(url)

    # Используйте словарь для удобства доступа к элементам по их описательным именам
    field_mapping = {
        'date_of_birth': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_DateOfBirth_TextBox1',
        'gender': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_Gend',
        'insurance_coverage_duration_years': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_covperiod_TextBox1',
        'premium_payment_period_years': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_period_TextBox1',
        'premium_payment_frequency': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_payperiod',
        'tt_insurance_sum': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_ttsum',
        'total_insurance_sum': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_inssum_TextBox1',
        'insurance_premium': 'ctl00_MainContent_calc06_MixedInsuranceCalc1_prem_TextBox1',
    }

    # Заполнение полей формы
    driver.find_element(by='id', value=field_mapping['date_of_birth']).send_keys(date_of_birth)
    driver.find_element(by='id', value=field_mapping['gender']).send_keys(gender)
    driver.find_element(by='id', value=field_mapping['insurance_coverage_duration_years']).send_keys(
        insurance_coverage_duration_years)
    driver.find_element(by='id', value=field_mapping['premium_payment_period_years']).send_keys(
        premium_payment_period_years)

    # Выбор опций в выпадающих списках
    select_dropdown_option(driver.find_element(by='id', value=field_mapping['premium_payment_frequency']),
                           premium_payment_frequency)
    select_dropdown_option(driver.find_element(by='id', value=field_mapping['tt_insurance_sum']),
                           tt_insurance_sum)

    driver.find_element(by='id', value=field_mapping['total_insurance_sum']).send_keys(total_insurance_sum)
    driver.find_element(by='id', value=field_mapping['insurance_premium']).send_keys(insurance_premium)


def calc_1(date_of_birth, gender, insurance_coverage_duration_years, premium_payment_period_years,
           premium_payment_frequency, tt_insurance_sum, total_insurance_sum, insurance_premium):
    """
    Основная функция для выполнения всего процесса.
    """
    # Используйте контекстный менеджер для автоматического закрытия драйвера
    with initialize_driver() as driver:
        navigate_and_fill_fields(driver, date_of_birth, gender, insurance_coverage_duration_years,
                                 premium_payment_period_years, premium_payment_frequency, tt_insurance_sum,
                                 total_insurance_sum, insurance_premium)
        result_dict = click_and_parse_result(driver)

    return result_dict


# Пример использования с предоставленными данными
example_data = {
    "date_of_birth": "10.09.1990",
    "gender": "1",
    "insurance_coverage_duration_years": "10",
    "premium_payment_period_years": "30",
    "premium_payment_frequency": "1",
    "tt_insurance_sum": "200000",
    "total_insurance_sum": "200000",
    "insurance_premium": "500000"
}

# Для теста
# result = parse_selenium_and_bs4(**example_data)
# print(result)
