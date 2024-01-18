from selene import browser, be, have


def test_google_search(firefox, browser_size):
    browser.open('https://www.google.com/')
    browser.element('[name = "q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id = "search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print('Correct Google result')


def test_noresults_search(firefox, browser_size):
    browser.open('https://www.google.com/')
    browser.element('[name = "q"]').should(be.blank).type('fsdfsdfj"elfjWEJOFP23IR]9йцу').press_enter()
    assert browser.element('[id = "result-stats"]').should(have.text('0'))
    print('No results are found in Google')
