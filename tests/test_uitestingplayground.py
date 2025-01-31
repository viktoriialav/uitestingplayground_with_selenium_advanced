

def test_find_button_with_dynamic_id(browser):
    # GIVEN
    browser.open()
    necessary_text = 'Button with Dynamic ID'

    # WHEN
    browser.element('a[href="/dynamicid"]').click()
    founded_text = browser.element('.btn').text

    # THEN
    assert necessary_text == founded_text


def test_find_button_and_work_with_alert(browser):
    # GIVEN
    browser.open()

    # WHEN
    browser.element('a[href="/classattr"]').click()
    browser.element('.btn-primary').click()
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()
    browser.switch_to.default_content()

    # THEN
    assert text == 'Primary button pressed'
    assert browser.element('section .container h3')()


def test_button_is_unclickable_after_the_first_click(browser):
    # GIVEN
    browser.open()
    button_id = '#greenButton'

    # WHEN
    browser.element('a[href="/hiddenlayers"]').click()
    green_button_webelement = browser.element('#greenButton')()
    location = browser.element('#greenButton').location
    browser.element('#greenButton').click()

    new_element = browser.execute_script(
        'return document.elementsFromPoint(arguments[0], arguments[1]);', location['x'],
        location['y'])

    # THEN
    assert green_button_webelement != new_element


def test_wait_for_a_page_to_load(browser):
    # GIVEN
    browser.open()

    # WHEN/
    browser.element('a[href="/loaddelay"]').click()
    browser.set_wait(timeout=15.0)
    text = browser.element('.btn-primary').text

    # THEN
    assert text == 'Button Appearing After Delay'


def test_wait_for_data_to_appear_after_ajax_request(browser):
    # GIVEN
    browser.open()

    # WHEN
    browser.element('a[href="/ajax"]').click()
    browser.element('#ajaxButton').click()
    browser.set_wait(timeout=15.0)
    text = browser.element('.bg-success').text

    # THEN
    assert text == 'Data loaded with AJAX get request.'


def test_wait_for_data_to_appear_after_client_side_delay(browser):
    # GIVEN
    browser.open()
    # browser.set_wait(timeout=15.0)

    # WHEN
    browser.element('a[href="/clientdelay"]').click()
    browser.element('#ajaxButton').click()
    browser.set_wait(timeout=15.0)
    text = browser.element('.bg-success').text

    # THEN
    assert text == 'Data calculated on the client side.'
