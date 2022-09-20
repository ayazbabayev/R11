from behave import when, then


@when('User clicks on LAPTOPS category')
def click_product_category(context):
    context.app.header.header_laptops()


@then('Verify that user sees the {search_word} category page')
def verify_user_sees_laptops_page(context, search_word):
    context.app.product_category_page.verify_user_sees_laptops_page(search_word)
