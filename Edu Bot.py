import hashlib
import platform
import random
import string
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class FakeNameGenerator():
    def __init__(self):
        self.html = ""

    def GenerateIdenity(self):
        self.html = requests.get("https://www.fakenamegenerator.com/",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}).text
        self.name = {"completename":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0],"first":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[0],"last":self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[-1]}

        addy = self.html.split('<div class="adr">')[1].split("                                        ")[1].split("                                        </div>")[0]
        addynum = addy.split(" ")[0]
        streetlist = self.html.split('<div class="adr">')[1].split("                                        ")[1].split("                                        </div>")[0].split("<br />")[:1][0].split(" ")[1:]
        street = ""

        province = addy.split('<br />')[1].split(",")[0]
        ZIP = addy.split(", ")[1].split('   ')[0]
        for i in streetlist:
            street = street + " " + i
        self.addy = {"addynum":addynum,"street":street[1:],"province":province,"zip":ZIP}

        self.SSN = self.html.split('tal"><dt>SSN</dt><dd>')[1].split(' <div class="adtl">')[0]
        self.phone = self.html.split("<dt>Phone</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.phoneprefix = "+" + self.html.split("<dt>Country code</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        birthday = "+" + self.html.split("<dt>Birthday</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        Month = birthday.split(" ")[0].replace("+","")
        Day = birthday.split(" ")[1].replace(",","")
        Year = birthday.split(" ")[-1]
        self.birthday = {"Day":Day,"Month":Month,"Year":Year}
        self.age = self.html.split("<dt>Age</dt>")[1].split(" years old</dd>")[0].split("<dd>")[1]
        self.tropicalzodiac = self.html.split("<dt>Tropical zodiac</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.email = self.html.split('<dt>Email Address</dt>')[1].split('<dd>')[1].split('        ')[0]
        self.username = self.html.split("<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.password = self.html.split("<dt>Password</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.website = self.html.split("<dt>Website</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.useragent = self.html.split("<dt>Browser user agent</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.cardtype = self.html.split('<h3 class="hh3">Finance</h3>')[1].split('<dt>')[1].split('</dt>')[0]
        self.card = self.html.split(f"<dt>{self.cardtype}</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.exp = self.html.split("<dt>Expires</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        try:
            self.CVC = self.html.split("<dt>CVC2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        except:
            self.CVC = self.html.split("<dt>CVV2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.company = self.html.split("<dt>Company</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.job = self.html.split("<dt>Occupation</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.height = self.html.split("<dt>Height</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.weight = self.html.split("<dt>Weight</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.bloodtype = self.html.split("<dt>Blood type</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.UPSTrackingnum = self.html.split("<dt>UPS tracking number</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.MoneyGram = self.html.split("<dt>MoneyGram MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.WesternUnion = self.html.split("<dt>Western Union MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.favcolor = self.html.split("<dt>Favorite color</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.car = self.html.split("<dt>Vehicle</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.GUID = self.html.split("<dt>GUID</dt>")[1].split("</dd>")[0].split("<dd>")[1]

generated = 0

def createaccount(collage,use_captcha):
    try:
        Bot(collage, use_captcha)
    except:
        createaccount(collage, use_captcha)

def randomSSN(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def Bot(collage,use_captcha):
    
    

    try:
        config = open("config.txt", "r+").readlines()
        mail = config[0]
    except:
        mail = "@tempr.email"
        pass
    try:
        captcha = config[1]
        captcha, _ = captcha.split("\n")
    except:
        pass
    try:
        full_mail = config[2]
        fullmail = 1
    except:
        fullmail = 0
        pass






    driver = webdriver.Firefox(executable_path=geckopath)

    driver.get("https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s2")

    datafake = FakeNameGenerator()
    datafake.GenerateIdenity()
    
    first = datafake.name["first"]
    last = datafake.name["last"]
    number = datafake.phone
    ssn = str(str(datafake.SSN) + str(randomSSN())).replace("X","")
    street = datafake.addy["addynum"] + " " + datafake.addy["street"]
    city = datafake.addy["province"]
    zipcode = datafake.addy["zip"]

    pw = datafake.password
    name = datafake.username + randomSSN()
    
    if fullmail == 0:
        email = name + mail
    else:
        email = full_mail

    ssnlol = ssn

    register_button = driver.find_element_by_name("_eventId_continue")
    register_button.click()


    first_name = driver.find_element_by_name("firstName")
    first_name.send_keys(first)
    time.sleep(4)
    driver.find_element_by_id("inputHasNoMiddleName").click()
    last_name = driver.find_element_by_id("inputLastName")
    last_name.send_keys(last)
    time.sleep(4)
    prev_name = driver.find_element_by_id("hasOtherNameNo")
    prev_name.click()
    preffered_name = driver.find_element_by_id("hasPreferredNameNo")
    preffered_name.click()
    time.sleep(4)

    driver.find_elements_by_tag_name("option")[10].click()
    driver.find_elements_by_tag_name("option")[27].click()
    year = driver.find_element_by_name("birthDateModel.year")
    year.send_keys("1994")
    time.sleep(4)
    driver.find_elements_by_tag_name("option")[55].click()
    driver.find_elements_by_tag_name("option")[72].click()
    time.sleep(4)
    year_confirm = driver.find_element_by_name("birthDateModel.yearConfirm")
    year_confirm.send_keys("1994")
    driver.find_element_by_id("inputSSNTypeSSN").click()
    driver.find_element_by_id("inputSsn").send_keys(ssnlol)
    driver.find_element_by_id("inputSsnConfirm").send_keys(ssnlol)
    time.sleep(1)
    driver.find_element_by_id("accountFormSubmit").click()
        
    print("[*] Page 1/3 Done!")

    time.sleep(4)


    
    driver.find_element_by_id("inputEmail").send_keys(email)
    driver.find_element_by_id("inputEmailConfirm").send_keys(email)
    time.sleep(4)
    driver.find_element_by_id("inputSmsPhone").send_keys(number)
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    time.sleep(4)
    driver.find_element_by_id("accountFormSubmit").click()







    


    try:
        driver.find_element_by_id("inputUserId").send_keys(name)
        print("[*] Page 2/3 Done!")
    except:
        driver.find_element_by_id("error-modal-ok-button").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_id("accountFormSubmit").click()
        
    print("[*] Page 2/3 Done!")   
    driver.find_element_by_id("inputUserId").send_keys(name)
    driver.find_element_by_id("inputPasswd").send_keys(pw)
    driver.find_element_by_id("inputPasswdConfirm").send_keys(pw)


    driver.find_element_by_id("inputPin").send_keys("0420")
    driver.find_element_by_id("inputPinConfirm").send_keys("0420")

    driver.find_elements_by_tag_name("option")[10].click()
    driver.find_element_by_id("inputSecurityAnswer1").send_keys("12")

    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_id("inputSecurityAnswer2").send_keys("Josh")

    driver.find_elements_by_tag_name("option")[42].click()
    driver.find_element_by_id("inputSecurityAnswer3").send_keys("Tesla 3")




    print("[*] Bypassing the Captcha!")

    if use_captcha == "1":


        url = "https://2captcha.com/in.php?key=" + captcha + "&method=userrecaptcha&json=0&googlekey=6LeaXhITAAAAACiHR6YSn1YKAUrrTZTLtjxuwYx6&pageurl=https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s4"

        r = requests.get(url)



        _, moin = r.text.split("|")
        time.sleep(20)

        url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
        r = requests.get(url2)
        while "CAPCHA_NOT_READY" in r.text:

            url2 = "https://2captcha.com/res.php?key=" +captcha + "&action=get&id=" + moin
            r = requests.get(url2)
            print("[*] Waiting for 2Captcha")
            time.sleep(3)
        try:
            _, key = r.text.split("|")
        except:
            print(r.text)

        command = 'document.getElementById("g-recaptcha-response").innerHTML="' + key + '";'
        driver.execute_script("document.getElementsByName('captchaResponse')[0].setAttribute('type', 'shown');")
        driver.find_element_by_name("captchaResponse").send_keys(key)
        time.sleep(5)
        driver.execute_script(command)
    elif use_captcha == "2":
        print("Solve the captcha now!\n\n")
        captcha_solved = "1"
        while captcha_solved == "1":
            captcha_solved = input("[Y]Solved?\n")
    else:
        print("Error")


    time.sleep(3)
    driver.find_element_by_id("accountFormSubmit").click()
    time.sleep(5)

    print("[*] Page 3/3 Done!")

    driver.quit()

    time.sleep(3)

    if collage == "1":
        resp = Coastline(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "2":
        resp = Coastline(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "3":
        resp = Crafton(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "4":
        resp = San_Bernardino(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "5":
        resp = Santa_Monica(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "6":
        resp = Solano(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "7":
        resp = ccsf(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "8":
        resp = Canada(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "9":
        resp = barbara(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "10":
        resp = gavilan(name,pw,email,first,last,number,ssn, street, city, zipcode)
    elif collage == "11":
        resp = orange(name,pw,email,first,last,number,ssn, street, city, zipcode)
    else:
        print("Fuck")
        exit()
    
    
    global generated
    generated += 1
    with open("accountsb.txt", "a+") as file:
        file.write(resp[0] + ":" + resp[1] + "  Email:" + resp[2] + " " + resp[3] + " " + resp[4] + " SSN: " + resp[5] + " number: " + resp[6])
        file.write("\n")

def orange(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    


    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('833')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
        
    
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
#supplemental

    driver.find_element_by_id("_supp_TEXT_1").send_keys(city)
    state = Select(driver.find_element_by_id('_supp_STATE_1'))
    state.select_by_value('CA')
    driver.find_element_by_id("YESNO_2_no").click()
    driver.find_element_by_id("YESNO_3_no").click()
    time.sleep(0.5)
    state = Select(driver.find_element_by_id('_supp_MENU_1'))
    state.select_by_value('10')
    driver.find_element_by_id("_supp_CHECK_29").click()    
    driver.find_element_by_name("_eventId_continue").click()


#submisson

    time.sleep(0.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 seconds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)




def gavilan(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    


    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('441')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
        
    
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#supplemental

    driver.find_element_by_id("_supp_TEXT_1").send_keys(first)
    driver.find_element_by_id("_supp_TEXT_2").send_keys(last)
    driver.find_element_by_id("_supp_TEXT_3").send_keys("54412")
    time.sleep(1)
    driver.find_element_by_id("_supp_TEXT_4").send_keys(number)
    driver.find_element_by_id("_supp_TEXT_6").send_keys(street)
    driver.find_element_by_id("_supp_TEXT_8").send_keys(city)
    time.sleep(1)
    driver.find_element_by_id("_supp_TEXT_9").send_keys(zipcode)
    relation = Select(driver.find_element_by_id('_supp_MENU_1'))
    relation.select_by_value('N')
    state = Select(driver.find_element_by_id('_supp_STATE_1'))
    state.select_by_value('CA')
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)

#submisson

    time.sleep(0.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 seconds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)


def barbara(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    


    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    time.sleep(484)
    collage.select_by_value('651')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#supplemental

    supp1 = Select(driver.find_element_by_id('_supp_MENU_1'))
    supp1.select_by_value('15')

    supp2 = Select(driver.find_element_by_id('_supp_MENU_2'))
    supp2.select_by_value('01')
    time.sleep(1.5)

    supp3 = Select(driver.find_element_by_id('_supp_MENU_3'))
    supp3.select_by_value('7')
    time.sleep(1.5)
    supp5 = Select(driver.find_element_by_id('_supp_MENU_5'))
    supp5.select_by_value('Y')

    supp4 = Select(driver.find_element_by_id('_supp_MENU_4'))
    supp4.select_by_value('N')

    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)

#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 seconds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)


def Canada(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
#collage auswahl

    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('371')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)

#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)

def Solano(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass

#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('281')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    driver.find_element_by_id("_supp_CHECK_1").click()
    driver.find_element_by_name("_eventId_continue").click()
#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)

def ccsf(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('361')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    Select(driver.find_element_by_id("_supp_MENU_1")).select_by_value('ENG')
    time.sleep(2)
    Select(driver.find_element_by_id("_supp_MENU_5")).select_by_value('N')
    Select(driver.find_element_by_id("_supp_MENU_6")).select_by_value('N')
    Select(driver.find_element_by_id("_supp_MENU_4")).select_by_value('OPT2')
    driver.find_element_by_id("_supp_CHECK_5").click()
    time.sleep(3)
    driver.find_element_by_name("_eventId_continue").click()

#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(27)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)





def San_Bernardino(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('982')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('K')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    Special = Select(driver.find_element_by_id('_supp_MENU_1'))
    Special.select_by_value('WEBS')
    time.sleep(1)

    Married = Select(driver.find_element_by_id('_supp_MENU_2'))
    Married.select_by_value("U")

    driver.find_element_by_id("_supp_TEXT_1").send_keys(name)
    time.sleep(1)

    driver.find_element_by_id("_supp_TEXT_2").send_keys(number)
    driver.find_element_by_id("_supp_TEXT_3").send_keys(number)

    Parent = Select(driver.find_element_by_id('_supp_MENU_3'))
    Parent.select_by_value("Parent")

    driver.find_element_by_id("YESNO_1_no").click()
    driver.find_element_by_id("YESNO_3_yes").click()

    driver.find_element_by_name("_eventId_continue").click()
#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)



def Crafton(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('981')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    Special = Select(driver.find_element_by_id('_supp_MENU_1'))
    Special.select_by_value('WEBS')
    time.sleep(1)

    Married = Select(driver.find_element_by_id('_supp_MENU_2'))
    Married.select_by_value("U")

    driver.find_element_by_id("_supp_TEXT_1").send_keys(name)
    time.sleep(1)

    driver.find_element_by_id("_supp_TEXT_2").send_keys(number)
    driver.find_element_by_id("_supp_TEXT_3").send_keys(number)

    Parent = Select(driver.find_element_by_id('_supp_MENU_3'))
    Parent.select_by_value("Parent")

    driver.find_element_by_id("YESNO_1_no").click()
    driver.find_element_by_id("YESNO_2_no").click()


    driver.find_element_by_name("_eventId_continue").click()
#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)

def San_Bernardino(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    

    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('982')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('K')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    Special = Select(driver.find_element_by_id('_supp_MENU_1'))
    Special.select_by_value('WEBS')
    time.sleep(1)

    Married = Select(driver.find_element_by_id('_supp_MENU_2'))
    Married.select_by_value("U")

    driver.find_element_by_id("_supp_TEXT_1").send_keys(name)
    time.sleep(1)

    driver.find_element_by_id("_supp_TEXT_2").send_keys(number)
    driver.find_element_by_id("_supp_TEXT_3").send_keys(number)

    Parent = Select(driver.find_element_by_id('_supp_MENU_3'))
    Parent.select_by_value("Parent")

    driver.find_element_by_id("YESNO_1_no").click()
    driver.find_element_by_id("YESNO_3_yes").click()

    driver.find_element_by_name("_eventId_continue").click()
#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)


def Santa_Monica(name,pw,email,first,last,number,ssn, street, city, zipcode):
    
    



    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
#collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('781')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
#enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('K')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
#account info
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
#education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
#military
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
#needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
#demographic
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1.5)
#submental

    Select(driver.find_element_by_id('_supp_MENU_1')).select_by_value('NULL')
    Select(driver.find_element_by_id('_supp_MENU_2')).select_by_value('Y')
    Select(driver.find_element_by_id('_supp_MENU_3')).select_by_value('N')
    Select(driver.find_element_by_id('_supp_MENU_4')).select_by_value('N/A')
    time.sleep(3)
    driver.find_element_by_id("_supp_TEXT_1").send_keys("3")
    Select(driver.find_element_by_id('_supp_MENU_5')).select_by_value('11')
    Select(driver.find_element_by_id('_supp_MENU_8')).select_by_value('NULL')
    Select(driver.find_element_by_id('_supp_MENU_9')).select_by_value('N')
    Select(driver.find_element_by_id('_supp_MENU_7')).select_by_value('3')
    Select(driver.find_element_by_id('_supp_MENU_10')).select_by_value('N')
    Select(driver.find_element_by_id('_supp_MENU_11')).select_by_value('Y')
    driver.find_element_by_id("_supp_CHECK_1").click()
    time.sleep(3)
    driver.find_element_by_name("_eventId_continue").click()
#submisson

    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 secounds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    
    
    
    
    return (name,pw,email,first,last,ssn,number)
    


def Coastline(name,pw,email,first,last,number,ssn, street, city, zipcode):
    driver = webdriver.Firefox(executable_path= geckopath)
    driver.get("https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")

    driver.find_element_by_id("portal-sign-in-link").click()
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(3)
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        

        pass

    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('233')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1.5)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
    driver.find_element_by_id("inputStreetAddress1").send_keys(street)
    driver.find_element_by_id("inputCity").send_keys(city)
    state = Select(driver.find_element_by_id('inputState'))
    state.select_by_value('CA')
    driver.find_element_by_id("inputPostalCode").send_keys(zipcode)
    driver.find_element_by_name("_eventId_continue").click()
    try:
        driver.find_element_by_id("inputHsAttendance3").click()
        
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_name("_eventId_continue").click()
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)

    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)

    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(4.5)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)

    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)



    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()

    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(4.5)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1.5)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1.5)
    driver.find_element_by_name("_eventId_continue").click()

        #found = Select(driver.find_element_by_id('_supp_MENU_1'))
        #found.select_by_value('FAM')
    time.sleep(1.5)


    driver.find_element_by_id("YESNO_1_yes").click()
    driver.find_element_by_id("YESNO_2_yes").click()
    time.sleep(1.5)
    driver.find_element_by_id("_supp_TEXT_1").send_keys(number)
    time.sleep(1)

    GPA = Select(driver.find_element_by_id('_supp_MENU_2'))
    GPA.select_by_value('4')
    time.sleep(1)

    units = Select(driver.find_element_by_id('_supp_MENU_8'))
    units.select_by_value('4')
    time.sleep(1)

    money = Select(driver.find_element_by_id('_supp_MENU_3'))
    money.select_by_value('30')
    time.sleep(1)

    house = Select(driver.find_element_by_id('_supp_MENU_4'))
    house.select_by_value('1')
    time.sleep(1)

    house = Select(driver.find_element_by_id('_supp_MENU_5'))
    house.select_by_value('B')
    time.sleep(1)

    driver.find_element_by_id("YESNO_4_yes").click()
    driver.find_element_by_id("YESNO_5_yes").click()
    time.sleep(1)
    driver.find_element_by_id("YESNO_6_yes").click()
    driver.find_element_by_id("YESNO_7_no").click()
    time.sleep(1)
    driver.find_element_by_id("YESNO_8_yes").click()
    driver.find_element_by_id("YESNO_9_no").click()
    driver.find_element_by_id("YESNO_10_no").click()
    time.sleep(1)
    driver.find_element_by_id("YESNO_11_yes").click()
    time.sleep(1)
    driver.find_element_by_id("YESNO_12_no").click()
    time.sleep(1)
    driver.find_element_by_id("YESNO_13_no").click()
    driver.find_element_by_id("YESNO_14_yes").click()

    question = Select(driver.find_element_by_id('_supp_MENU_6'))
    question.select_by_value('What school did you attend for sixth grade?')
    time.sleep(1)
    question = Select(driver.find_element_by_id('_supp_MENU_7'))
    question.select_by_value('What is the first name of your least favorite relative?')
    time.sleep(1)
    driver.find_element_by_id("_supp_TEXT_3").send_keys("Nulled")
    driver.find_element_by_id("_supp_TEXT_4").send_keys("Nulled")
    time.sleep(1)

    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(4.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(3)

    driver.find_element_by_id("inputESignature").click()
    driver.find_element_by_id("inputFinancialAidAck").click()
    print("[*] Sleeping 25 seconds!")
    time.sleep(25)
    driver.find_element_by_id("submit-application-button").click()
    time.sleep(5)
    driver.find_element_by_name("_eventId_finish").click()
    time.sleep(1)

    driver.find_element_by_id("inputEnglishSatisfied").click()
    driver.find_element_by_id("RecommendYes").click()
    driver.find_element_by_name("_eventId_submit").click()

    time.sleep(1)
    driver.quit()
    time.sleep(3)
    return (name,pw,email,first,last,ssn,number)

if platform.system() == "Windows": #checking OS
    geckopath = "./geckodriver.exe"
else:
    geckopath = "./geckodriver"


print("""""
▓█████ ▓█████▄  █    ██        ███▄ ▄███▓ ▄▄▄       ██▓ ██▓           ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█   ▀ ▒██▀ ██▌ ██  ▓██▒      ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒          ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ░██   █▌▓██  ▒██░      ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░          ▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ░▓█▄   ▌▓▓█  ░██░      ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░          ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▒░▒████▓ ▒▒█████▓       ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒      ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░ ▒▒▓  ▒ ░▒▓▒ ▒ ▒       ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░      ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░  ░ ░ ▒  ▒ ░░▒░ ░ ░       ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░        ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░    ░ ░  ░  ░░░ ░ ░       ░      ░     ░   ▒    ▒ ░  ░ ░         ░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
░  ░   ░       ░                  ░         ░  ░ ░      ░  ░      ░ ░         ░        ░  ░     ░  ░            ░ ░     ░     
        ░                                                            ░                                                           

\n

by Exploit


"""""                                                                                                             
)


accounts = int(input("How many Accounts do u want?\n"))

use_captcha = input("1. 2Captcha \n2. Manually\n")
if use_captcha == "1":
    print("2Captcha!\n")
elif use_captcha == "2":
    print("Manually!\n")
else:
    print("Wrong Input!")
    time.sleep(3)
    exit()


#collage = input("Which Collage?\n1. Sacramento (Google Drive) \n2. Coastline (Azure RDP / maybe broke)\n3. Crafton Hills \n4. San Bernardino\n5. Santa Monica\n6. Solano\n7. CCSF\n8. Canada College\n9. Santa Barbara\n10. Gavilan College\n11. Orange Coast College\n")

collages = ["Sacremento","Coastline","Crafton Hills","San Bernardino","Santa Monica","Solano Community","City College of San Francisco","Canada Collage","Santa Barbara City College","Gavilan College","Orange Coast College"]

print("Which Collage?")

for index,name in enumerate(collages): 
    print(str(index + 1) + ". " + name)

index = int(input("")) - 1

print("[*] " + collages[index])

#input()

collage = str(index + 1)

while accounts > generated:
    createaccount(collage, use_captcha)
    #Bot(collage, use_captcha)
