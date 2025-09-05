import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commom.wps_login_func import func
from commom.tools import get_txt_data


# fixture前置登录，后置关闭页面
@pytest.fixture(scope='class')
def driver():
    login_datas = get_txt_data()
    for i in login_datas:
        service = Service(r"C:\Users\syb\python_fj\pythonProject_fj\pythonProject_fj\chromedriver.exe")
        dri = webdriver.Chrome(service=service)
        # 隐式等待再进行登录操作
        dri.implicitly_wait(10)
        msg = func(dri, i[0], i[1])
        assert msg == '个人中心'
        yield dri
        dri.close()


class TestPersonal:
    def test_avatar(self, driver):
        # 点击修改头像
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/img').click()
        # 显示等待头像上传框出现，再点击上传
        wait = WebDriverWait(driver, 10)
        wait.until(lambda dri: driver.find_element(By.XPATH, '//span[contains(text(), "请选择要上传的图片")]'))
        driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(r"C:\Users\syb\Pictures\Camera Roll\IMG_5538.JPG")
        # 显示等待头像定位调整框出现，再点击确定
        wait = WebDriverWait(driver, 10)
        wait.until(lambda dri: driver.find_element(By.XPATH,
                                                   '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/span[5]'))
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div[4]/div/button[2]/span').click()
        # 显示等待修改生效提示框
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(lambda dri: driver.find_element(By.XPATH, '/html/body/div[3]/div/p'))
            msg = driver.find_element(By.XPATH, '//p[contains(text(),"修改将在24小时内生效，请耐心等待")]').text
            assert msg == '修改将在24小时内生效，请耐心等待'

        except:
            wait = WebDriverWait(driver, 10)
            wait.until(lambda dri: driver.find_element(By.XPATH, '//p[contains(text(),"一周内仅可修改 2 次头像")]'))
            msg = driver.find_element(By.XPATH, '//p[contains(text(),"一周内仅可修改 2 次头像")]').text
            assert msg == '一周内仅可修改 2 次头像'
