from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from time import sleep

import pyperclip
import urllib.request

import bs4

# No close browser when finish test and full-screen browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")


# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Firefox()
# driver.get("http://dlib.ptit.edu.vn/flowpaper/simple_document.php?subfolder=30/16/21/&doc=30162126041710350305223424440233135951&bitsid=dd544e34-2a5e-4c19-841f-38f79db31fad&uid=869e977e-9ed5-4588-8f4c-f169046ea281")

def login():
    # inputUsername = driver.find_element_by_id("tlogin_email")
    inputUsername = driver.find_element(By.ID, "tlogin_email")
    inputUsername.send_keys(username)
    inputPassword = driver.find_element(By.ID, "tlogin_password")
    inputPassword.send_keys(password)
    inputPassword.send_keys(Keys.ENTER)
    
def download():
    elem = driver.find_element(By.ID, "page_0_documentViewer")
    src = elem.get_attribute("src")
    print(src)
    div_count = driver.find_elements(By.CLASS_NAME, "flowpaper_page")
    count = len(div_count)
    src = src.replace("page=1", "page=n")
    print("new src: ", src)
    for i in range(count):
        page = "page="+str(i+1)
        new_src = src.replace("page=n", page)
        location = "D:/Workspace/LibScraping/imgdl/"+str(i+1)+".jpg"
        urllib.request.urlretrieve(new_src, location)
        

link = input("Mời bạn nhập trang sách thư viện bạn muốn crawl về: ")
username = input("Mời bạn tài khoản: ")
password = input("Mời bạn nhập mật khẩu: ")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(link)
sleep(3)
login()
sleep(7)
download()

sleep(5)
driver.close()