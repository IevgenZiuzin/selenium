from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://www.google.com/'
PREfIX = 'search?q='


def get_search_results(prompts):
    suffix = '+'.join(prompts)
    search_query = URL + PREfIX + suffix
    try:
        driver = webdriver.Chrome()
    except:
        driver = webdriver.Safari()

    try:
        driver.get(URL)
        assert "Google" in driver.title
        elem = driver.find_element(By.CSS_SELECTOR, "button:nth-of-type(2)")
        elem.click()
    except:
        driver.get(search_query)

    driver.implicitly_wait(5)

    results_wrapper = driver.find_element(By.CSS_SELECTOR, "#search")
    results = results_wrapper.find_elements(By.TAG_NAME, "h3")
    for result in results[:5]:
        title = result.get_attribute('innerHTML')
        url = result.find_element(By.XPATH, "..").get_attribute('href')
        if url:
            print(title)
            print(url)
            print('\n')
    driver.close()


if __name__ == '__main__':
    get_search_results(['python', 'developer'])
