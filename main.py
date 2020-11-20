from time import sleep
from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from secrets import username
from secrets import pw

from sheetsapi import code_values

class ClassroomBot:
    def __init__(self, username, pw):
        self.driver = Safari()
        #self.driver.maximize_window()
        self.driver.get(
            "https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F"
            "%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName"
            "=GlifWebSignIn&flowEntry=ServiceLogin "
        )

        # Username Field
        self.driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(username + Keys.ENTER)

        # Password field
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type=\"password\"]"))).send_keys(pw + Keys.ENTER)

        sleep(10)

        for code in code_values:
            self.driver.get("https://classroom.google.com/u/0/h")
            sleep(10)
            # '+' button

            self.driver.find_element_by_xpath('//*[@id="ow23"]/div').click()
            sleep(1)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.ENTER)

            # try:
            #     element = WebDriverWait(self.driver, 10).until(
            #         EC.presence_of_element_located(By.XPATH, '//*[@id="ow40"]'))
            # finally:
            #     self.driver.quit()
            # element.click()

            #buttons = self.driver.find_elements(By.TAG_NAME, 'div');
            #print(buttons);
            #buttons[0].click;
            sleep(1)
            # Join class
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label=\"Join class\" or "
                                                             "@aria-label=\"Înscrieți-vă la curs\"]"))).click()

            sleep(1)
            # Code field
            code_field = self.driver.find_element_by_xpath("//input")
            code_field.send_keys(code + Keys.ENTER)
            sleep(5)


ClassroomBot(username, pw)
