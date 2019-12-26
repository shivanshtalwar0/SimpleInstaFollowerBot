from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup


class webscrapper:
    def reinitialize(self):
        print("reinitializing...")
        self.driver.close()
        self.driver = webdriver.Chrome(executable_path=self.path, options=self.options)

        self.driver.get("https://www.instagram.com/accounts/login/?next=%2Famitabhbachchan%2F&source=desktop_nav")
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.email)
        wait.until(
            EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.password)

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button._0mzm-.sqdOP.L3NKy"))).click()

        pass

    def __init__(self, url="", auth=True, email="", password="",
                 platform="linux",preview=True,otp_timeout=30):
        self.path = ""
        self.email = email
        self.password = password

        if platform == "windows":
            self.path = "./webdrivers/chrome/chromedriver.exe"
        elif platform == "linux":
            self.path = "./webdrivers/chrome/chromedriver"
        elif platform == "macos":
            self.path = "./webdrivers/chrome/chromedriver_mac"

        self.options = webdriver.ChromeOptions()
        self.options.headless = not preview
        self.options.add_argument('--window-size=1200,1200')
        self.driver = webdriver.Chrome(executable_path=self.path, options=self.options)

        if auth:
            self.driver.get("https://www.instagram.com/accounts/login/?next=%2Famitabhbachchan%2F&source=desktop_nav")
            wait = WebDriverWait(self.driver, 5)
            wait.until(
                EC.presence_of_element_located((By.NAME, "username"))).send_keys(email)
            wait.until(
                EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

            wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and div='Log In']"))).click()
            import time
            print('waiting {} seconds in case it asks for otp'.format(otp_timeout))
            time.sleep(otp_timeout)
        self.urls = []

    def seturls(self, urls):
        self.urls = urls

    def followbyurl(self):
        for url in self.urls:
            self.driver.get(url)
            try:
                wait = WebDriverWait(self.driver, 2)
                wait.until(
                    EC.presence_of_element_located((By.XPATH, "//button[text()='Follow']"))).click()
                time.sleep(1)
                print("trying to Follow {}".format(url.split("/")[-2]))
            except:
                print("already following {}".format(url.split("/")[-2]))
                try:
                    wait = WebDriverWait(self.driver, 2)
                    wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button._5f5mN.-fzfL._6VtSN.yZn4P"))).click()
                    wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button.aOOlW.-Cab_"))).click()
                    import time
                    time.sleep(1)
                    print("trying to unfollow")
                except:
                    print("skipping")


#_________________________________________ Configuration of script______________________________________________________________________________________

obj = webscrapper(url="", email="youremail@provider.com",
                  password="yourinstapasswordgoeshere",platform="linux",preview=True,otp_timeout=30)
# by default it runs on linux but you can change according to your platform chromedriver is updated to latest version 79.0.3945.36
# by default otp time out is 30 seconds


# urls is a list of famous instagram profiles
urls = ["https://www.instagram.com/amitabhbachchan/",
        "https://www.instagram.com/cristiano/",
        "https://www.instagram.com/selenagomez/",
        "https://www.instagram.com/eminem/",
        "https://www.instagram.com/robertdowneyjr/",
        "https://www.instagram.com/marvelstudios/",
        "https://www.instagram.com/therock/",
        "https://www.instagram.com/thehughjackman/",
        "https://www.instagram.com/leonardodicaprio/",
        "https://www.instagram.com/davidbeckham/",
        "https://www.instagram.com/wizkhalifa/",
        "https://www.instagram.com/realmadrid/",
        "https://www.instagram.com/leomessi/",
        "https://www.instagram.com/djsnake/",
        "https://www.instagram.com/fcbarcelona/",
        "https://www.instagram.com/champagnepapi/",
        "https://www.instagram.com/vindiesel/",
        "https://www.instagram.com/nickiminaj/",
        "https://www.instagram.com/joynerlucas/",
        "https://www.instagram.com/justinbieber/",
        "https://www.instagram.com/bhuvan.bam22/",
        "https://www.instagram.com/kimkardashian/",
        "https://www.instagram.com/alanwalkermusic/",
        "https://www.instagram.com/kendalljenner/",
        "https://www.instagram.com/arianagrande/",
        "https://www.instagram.com/iamsrk/",
        "https://www.instagram.com/beingsalmankhan/",
        "https://www.instagram.com/ranveersingh/",
        "https://www.instagram.com/katrinakaif/",
        "https://www.instagram.com/shahidkapoor/",
        "https://www.instagram.com/deepikapadukone/",
        "https://www.instagram.com/virat.kohli/",
        "https://www.instagram.com/hrithikroshan/",
        "https://www.instagram.com/tigerjackieshroff/",
        "https://www.instagram.com/dishapatani/",
        "https://www.instagram.com/kritisanon/",
        "https://www.instagram.com/urvashirautela/",
        "https://www.instagram.com/ayushmannk/",
        "https://www.instagram.com/varundvn/",
        "https://www.instagram.com/anushkasharma/",
        "https://www.instagram.com/kapilsharma/",
        "https://www.instagram.com/sunnyleone/",
        "https://www.instagram.com/saraalikhan95/",
        "https://www.instagram.com/aliaabhatt/",
        "https://www.instagram.com/arjunkapoor/",
        "https://www.instagram.com/shrutzhaasan/",
        "https://www.instagram.com/narendramodi/",
        "https://www.instagram.com/ileana_official/",
        "https://www.instagram.com/kajalaggarwalofficial/",
        "https://www.instagram.com/nehakakkar/",
        "https://www.instagram.com/_aamirkhan/",
        "https://www.instagram.com/shreyaghoshal/",
        "https://www.instagram.com/priya.p.varrier/",
        "https://www.instagram.com/safasrour/",
        "https://www.instagram.com/teddymanuel/",
        "https://www.instagram.com/charlieputh/",
        "https://www.instagram.com/shawnmendes/",
        "https://www.instagram.com/taylorswift/",
        "https://www.instagram.com/dualipa/",
        "https://www.instagram.com/marshmellomusic/",
        "https://www.instagram.com/thechainsmokers/",
        "https://www.instagram.com/nickjonas/",
        "https://www.instagram.com/beberexha/",
        "https://www.instagram.com/katyperry/",
        "https://www.instagram.com/priyankachopra/"
        ]

obj.seturls(urls)
for i in range(1000):
    obj.followbyurl()
