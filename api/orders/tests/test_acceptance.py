from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class OrderAcceptanceTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_customer_creation(self):
        self.browser.get(self.live_server_url + '/create_customer')

        customer_name_input = self.browser.find_element(By.ID, 'name')
        customer_name_input.send_keys('Test Customer')

        customer_code_input = self.browser.find_element(By.ID, 'code')
        customer_code_input.send_keys('TC001')

        customer_email_input = self.browser.find_element(By.ID, 'phone')
        customer_email_input.send_keys("123456")

        create_customer_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Create Customer')]")
        self.assertTrue(create_customer_button.is_displayed())

        create_customer_button.click()

    def test_order_creation(self):

        self.browser.get(self.live_server_url + '/create_order')

        
        customer_select = Select(self.browser.find_element(By.ID, 'customer'))
        customer_select.select_by_visible_text('manu')  # Replace 'Customer Name' with the actual name

    # Select an item from the dropdown
        item_select = Select(self.browser.find_element(By.ID, 'item'))
        item_select.select_by_visible_text('Hospital Bed')  # Replace 'Item Name' with the actual item name

        quantity_input = self.browser.find_element(By.ID, 'quantity')
        quantity_input.clear()
        quantity_input.send_keys('3') 

        submit_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Create Order')]")
        submit_button.click()

        self.assertIn('order-detail', self.browser.title)

        

    