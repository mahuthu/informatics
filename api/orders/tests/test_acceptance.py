from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OrderAcceptanceTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_order_creation(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Orders', self.browser.title)

        customer_name_input = self.browser.find_element_by_name('customer_name')
        customer_name_input.send_keys('Test Customer')

        customer_code_input = self.browser.find_element_by_name('customer_code')
        customer_code_input.send_keys('TC001')

        customer_email_input = self.browser.find_element_by_name('customer_email')
        customer_email_input.send_keys("tester@gmail.com")

        create_customer_button = self.browser.find_element_by_xpath("//button[contains(text(), 'Create Customer')]")
        self.assertTrue(create_customer_button.is_displayed())

        create_customer_button.click()

        
        customer_select = self.browser.find_element_by_id('customer')
        customer_option = customer_select.find_elements_by_tag_name('option')[1]  
        customer_option.click()

        item_select = self.browser.find_element_by_id('item')
        item_option = item_select.find_elements_by_tag_name('option')[1]  
        item_option.click()

        quantity_input = self.browser.find_element_by_id('quantity')
        quantity_input.clear()
        quantity_input.send_keys('3') 

        submit_button = self.browser.find_element_by_xpath("//button[contains(text(), 'Create Order')]")
        submit_button.click()

        self.assertIn('order-detail', self.browser.title)

        success_message = self.browser.find_element_by_css_selector('.alert-success')
        self.assertIn('Order placed successfully', success_message.text)


    