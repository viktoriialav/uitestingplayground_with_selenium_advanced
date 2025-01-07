from project_tests.selenium_advanced import browser


def test_find_button_with_dynamic_id():
    # GIVEN
    browser.open()
    necessary_text = 'Button with Dynamic ID'

    # WHEN
    browser.element('a[href="/dynamicid"]').click()
    founded_text = browser.find_element('.btn').text

    # THEN
    assert necessary_text == founded_text


def test_find_button_and_work_with_alert():
    # GIVEN
    browser.open()

    # WHEN
    browser.element('a[href="/classattr"]').click()
    browser.find_element('.btn-primary').click()
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()
    browser.switch_to.default_content()

    # THEN
    assert text == 'Primary button pressed'
    assert browser.find_element('section .container h3')


def test_wait_for_data_to_appear_after_ajax_request():
    # GIVEN
    browser.open()
    browser.set_wait(timeout=15.0)

    # WHEN
    browser.element('a[href="/ajax"]').click()
    browser.element('#ajaxButton').click()
    text = browser.element('.bg-success').text

    # THEN
    assert text == 'Data loaded with AJAX get request.'


def test_wait_for_a_page_to_load():
    # GIVEN
    browser.open()
    browser.set_wait(timeout=15.0)

    # WHEN/
    browser.element('a[href="/loaddelay"]').click()
    text = browser.find_element('.btn-primary').text

    # THEN
    assert text == 'Button Appearing After Delay'






