from selenium import webdriver
import platform

class BrowserInt():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        os_platform = platform.system()
        if os_platform == 'Linux':
            driver_path = webdriver.Firefox(executable_path='./geckodriver')
        elif os_platform == 'Darwin':
            driver_path = webdriver.Chrome()

        driver = driver_path

        driver.maximize_window()
        driver.get(baseUrl)

        title = driver.title
        print('Title of webpage is {}'.format(title))
        currentUrl = driver.current_url
        print('Current URL of page is {}'.format(currentUrl))

        driver.refresh()
        print('Browser refreshed 1st time')
        driver.get(driver.current_url)
        print('Browser refreshed 2nd time')

        driver.get('https://www.google.com')
        print('Current URL of page is {}'.format(driver.current_url))
        driver.back()
        print('Browser went one step back in history')
        print('Current URL of page is {}'.format(driver.current_url))
        driver.forward()
        print('Browser went one step forward in history')

        source = driver.page_source
        driver.close()
        driver.quit()


ff = BrowserInt()
ff.test()
