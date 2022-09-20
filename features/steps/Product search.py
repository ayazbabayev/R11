from behave import given, when, then


@when('User hovers over search icon on main page')
def user_hovers_on_search_icon(context):
    context.app.header.user_hovers_over_search_icon()


@when('Leaves search bar blank and clicks on magnifier icon next to it')
def leave_search_blank_and_click_magnifier(context):
    context.app.header.click_magnifier()


@then('Results show correct quantity: {number}.')
def result_show_correct_quantity(context, number):
    context.app.search_results_page.verify_results_show_correct_quantity(number)


# @then('verify results show right number: {expected_no}')
# def verify_results_show_right_number(context, expected_no):
#     context.app.search_results_page.verify_results_show_right_number(expected_no)


@when('User searches for {brand} and clicks on magnifier icon next to it')
def search_product_and_click_magnifier(context, brand):
    context.app.header.search_product(brand)
    context.app.header.click_magnifier()


@then('Results show {brand} products')
def results_show_searched_results(context, brand):
    context.app.search_results_page.results_show_searched_results(brand)

# TMTN-96 ______________________________________________________________


@then('Verify that user can set price with left slider')
def user_can_use_left_slider_set_min_price(context):
    context.app.search_results_page.user_can_use_left_slider_set_min_price()


@then('Verify that user can set price with right slider')
def user_can_use_right_slider_set_min_price(context):
    context.app.search_results_page.user_can_use_right_slider_set_min_price()


@then('Verify that active filter shows min and max')
def user_can_see_active_filter_with_set_prices(context):
    context.app.search_results_page.user_can_see_active_filter_with_set_prices()


@then('Verify that active filters reset when user clicks on min and max')
def verify_active_filters_reset_when_clicked_on_min_max(context):
    context.app.search_results_page.verify_active_filters_reset_when_clicked_on_min_max()
