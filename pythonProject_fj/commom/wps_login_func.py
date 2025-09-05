import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def func(driver, phone, password):
    driver.get("https://account.wps.cn/")  # 打开金山文档
    driver.maximize_window()  # 网页最大化

    # driver.find_element(By.XPATH, '//*[@id="pcLoginWrap"]/div[5]/div[2]').click()  # 点击切换账号
    driver.find_element(By.XPATH, '//*[@id="footWrap"]/div[3]/a[4]/span[1]').click()  # 点击更多
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dialog"]/div[2]/div/div[3]/div[2]')))  # 显示等待“弹出隐私协议”
    driver.find_element(By.XPATH, '//*[@id="dialog"]/div[2]/div/div[3]/div[2]').click()  # 点击同意
    driver.find_element(By.XPATH, '//*[@id="account"]/span[2]').click()  # 点击账号密码
    time.sleep(2)

    # 通过 ID 或 index 切换
    driver.switch_to.frame(0)

    # 操作元素
    driver.find_element(By.ID, 'email').send_keys(phone)  # 输入账号  //*[@id="email"]
    driver.find_element(By.ID, 'password').send_keys(password)  # 输入密码
    driver.find_element(By.XPATH, '//*[@id="rectBottom"]').click()  # 点击智能验证
    # time.sleep(5)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "验证成功")]')))  # 显示等待“验证成功”
    driver.find_element(By.XPATH, '//*[@id="login"]').click()  # 点击登录
    # 切换回主页面
    driver.switch_to.default_content()

    # wait = WebDriverWait(driver, 10)
    # wait.until(lambda dri: driver.find_element(By.PARTIAL_LINK_TEXT, '发送验证码'))
    # Msg = driver.find_element(By.PARTIAL_LINK_TEXT, '发送验证码').text

    wait = WebDriverWait(driver, 10)
    wait.until(lambda dri: driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]'))  # 显示等待跳转到“个人中心”
    msg = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[1]').text
    return msg

