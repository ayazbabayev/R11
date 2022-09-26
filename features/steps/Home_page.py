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


@when('User clicks on GetTop logo')
def user_clicks_gettop_logo(context):
    context.app.homepage.user_clicks_gettop_logo()


@then('Verify that user reaches GetTop home page')
def verify_user_reaches_homepage(context):
    context.app.homepage.verify_user_reaches_homepage()


@when('User scrolls page to the bottom')
def user_scrolls_page_to_bottom(context):
    context.app.footer.user_scrolls_page_to_bottom()


@then('User can see bestselling, latest and top rated categories')
def user_sees_bestselling_latest_toprated(context):
    context.app.footer.user_sees_bestselling_latest_toprated()


@then('Verify that bestselling, latest and top rated section have {expected_qty} product names')
def verify_bs_lat_tr_have_11_product_names(context, expected_qty):
    context.app.footer.verify_bs_lat_tr_have_11_product_names(expected_qty)


@then('Verify that bestselling, latest and top rated section have {expected_qty} prices')
def verify_bs_lat_tr_have_12_prices(context, expected_qty):
    context.app.footer.verify_bs_lat_tr_have_12_prices(expected_qty)

@then('Verify that "Copyright 2022" shown in footer')
def verify_copyright2022_shown_in_footer(context):
    context.app.footer.verify_copyright2022_shown_in_footer()

@then('Verify that Footer has button to go back to top and its functional')
def verify_footer_has_gototop_button_and_functional(context):
    context.app.footer.verify_footer_has_gototop_button_and_functional()

@then('Verify that Footer has working links to all product categories')
def verify_footer_links_connect_to_all_product_categories(context):
    context.app.footer.verify_footer_links_connect_to_all_product_categories()