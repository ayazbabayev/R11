from behave import given, then


@then('Verify that user can add product(s) to wishlist')
def verify_user_can_add_products_to_wishlist(context):
    context.app.wishlist_page.verify_user_can_add_products_to_wishlist()


@then('User can click the product in wishlist and go to product page')
def user_can_click_the_product_in_wishlist_and_go_to_product_page(context):
    context.app.wishlist_page.user_can_click_the_product_in_wishlist_and_go_to_product_page()


@then('User can go back to previous page')
def user_can_go_back_to_previous_page(context):
    context.app.wishlist_page.user_can_go_back_to_previous_page()


@then('Verify that user sees {number} product(s) in wishlist')
def verify_user_sees_correct_qty_in_wishlist(context, number):
    context.app.wishlist_page.verify_user_sees_correct_qty_in_wishlist(number)


@then('Verify sees 4 logos for sharing options in wishlist')
def verify_user_sees_4_logos_for_sharing_ops(context):
    context.app.wishlist_page.verify_user_sees_4_logos_for_sharing_ops()


@then('Verify that user can remove product(s) in wishlist')
def verify_that_user_can_remove_products_in_wishlist(context):
    context.app.wishlist_page.verify_that_user_can_remove_products_in_wishlist()


@then('Verify that user sees empty wishlist')
def verify_that_user_sees_no_products_in_wishlist(context):
    context.app.wishlist_page.verify_that_user_sees_no_products_in_wishlist()


@given('Open GetTop Wishlist page')
def open_gettop_wishlist_page(context):
    context.app.wishlist_page.open_gettop_wishlist_page()
