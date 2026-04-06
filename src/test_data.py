class URL:
    kitchen_cabinet_url = 'https://www.homebuddy.com/near-me/kitchen-cabinet-refacing'


class TestData:
    correct_ZIP = '10003'
    incorrect_ZIP = '500'


class Constants:
    error_message_validation = 'The ZIP Code must be 5 digits with no spaces.'


class Locators:
    zip_code_input = '[data-autotest-input-0]'
    start_matching_button = '[data-autotest-zip-submit-0]'
    button_next = '[data-autotest-next]'
    zip_code_input_error = '.zip-input__message'
