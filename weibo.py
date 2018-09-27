from selenium import webdriver
import re
import tesserocr
from PIL import Image 
def get_cookie():
    #获取连接图片
    url_login = 'https://weibo.com/'
    driver = webdriver.PhantomJS()
    driver.get(url_login)
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[1]/div/input/[@type="text"]').send_keys('15270284451')
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input/[@type="password"]').send_keys('wawnsbxysmly')
    a = url_login.xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img/@src')
    with open('code.jpg','wb') as f:
        f.write(a)
    image = Image.open('code.jpg')
    result = tesserocr.image_to_text(imange)
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input/[@type="text"]').send_keys(str(result))
    driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span/[@node-type="submitStates"]').click()
    cookie_list = driver.get_cookies()
    print(cookie_list)
    cookie_dict = {}
    for cookie in cookie_list:
        with open('weibo','wb') as f:
            f.write(cookie)
    f.close()
    
get_cookie()

