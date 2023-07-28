import allure
from demoqa_tests.model.pages.alerts import AlertsPage

alerts = AlertsPage()


@allure.label('owner', 'Larisa Badmaeva')
@allure.feature('Tests DemoQA')
@allure.title('Alert confirmation')
def test_confirm_alert():
    with allure.step('Opening the alert page'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_confirm()
    with allure.step('Check alert confirmation'):
        alerts.assert_confirm_alert()


@allure.label('owner', 'Larisa Badmaeva')
@allure.feature('Tests DemoQA')
@allure.title('Acknowledge alert with text field filled')
def test_prompt_alert():
    with allure.step('Opening the alert page'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_prompt()
    with allure.step('Entering value in text field in alert'):
        alerts.type_to_alert('laribadmaeva')
    with allure.step('Check alert confirmation'):
        alerts.assert_prompt_alert('laribadmaeva')