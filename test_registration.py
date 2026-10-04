import allure


@allure.feature("Registration")
def test_registration(registration_page):
    registration_page.register_user(
        "Lana",
        "Shanava",
        "marilan171191+6@gmail.com",
        "Lanatest1!"
    )
    registration_page.check_registration()