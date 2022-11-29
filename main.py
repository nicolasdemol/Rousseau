from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json
import os
from get_chrome_driver import GetChromeDriver
from get_gecko_driver import GetGeckoDriver




class Voltaire():
    def __init__(self, user_id, user_pwd, browser):
        if(browser == "chrome"):
            self.driver = webdriver.Chrome(
                executable_path="./drivers/chromedriver")
        if(browser == "mozilla"):
            self.driver = webdriver.Firefox(
                executable_path="./drivers/geckodriver")
        self.driver.get(
            "https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?texte&returnUrl=www.projet-voltaire.fr/")
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//input[@type=\"text\"]").send_keys(user_id)
        self.driver.find_element_by_xpath(
            "//input[@type=\"password\"]").send_keys(user_pwd)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        option = self.driver.find_element_by_id('activityCellDiv_3')
        option.click()
        sleep(5)

    def next_move(self):
        suivant = self.driver.find_element(By.ID, "btn_question_suivante")
        suivant.click()
        self.process()

    def ad_fb(self):
        fb = self.driver.find_element_by_id('btn_fermer')
        fb.click()

    def video(self):
        compris = self.driver.find_element_by_class_name('understoodButton')
        compris.click()
        sleep(1)
        answer = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div[3]/div/div[1]/div/button[2]")
        answer.click()
        answer = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div[3]/div/div[2]/div/button[2]")
        answer.click()
        answer = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div[3]/div/div[3]/div/button[2]")
        answer.click()
        sleep(1)
        abandon = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div/div/div/div[5]/button[3]")
        abandon.click()
        sleep(1)

    def process(self):
        pass


class User:

    def check_user():
        if os.path.exists("user.json"):
            with open("user.json", "r+") as save:
                if (save.read() == ""):
                    return False
                else:
                    return True
        else:
            return False

    def save_user():
        print("\n---------------------------------")
        user_id = str(input("> Identifiant: "))
        user_pwd = str(input("> Mot de passe: "))
        print("---------------------------------")
        with open("user.json", "w+") as save:
            json.dump({"id": user_id, "pwd": user_pwd},
                      save, indent=4)

    def load_user():
        with open("user.json", "r+") as save:
            user = json.load(save)
            return user["id"], user["pwd"]


def check_driver(driver_name):
    check = False
    while check == False:
        if (os.path.exists("./drivers")):
            if (os.path.isfile("./drivers/{}".format(driver_name))):
                check = True
            else:
                download_driver(driver_name)
        else:
            os.mkdir("./drivers")
            download_driver(driver_name)


def download_driver(driver_name):
    if (driver_name == "chromedriver"):
        print("\n-> Téléchargement du driver pour Google Chrome en cours...")
        get_driver = GetChromeDriver()
        get_driver.download_stable_version(extract=True, output_path='./drivers/')

    if (driver_name == "geckodriver"):
        print("\n-> Téléchargement du driver pour Mozilla Firefox en cours...")
        get_driver = GetGeckoDriver()
        get_driver.download_latest_version(extract=True, output_path='./drivers')



def select_driver():
    print("\n---------------------------------")
    print("1. Google Chrome")
    print("2. Mozilla Firefox")
    print("---------------------------------")
    use_driver = str(
        input("> Sélectionner le navigateur de votre ordinateur ? (1/2): "))
    browser = "chrome"
    if (use_driver == "1"):
        browser = "chrome"
    if (use_driver == "2"):
        browser = "mozilla"
    return browser


def main():
    print("==========================================")
    print("||             BOT ROUSSEAU             ||")
    print("||         pour Projet Voltaire         ||")
    print("||          par Nicolas Demol           ||")
    print("==========================================")

    check_driver("chromedriver")
    check_driver("geckodriver")
    browser_selected = select_driver()

    us = User

    while True:
        if (us.check_user()):
            os.system("clear")
            user_id, user_pwd = us.load_user()
            print("\n---------------------------------")
            print("Navigateur -> " + browser_selected)
            print("Identifiant -> " + user_id)
            print("Mot de passe -> " + user_pwd)
            print("---------------------------------")
            use_save = str(
                input("> Utiliser ces identifiants ? (Y/n): "))
            if (use_save in ["N", "n"]):
                os.system("clear")
                us.save_user()
                os.system("clear")
                continue
        else:
            os.system("clear")
            us.save_user()
            os.system("clear")
            continue

        bot = Voltaire(user_id, user_pwd, browser_selected)
        bot.process()


if __name__ == "__main__":
    main()
