from selenium import webdriver
# (1)
import unittest
import time
from selenium.webdriver.common.keys import Keys
# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# assert 'To-Do' in browser.title, "Broswer title was" + browser.title


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app. She goes#to check out its homepage
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        self.fail('Finish the test!')
# She notices the page title and header mention to-do listsassert 'To-Do' in browser.title#(4)
# She is invited to enter a to-do item straight away
# She types "Buy peacock feathers" into a text box (Edith's hobby#is tying fly-fishing lures)
# when she hits enter，the page updates，and now the page lists#"1:Buy peacock feathers " as an item in a to-do list
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)
# The page updates again，and now shows both items on her list
# Edith wonders whether the site will remember her list. Then she sees# that the site has generated a unique URL for her -- there is someexplanatory text to that effect.
# She visits that URL - her to-do list is still there.
# Satisfied，she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
