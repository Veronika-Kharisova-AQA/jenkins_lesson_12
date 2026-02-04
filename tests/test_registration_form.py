from pathlib import Path
import allure
from selene import browser, by, have, command
from selene.support.shared.jquery_style import s, ss


@allure.title('Successfull registration')
def test_practice_form():
    with allure.step('Open registration form'):
        browser.open('/automation-practice-form')

    with allure.step('Fill full name'):
        s('#firstName').type('Veronika')
        s('#lastName').type('Kharisova')

    with allure.step('Fill email'):
        s('#userEmail').type('Veronika@example.com')

    with allure.step('Select gender'):
        s(by.text('Female')).click()

    with allure.step('Fill phone number'):
        s('#userNumber').type('5643782341')

    with allure.step('Fill birth date'):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().element(by.text('July')).click()
        s('.react-datepicker__year-select').click().element(by.text('2002')).click()
        s('.react-datepicker__day--014:not(.react-datepicker__day--outside-month').click()

    with allure.step('Fill subject'):
        s('#subjectsInput').type('Math').press_enter()

    with allure.step('Choose hobby'):
        s('#hobbiesWrapper').element(by.text('Sports')).click()

    with allure.step('Upload picture'):
        picture = str(Path(__file__).parent.parent.joinpath('resources', 'cat.jpg').resolve())
        s('#uploadPicture').set_value(picture)

    with allure.step('Full address'):
        s('#currentAddress').type('Russia, Moscow')

    with allure.step('Select state'):
        s('#state').perform(command.js.scroll_into_view).click()
        s('#react-select-3-input').type('NCR').press_enter()

    with allure.step('Select city'):
        s('#city').click()
        s('#react-select-4-input').type('Delhi').press_enter()

    with allure.step('Submit'):
        s('#submit').click()

    with allure.step('Displaying a modal window'):
        s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    with allure.step('Check values'):
        ss('.modal-content table tbody tr td:nth-child(2)').should(have.exact_texts(
            'Veronika Kharisova',
            'Veronika@example.com',
            'Female',
            '5643782341',
            '14 July,2002',
            'Maths',
            'Sports',
            'cat.jpg',
            'Russia, Moscow',
            'NCR Delhi'
        ))
