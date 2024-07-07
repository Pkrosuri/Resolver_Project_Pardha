import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("E:\\Project\\chromedriver-win64\\chromedriver.exe")
from PageObjects.HomePageObjects import HomePageObj

@pytest.fixture()
def setup_and_teardown():
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("file:///E:/Project/Automation_Challenge_Guide/QE-index.html")
    yield driver
    driver.quit()
    time.sleep(1)

def test_email_password_fields_and_login_button(setup_and_teardown):
    driver = setup_and_teardown
    homepage = HomePageObj(driver)
    homepage.verify_email_textbox_is_displayed
    homepage.enter_email_textbox("Resolver@gmail.com")
    homepage.verify_password_textbox_is_displayed()
    homepage.enter_password("resolver123")
    homepage.verify_signin_button_is_displayed_and_perform_click()

def test_listgroup_items(setup_and_teardown):
    driver = setup_and_teardown
    homepage=HomePageObj(driver)
    homepage.verify_number_of_list_items_is_displayed(3)
    homepage.verify_second_list_item("List Item 2")
    homepage.verify_second_list_badge_value("6")

def test_select_option(setup_and_teardown):
    driver = setup_and_teardown
    homepage=HomePageObj(driver)
    homepage.verify_selected_dropdown_is_displayed("Option 1")
    homepage.select_dropdown_option("Option 3")

def test_button_state(setup_and_teardown):
    driver = setup_and_teardown
    homepage = HomePageObj(driver)
    homepage.verfiy_button_is_enabled()

def test_click_button_and_verify_message(setup_and_teardown):
    driver = setup_and_teardown
    homepage = HomePageObj(driver)
    homepage.wait_and_perform_click_action_on_button()
    homepage.verify_success_message("You clicked a button!")
    homepage.verify_button_is_disabled()

def test_find_grid_cell_value(setup_and_teardown):
    driver = setup_and_teardown
    homepage = HomePageObj(driver)
    value = homepage.find_grid_cell_value(2, 2)
    assert value == "Ventosanzap"
