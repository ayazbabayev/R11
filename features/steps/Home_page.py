from behave import given, when, then


@given('Open GetTop website')
def open_gettop(context):
    context.app.main_page.open_main()


@when('User clicks on account icon')
def click_account_icon(context):
    context.app.header.click_account_icon()


@then('Verify that {expected_title} window pops up over home page')
def verify_login_window_pops(context, expected_title):
    context.app.homepage.verify_login_window_pops(expected_title)


@when('User clicks on Ipad Pro ad')
def click_displayed_ad_ipad(context):
    context.app.mainpage_ad.displayed_ad_ipad()


@when('User clicks to next slide on ad banner')
def click_next_slide(context):
    context.app.mainpage_ad.click_nextslide()


@when('User clicks on MacBook Pro ad')
def click_displayed_ad_macbook(context):
    context.app.mainpage_ad.displayed_ad_macbook()


@then('Verify that user sees the advertised product in {search_word} page')
def verify_category_page_of_advertised_product_open(context, search_word):
    context.app.product_category_page.verify_category_page_of_advertised_product_open(search_word)
