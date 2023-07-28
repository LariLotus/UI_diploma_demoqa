import allure
from demoqa_tests.model.pages.tooltips import TooltipPage

tooltips = TooltipPage()


@allure.label('owner', 'Larisa Badmaeva')
@allure.feature('Tests DemoQA')
@allure.title('Text field tooltip')
def test_confirm_alert():
    with allure.step('Opening the hint page'):
        tooltips.open()
    with allure.step('Setting focus on the field'):
        tooltips.set_focus_in_field()
    with allure.step('Check hint text'):
        tooltips.assert_text()
