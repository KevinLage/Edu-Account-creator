import hashlib
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

generated = 0

def createaccount(collage):
    try:
        Bot(collage, use_captcha)
    except:
        createaccount(collage)


def Bot(collage,use_captcha):
    global generated
    global accounts

    
    config = open("config.txt", "r+").readlines()
    mail = config[0]
    try:
        captcha = config[1]
        captcha, gay = captcha.split("\n")
    except:
        pass
    namesss = open('FakeNameGenerator.csv').read().splitlines()

    myline = random.choice(namesss)
    first, last, number, ssn = myline.split(",")


    def randomName(size=10, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for i in range(size))


    def randomPassword(size=14, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for i in range(size))


    driver = webdriver.Firefox(executable_path= "./geckodriver")

    driver.get("https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s2")

    lines = open('FakeNameGenerator.csv').read().splitlines()

    myline = random.choice(lines)
    first, last, number, ssn = myline.split(",")


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



    email = randomPassword() + mail
    driver.find_element_by_id("inputEmail").send_keys(email)
    driver.find_element_by_id("inputEmailConfirm").send_keys(email)
    time.sleep(4)
    driver.find_element_by_id("inputSmsPhone").send_keys(number)
    driver.find_element_by_id("inputHomeless").click()
    driver.find_element_by_id("homeless-confirm-yes").click()
    driver.find_element_by_id("homelessConfirmationDialog-modal-ok-button").click()
    driver.find_element_by_id("accountFormSubmit").click()

    print("[*] Page 2/3 Done!")




    pw = randomPassword() + "1"
    name = randomName()



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



        lol, moin = r.text.split("|")
        time.sleep(20)

        url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
        r = requests.get(url2)
        while "CAPCHA_NOT_READY" in r.text:

            url2 = "https://2captcha.com/res.php?key=" +captcha + "&action=get&id=" + moin
            r = requests.get(url2)
            print("[*] Waiting for 2Captcha")
            time.sleep(3)

        ok, key = r.text.split("|")

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
        Coastline(name, pw, number, email)
    elif collage == "2":
        Coastline(name,pw,number,email)
    elif collage == "3":
        Crafton(name,pw,number,email)
    elif collage == "4":
        San_Bernardino(name,pw,number,email)
    elif collage == "5":
        Santa_Monica(name,pw,number,email)
    elif collage == "6":
        Solano(name,pw,number,email)
    elif collage == "7":
        ccsf(name,pw,number,email)
    else:
        print("Fuck")
        exit()


def Solano(name,pw,number,email):
    global generated
    global accounts

    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")

def ccsf(name,pw,number,email):
    global generated
    global accounts

    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    Select(driver.find_element_by_id("_supp_MENU_1")).select_by_value('ENG')
    time.sleep(2)
    Select(driver.find_element_by_id("_supp_MENU_4")).select_by_value('OPT1')
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")





def San_Bernardino(name,pw,number,email):
    global generated
    global accounts

    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")



def Crafton(name,pw,number,email):
    global generated
    global accounts

    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    time.sleep(39000)
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")

def San_Bernardino(name,pw,number,email):
    global generated
    global accounts

    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")


def Santa_Monica(name,pw,number,email):
    global generated
    global accounts



    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)
    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write("  Email:" + email)
        file.write("\n")



def Coastline(name,pw,number,email):
    global generated
    global accounts



    driver = webdriver.Firefox(executable_path= "./geckodriver")
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
    time.sleep(4838)
    collage.select_by_value('233')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
    driver.find_elements_by_tag_name("option")[1].click()
    driver.find_elements_by_tag_name("option")[3].click()
    time.sleep(1)

    time.sleep(1.5)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
    driver.find_element_by_id("inputHomelessNoMailingAddress").click()
    time.sleep(1)

    driver.find_element_by_id("homelessNoCurrentMailingAddress-confirm-yes").click()
    driver.find_element_by_id("homelessNoCurrentMailingAddressConfirmationDialog-modal-ok-button").click()
    time.sleep(0.5)
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
    driver.find_element_by_id("inputAthleticInterest1").click()
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
    generated += 1
    print(generated , "/" , accounts , " Accounts are done!")
    with open("accountsb.txt", "a+") as file:
        file.write(name + ":" + pw)
        file.write(" Email:" + email)
        file.write("\n")

url = "https://pastebin.com/raw/833mvJDa"
r = requests.get(url)
if r.text == "1":
    print("Update the tool!")
    time.sleep(3)
    exit()
else:
	pass


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

use_captcha = input("[1]2Captcha \n[2]Manually\n")
if use_captcha == "1":
    print("2Captcha!\n")
elif use_captcha == "2":
    print("Manually!\n")
else:
    print("Wrong Input!")
    time.sleep(3)
    exit()
collage = input("Which Collage?\n1. Sacramento (Google Drive) \n2. Coastline (Azure RDP / maybe broke)\n3. Crafton Hills (RDP)\n4. San Bernardino\n5. Santa Monica\n6. Solano\n7. CCSF\n\n")

if collage == "1":
    print("[*] Sacremento")
elif collage == "2":
    print("[*] Coastline")
elif collage == "3":
    print("[*] Crafton Hills")
elif collage == "4":
    print("[*] San Bernardino")
elif collage == "5":
    print("[*] Santa Monica")
elif collage == "6":
    print("[*] Solano Community")
elif collage == "7":
    print("[*] City College of San Francisco ")
else:
    print("Wrong input")
    time.sleep(3)
    exit()


while accounts > generated:
    createaccount(collage)