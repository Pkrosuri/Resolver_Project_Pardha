from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePageObj:
    email_text_box='//input[@placeholder="Email address"]'
    password_text_box='//input[@placeholder="Password"]'
    signin_button='//button[@type="submit" and contains(text(),"Sign in")]'
    list_items='//ul[@class="list-group"]//following-sibling::li'
    badge_items='//ul[@class="list-group"]//following-sibling::li//span'
    dropdown='//button[@data-toggle="dropdown"]'
    enabled_button='//button[text()="Button" and not(@disabled)]'
    alert_text_element='//div[contains(@class,"alert")]'


    def __init__(self,driver):
        self.driver=driver

    def verify_email_textbox_is_displayed(self):
        email_textbox = self.driver.find_element(By.XPATH, self.email_text_box)
        assert email_textbox.is_displayed(), "Email Text Box Is Not Displayed"

    def enter_email_textbox(self,email):
        email_textbox = self.driver.find_element(By.XPATH, self.email_text_box)
        email_textbox.clear()
        email_textbox.send_keys(email)  #"Resolver@gmail.com")

    def verify_password_textbox_is_displayed(self):
        password_textbox = self.driver.find_element(By.XPATH, self.password_text_box)
        assert password_textbox.is_displayed(), "Password Text Box Is Not Displayed"

    def enter_password(self,password):
        password_textbox = self.driver.find_element(By.XPATH, self.password_text_box)
        password_textbox.clear()
        password_textbox.send_keys(password)

    def verify_signin_button_is_displayed_and_perform_click(self):
        signin_button = self.driver.find_element(By.XPATH, self.signin_button)
        assert signin_button.is_displayed(), "Sign In Button Is Not Displayed"
        signin_button.click()

    def verify_number_of_list_items_is_displayed(self,val):
        listgroup = self.driver.find_elements(By.XPATH, self.list_items)
        print(len(listgroup))
        assert len(listgroup) == val  #3

    def verify_second_list_item(self,item):
        listgroup = self.driver.find_elements(By.XPATH, self.list_items)
        second_list_item = listgroup[1].text.split('\n')[0]
        print(second_list_item)
        assert second_list_item.__contains__(item)   #List Item 2

    def verify_second_list_badge_value(self,badge_val):
        second_list_item_badge_value = self.driver.find_elements(By.XPATH, self.badge_items)
        assert second_list_item_badge_value[1].text == badge_val  #"6"

    def verify_selected_dropdown_is_displayed(self,val):
        dropdown_value = self.driver.find_element(By.XPATH,self.dropdown)
        assert dropdown_value.text.__contains__(val)  #"Option 1"

    def select_dropdown_option(self,option):
        self.driver.find_element(By.XPATH, self.dropdown).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, f'//a[text()="{option}"]')))
        self.driver.find_element(By.XPATH, f'//a[text()="{option}"]').click()  #Option 3

    def verfiy_button_is_enabled(self):
        button_enabled = self.driver.find_element(By.XPATH, self.enabled_button)
        assert button_enabled.is_enabled(), 'button is disabled'

    def wait_and_perform_click_action_on_button(self):
        button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.ID, 'test5-button')))
        button.click()

    def verify_success_message(self,text):
        success_msg_element = self.driver.find_element(By.XPATH, self.alert_text_element).text
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.alert_text_element)))
        assert success_msg_element.__contains__(text)

    def verify_button_is_disabled(self):
        button_element = self.driver.find_element(By.ID, 'test5-button')
        assert not button_element.is_enabled(), 'button is enabled'

    def find_grid_cell_value(self, row, col):
        cell_value = self.driver.find_element(By.XPATH, f'//table[@class="table table-bordered table-dark"]/child::tbody/tr[{row + 1}]/td[{col + 1}]')
        cell_value = cell_value.text
        return cell_value























