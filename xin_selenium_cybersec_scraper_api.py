from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_exd_detail(url, driver):
    data = dict()
    driver.get(url)

    # 電話
    telephone_element = driver.find_element(By.CLASS_NAME, 'info-tel')
    if telephone_element: # 確定有東西
        data['telephone'] = telephone_element.text

    # EMAIL
    email_element = driver.find_element(By.CLASS_NAME, 'info-mail')
    if email_element: # 確定有東西
        data['email'] = email_element.text

    # Website
    website_elements = driver.find_elements(By.CLASS_NAME, 'border-icon')
    if website_elements: # 確定有找到東西
        for website_element in website_elements:
            # 利用 element.get_attribute("屬性名稱") 取得資訊
            href = website_element.get_attribute('href')
            if href:
                for social_media_name in ['facebook', 'twitter', 'linkedin', 'instagram']:
                    if social_media_name in href:
                        data[social_media_name] = href
                else:
                    data['website'] = href

    # Description
    desc_element = driver.find_element(By.CLASS_NAME, 'ex-foreword')
    if desc_element: # 確定有東西
        data['description'] = desc_element.text

    return data


if __name__ == '__main__':
    test_driver = webdriver.Firefox()
    exd_url = "https://cybersec.ithome.com.tw/2024/exhibition-page/2043"
    exd_data = get_exd_detail(
        url=exd_url,
        driver=test_driver
    )
    print(exd_data)
    test_driver.close()