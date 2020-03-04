from selenium import webdriver
from time import sleep

class Voltaire():
    def __init__(self, username, pw):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?texte&returnUrl=www.projet-voltaire.fr/")
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@type=\"text\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        self.select_prog()

    def select_prog(self):
        option = self.driver.find_element_by_id('activityCellDiv_2') 
        option.click()
        sleep(3)

    def next_move(self):
        pasfaute = self.driver.find_element_by_id('btn_pas_de_faute')
        suivant = self.driver.find_element_by_id('btn_question_suivante')
        mot = self.driver.find_element_by_class_name('pointAndClickSpan')
        sleep(2)
        pasfaute.click()
        sleep(1)
        suivant.click()
        self.process()

    def ad_fb(self):
        fb = self.driver.find_element_by_id('btn_fermer')
        fb.click()
        self.process()

    def video(self):
        compris = self.driver.find_element_by_class_name('understoodButton')
        compris.click()
        sleep(1)
        answer = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[1]/div/button[2]")
        answer.click()
        answer = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[2]/div/button[2]")
        answer.click()
        answer = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[3]/div/button[2]")
        answer.click()
        sleep(1)
        abandon = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[5]/button[3]")
        abandon.click()
        sleep(1)
        self.process()



    def process(self):
        try:
            self.next_move()    
        except:
            try:
                self.ad_fb()
            except:
                self.video()

        

bot = Voltaire('nicolas.demol@esme.fr','125478Nyco-')
bot.process()
