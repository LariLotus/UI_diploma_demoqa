import allure
from demoqa_tests.model.pages.browser_windows import WindowPage

browser_windows = WindowPage()


@allure.label('owner', 'Larisa Badmaeva')
@allure.feature('DemoQA Tests')
@allure.title("Opening a second browser tab")
def test_confirm_alert():
    with allure.step('Open browser window page'):
        browser_windows.open()
    with allure.step('Opening a second tab'):
        browser_windows.click_btn_new_tab()
    with allure.step('Check text on open tab'):
        browser_windows.assert_open_new_tab()