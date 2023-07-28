from selene import have, be
from selene.support.shared import browser
from demoqa_tests.model.methods.radio import Radio


def opening():
    browser.open("/automation-practice-form")
    browser.driver.execute_script("$('footer').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")


def input_name(value):
    browser.element("#firstName").set_value(value)


def input_surname(value):
    browser.element("#lastName").set_value(value)


def set_gender(value):
    gender = Radio(browser.all('[name=gender]'))
    gender.set(value)


def input_phone(value):
    browser.element("#userNumber").set_value(value)


def submit():
    browser.element('#submit').press_enter()


def fill_registration_form(name, surname, gender, phone):
    input_name(name)
    input_surname(surname)
    set_gender(gender)
    input_phone(phone)
    submit()


def assert_results_registration(data):
    rows = browser.all('.modal-content tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
