# -*- coding: UTF-8 -*-
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
        self.html = requests.get("https://www.fakenamegenerator.com/", headers={
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}).text
        self.name = {"completename": self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0], "first": self.html.split('<div class="address">')[
            1].split('<h3>')[1].split('</h3>')[0].split(" ")[0], "last": self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[-1]}

        addy = self.html.split('<div class="adr">')[1].split("                                        ")[
            1].split("                                        </div>")[0]
        addynum = addy.split(" ")[0]
        streetlist = self.html.split('<div class="adr">')[1].split("                                        ")[
            1].split("                                        </div>")[0].split("<br />")[:1][0].split(" ")[1:]
        street = ""

        province = addy.split('<br />')[1].split(",")[0]
        ZIP = addy.split(", ")[1].split('   ')[0]
        for i in streetlist:
            street = street + " " + i
        self.addy = {"addynum": addynum,
                     "street": street[1:], "province": province, "zip": ZIP}

        self.SSN = self.html.split(
            'tal"><dt>SSN</dt><dd>')[1].split(' <div class="adtl">')[0]
        self.phone = self.html.split(
            "<dt>Phone</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.phoneprefix = "+" + \
            self.html.split(
                "<dt>Country code</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        birthday = "+" + \
            self.html.split(
                "<dt>Birthday</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        Month = birthday.split(" ")[0].replace("+", "")
        Day = birthday.split(" ")[1].replace(",", "")
        Year = birthday.split(" ")[-1]
        self.birthday = {"Day": Day, "Month": Month, "Year": Year}
        self.age = self.html.split(
            "<dt>Age</dt>")[1].split(" years old</dd>")[0].split("<dd>")[1]
        self.tropicalzodiac = self.html.split(
            "<dt>Tropical zodiac</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.email = self.html.split(
            '<dt>Email Address</dt>')[1].split('<dd>')[1].split('        ')[0]
        self.username = self.html.split(
            "<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.password = self.html.split(
            "<dt>Password</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.website = self.html.split(
            "<dt>Website</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.useragent = self.html.split(
            "<dt>Browser user agent</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.cardtype = self.html.split(
            '<h3 class="hh3">Finance</h3>')[1].split('<dt>')[1].split('</dt>')[0]
        self.exp = self.html.split(
            "<dt>Expires</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        try:
            self.CVC = self.html.split(
                "<dt>CVC2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        except:
            self.CVC = self.html.split(
                "<dt>CVV2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.company = self.html.split(
            "<dt>Company</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.job = self.html.split(
            "<dt>Occupation</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.height = self.html.split(
            "<dt>Height</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.weight = self.html.split(
            "<dt>Weight</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.bloodtype = self.html.split(
            "<dt>Blood type</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.UPSTrackingnum = self.html.split(
            "<dt>UPS tracking number</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.MoneyGram = self.html.split(
            "<dt>MoneyGram MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.WesternUnion = self.html.split(
            "<dt>Western Union MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.favcolor = self.html.split(
            "<dt>Favorite color</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.car = self.html.split(
            "<dt>Vehicle</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.GUID = self.html.split(
            "<dt>GUID</dt>")[1].split("</dd>")[0].split("<dd>")[1]


generated = 0


def createaccount(collage, use_captcha):
    try:
        Bot(collage, use_captcha)
    except Exception as E:
        open("log.txt", "a+").write(str(E)+"\n")
        print(E)


def randomSSN(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for i in range(size))


def Bot(collage, use_captcha):

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

    driver.get(
        "https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s2")

    datafake = FakeNameGenerator()
    datafake.GenerateIdenity()

    first = datafake.name["first"]
    last = datafake.name["last"]
    number = datafake.phone
    ssn = str(str(datafake.SSN) + str(randomSSN())).replace("X", "")
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

    register_button = driver.find_element_by_id("accountFormSubmit")
    register_button.click()

    # Page 1

    first_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    first_name.send_keys(first)

    no_middle_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "inputHasNoMiddleName"))
    )
    no_middle_name.click()

    last_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputLastName"))
    )
    last_name.send_keys(last)

    prev_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "hasOtherNameNo"))
    )
    prev_name.click()

    preffered_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "hasPreferredNameNo"))
    )
    preffered_name.click()

    month_one = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateMonth option[value="3"]'))
    )
    month_one.click()

    day_one = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateDay option[value="7"]'))
    )
    day_one.click()

    year_one = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))
    )
    year_one.send_keys("1994")

    month_two = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateMonthConfirm option[value="3"]'))
    )
    month_two.click()

    day_two = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateDayConfirm option[value="7"]'))
    )
    day_two.click()

    year_two = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))
    )
    year_two.send_keys("1994")

    select_ssn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, '-have-ssn-yes'))
    )
    select_ssn.click()

    input_ssn = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, '-ssn-input1'))
    )
    input_ssn.send_keys(ssnlol)

    input_ssn_confirm = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, '-ssn-input2'))
    )
    input_ssn_confirm.send_keys(ssnlol)

    page_one_submit = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'accountFormSubmit'))
    )
    page_one_submit.click()

    print("\n\n[*] Page 1/3 Done!")

    # Page 2

    input_email = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmail'))
    )
    input_email.send_keys(email)

    input_emailconfirm = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))
    )
    input_emailconfirm.send_keys(email)

    input_phone = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSmsPhone'))
    )
    input_phone.send_keys(number)

    input_street = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))
    )
    input_street.send_keys(street)

    input_city = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputCity'))
    )
    input_city.send_keys(city)

    input_state = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputState option[value="CA"]'))
    )
    input_state.click()

    input_zipcode = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPostalCode'))
    )
    input_zipcode.send_keys(zipcode)

    page_two_submit = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'accountFormSubmit'))
    )
    page_two_submit.click()

    try:
        driver.find_element_by_id("inputUserId").send_keys(name)
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_id("accountFormSubmit").click()

    print("\n\n[*] Page 2/3 Done!")

    # Page 3

    input_userid = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputUserId'))
    )
    input_userid.send_keys(name)

    input_pass = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswd'))
    )
    input_pass.send_keys(pw)

    input_passconf = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))
    )
    input_passconf.send_keys(pw)

    input_pin = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPin'))
    )
    input_pin.send_keys("0420")

    input_pinconf = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPinConfirm'))
    )
    input_pinconf.send_keys("0420")

    input_security1 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion1 option[value="10"]'))
    )
    input_security1.click()
    input_answer1 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))
    )
    input_answer1.send_keys("12")

    input_security2 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion2 option[value="4"]'))
    )
    input_security2.click()
    input_answer2 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))
    )
    input_answer2.send_keys("Josh")

    input_security3 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion3 option[value="2"]'))
    )
    input_security3.click()
    input_answer3 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))
    )
    input_answer3.send_keys("Tesla 3")

    print("\n\n[*] Bypassing the Captcha!\n\n")

    if use_captcha == "1":

        url = "https://2captcha.com/in.php?key=" + captcha + \
            "&method=userrecaptcha&json=0&googlekey=6LeaXhITAAAAACiHR6YSn1YKAUrrTZTLtjxuwYx6&pageurl=https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s4"

        r = requests.get(url)

        _, moin = r.text.split("|")
        time.sleep(20)

        url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
        r = requests.get(url2)
        while "CAPCHA_NOT_READY" in r.text:

            url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
            r = requests.get(url2)
            print("[*] Waiting for 2Captcha\n\n")
            time.sleep(3)
        try:
            _, key = r.text.split("|")
        except:
            print(r.text)

        command = 'document.getElementById("g-recaptcha-response").innerHTML="' + \
            key + '";'
        driver.execute_script(
            "document.getElementsByName('captchaResponse')[0].setAttribute('type', 'shown');")
        driver.find_element_by_name("captchaResponse").send_keys(key)
        time.sleep(5)
        driver.execute_script(command)
    elif use_captcha == "2":
        print("Solve the captcha now!\n\n")
        try:
            element = driver.find_element_by_id("accountFormSubmit")
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            print("Failed to scroll")
        captcha_solved = "1"
        while captcha_solved == "1":
            captcha_solved = input("[Y]Solved?\n")
    else:
        print("Error")

    time.sleep(2)
    driver.find_element_by_id("accountFormSubmit").click()
    time.sleep(2)

    print("\n\n[*] Page 3/3 Done!")

    driver.quit()

    with open("openccc.txt", "a+") as file:
        file.write("Username: " + name + ", Password: " + pw + ", Email: " + email + ", First: " + first + ", Last: " + last + ", Number: " +
                   number + ", SSN: " + ssn + ", Street Address: " + street + ", City: " + city + ", Zipcode: " + zipcode + ", College: " + collage)
        file.write("\n\n")

    print("\n\nYour openccc account has been created and is stored in openccc.txt and we will start filling college application now.\n\n")

    onlyCollege(name, pw, email, first, last, number,
                ssn, street, city, zipcode, collage)


def onlyCollege(name, pw, email, first, last, number, ssn, street, city, zipcode, collage):
    if collage == "1":
        resp = Coastline(name, pw, email, first, last,
                         number, ssn, street, city, zipcode)
    elif collage == "2":
        resp = Coastline(name, pw, email, first, last,
                         number, ssn, street, city, zipcode)
    elif collage == "3":
        resp = Crafton(name, pw, email, first, last,
                       number, ssn, street, city, zipcode)
    elif collage == "4":
        resp = San_Bernardino(name, pw, email, first, last,
                              number, ssn, street, city, zipcode)
    elif collage == "5":
        resp = Santa_Monica(name, pw, email, first, last,
                            number, ssn, street, city, zipcode)
    elif collage == "6":
        resp = Solano(name, pw, email, first, last,
                      number, ssn, street, city, zipcode)
    elif collage == "7":
        resp = ccsf(name, pw, email, first, last,
                    number, ssn, street, city, zipcode)
    elif collage == "8":
        resp = Canada(name, pw, email, first, last,
                      number, ssn, street, city, zipcode)
    elif collage == "9":
        resp = barbara(name, pw, email, first, last,
                       number, ssn, street, city, zipcode)
    elif collage == "10":
        resp = gavilan(name, pw, email, first, last,
                       number, ssn, street, city, zipcode)
    elif collage == "11":
        resp = orange(name, pw, email, first, last,
                      number, ssn, street, city, zipcode)
    else:
        print("Fuck")
        exit()

    global generated
    generated += 1
    with open("eduaccounts.txt", "a+") as file:
        file.write("Username: " + resp[0] + ", Password: " + resp[1] + ",  Email:" + resp[2] + ", First Name: " +
                   resp[3] + ", Last Name: " + resp[4] + ", SSN: " + resp[5] + ", Number: " + resp[6])
        file.write("\n\n")
    print("\n\nSuccessfully created ", generated,
          " student account(s), Please check eduaccounts.txt file for details. Wait a few days for college to accept your application, check your temp mail once in while.\n\n")


def orange(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('833')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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


# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographic page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# supplemental
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "_supp_TEXT_1"))
        )
    except:
        print("Unable to open supplemental page, restarting bot.")
        pass
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


# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submission page, restarting bot.")
        pass
    time.sleep(0.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(1)

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
    time.sleep(1)

    return (name, pw, email, first, last, ssn, number)


def gavilan(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('441')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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


# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographic page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)
# supplemental
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "_supp_TEXT_1"))
        )
    except:
        print("Unable to open supplemental page, restarting bot.")
        pass
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

# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submisson page, restarting bot.")
        pass
    time.sleep(0.5)
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(1)

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

    return (name, pw, email, first, last, ssn, number)


def barbara(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    time.sleep(1)
    collage.select_by_value('651')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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
# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographic page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)
# supplemental
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "_supp_MENU_1"))
        )
    except:
        print("Unable to open supplemental page, restarting bot.")
        pass
    supp1 = Select(driver.find_element_by_id('_supp_MENU_1'))
    supp1.select_by_value('15')

    supp2 = Select(driver.find_element_by_id('_supp_MENU_2'))
    supp2.select_by_value('01')
    time.sleep(1)

    supp3 = Select(driver.find_element_by_id('_supp_MENU_3'))
    supp3.select_by_value('7')
    time.sleep(1)
    supp5 = Select(driver.find_element_by_id('_supp_MENU_5'))
    supp5.select_by_value('Y')

    supp4 = Select(driver.find_element_by_id('_supp_MENU_4'))
    supp4.select_by_value('N')

    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)

# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submission page, restarting bot.")
        pass
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(1)

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

    return (name, pw, email, first, last, ssn, number)


def Canada(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass
# collage auswahl

    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('371')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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
# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest3").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographic page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)

# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submission page, restarting bot.")
        pass
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(1)

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

    return (name, pw, email, first, last, ssn, number)


def Solano(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)
        pass

# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('281')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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
# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographic page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)
# submental
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "_supp_CHECK_1"))
        )
    except:
        print("Unable to open submental page, restarting bot.")
        pass
    driver.find_element_by_id("_supp_CHECK_1").click()
    driver.find_element_by_name("_eventId_continue").click()
# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submission page, restarting bot.")
        pass
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

    return (name, pw, email, first, last, ssn, number)


def ccsf(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputJUsername"))
        )
    except:
        print("Unable to open signin page, restarting bot.")
        pass
    driver.find_element_by_id("inputJUsername").send_keys(name)
    time.sleep(1)
    driver.find_element_by_id("inputJPassword").send_keys(pw)
    driver.find_element_by_name("_eventId_proceed").click()
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "beginApplicationButton"))
        )
    except:
        print("Unable to login, restarting bot.")
        pass
    try:
        driver.find_elements_by_css_selector(".btn-primary")[3].click()
        time.sleep(1)

        driver.find_element_by_id("delete-confirmation-ok-button").click()
        time.sleep(4.5)
    except:
        time.sleep(3)

        pass
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('361')
    driver.find_element_by_id("beginApplicationButton").click()
# enrollment
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEduGoal"))
        )
    except:
        print("Unable to open enrollment page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
# account info
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputStreetAddress1"))
        )
    except:
        print("Unable to open account info page, restarting bot.")
        pass
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
# education
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputHsAttendance3"))
        )
    except:
        print("Unable to open education page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputMilitaryStatus"))
        )
    except:
        print("Unable to open military page, restarting bot.")
        pass
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    s2 = Select(driver.find_element_by_id('inputMilitaryStatus'))
    s2.select_by_value('1')
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    driver.find_element_by_id("inputCaRes2YearsYes").click()
    driver.find_element_by_id("inputIsEverInFosterCareNo").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# needs
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputEnglishYes"))
        )
    except:
        print("Unable to open needs page, restarting bot.")
        pass
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputGender"))
        )
    except:
        print("Unable to open demographics page, restarting bot.")
        pass
    gender = Select(driver.find_element_by_id('inputGender'))
    gender.select_by_value('Male')
    time.sleep(1)

    trans = Select(driver.find_element_by_id('inputTransgender'))
    trans.select_by_value('No')
    time.sleep(1)
    sexual = Select(driver.find_element_by_id('inputOrientation'))
    sexual.select_by_value('StraightHetrosexual')

    guard = Select(driver.find_element_by_id('inputParentGuardianEdu1'))
    guard.select_by_value('3')
    time.sleep(1)
    guard2 = Select(driver.find_element_by_id('inputParentGuardianEdu2'))
    guard2.select_by_value('Y')

    driver.find_element_by_id("inputHispanicNo").click()

    driver.find_element_by_id("inputRaceEthnicity800").click()
    time.sleep(1)
    driver.find_element_by_id("inputRaceEthnicity806").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(1)
# submental
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "_supp_MENU_1"))
        )
    except:
        print("Unable to open submental page, restarting bot.")
        pass
    Select(driver.find_element_by_id("_supp_MENU_1")).select_by_value('ENG')
    time.sleep(1)
    Select(driver.find_element_by_id("_supp_MENU_5")).select_by_value('N')
    Select(driver.find_element_by_id("_supp_MENU_6")).select_by_value('N')
    Select(driver.find_element_by_id("_supp_MENU_4")).select_by_value('OPT2')
    driver.find_element_by_id("_supp_CHECK_5").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()

# submisson
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "inputConsentYes"))
        )
    except:
        print("Unable to open submission page, restarting bot.")
        pass
    driver.find_element_by_id("inputConsentYes").click()
    time.sleep(1)

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

    return (name, pw, email, first, last, ssn, number)


def San_Bernardino(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
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
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('982')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
# enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('K')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
# account info
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
# education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
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
# needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
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
# submental

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

    radio1 = driver.find_element_by_id("YESNO_1_no")
    driver.execute_script(
        "arguments[0].checked = true;", radio1)

    radio2 = driver.find_element_by_id("YESNO_3_yes")
    driver.execute_script(
        "arguments[0].checked = true;", radio2)

    driver.find_element_by_name("_eventId_continue").click()
# submisson

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

    return (name, pw, email, first, last, ssn, number)


def Crafton(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
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
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('981')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
# enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(0.5)
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('F')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
# account info
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
# education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
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
# needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
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
# submental

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

    radio1 = driver.find_element_by_id("YESNO_1_no")
    driver.execute_script(
        "arguments[0].checked = true;", radio1)

    radio2 = driver.find_element_by_id("YESNO_2_no")
    driver.execute_script(
        "arguments[0].checked = true;", radio2)

    driver.find_element_by_name("_eventId_continue").click()
# submisson

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

    return (name, pw, email, first, last, ssn, number)


def Santa_Monica(name, pw, email, first, last, number, ssn, street, city, zipcode):

    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")
    time.sleep(1)
    driver.find_element_by_id("loginTab").click()
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
# collage auswahl
    collage = Select(driver.find_element_by_id('inputCollegeId'))
    collage.select_by_value('781')
    driver.find_element_by_id("beginApplicationButton").click()
    time.sleep(4)
# enrollment
    driver.find_elements_by_tag_name("option")[1].click()
    collage = Select(driver.find_element_by_id('inputEduGoal'))
    collage.select_by_value('K')
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[25].click()
    driver.find_element_by_name("_eventId_continue").click()
    time.sleep(2)
# account info
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
# education
    driver.find_elements_by_tag_name("option")[1].click()
    time.sleep(1)
    driver.find_elements_by_tag_name("option")[9].click()
    driver.find_element_by_id("inputHsAttendance3").click()
    driver.find_element_by_name("_eventId_continue").click()
# military
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
# needs
    driver.find_element_by_id("inputEnglishYes").click()
    driver.find_element_by_id("inputFinAidInfoNo").click()
    time.sleep(1)
    driver.find_element_by_id("inputAssistanceNo").click()
    driver.find_element_by_id("inputAthleticInterest1").click()
    time.sleep(1)
    driver.find_element_by_name("_eventId_continue").click()
# demographic
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
# submental

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
# submisson

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

    return (name, pw, email, first, last, ssn, number)


def Coastline(name, pw, email, first, last, number, ssn, street, city, zipcode):
    driver = webdriver.Firefox(executable_path=geckopath)
    driver.get(
        "https://www.opencccapply.net/uPortal/f/u63l1s1000/normal/render.uP")

    driver.find_element_by_id("loginTab").click()
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
    # found.select_by_value('FAM')
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
    question.select_by_value(
        'What is the first name of your least favorite relative?')
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
    return (name, pw, email, first, last, ssn, number)


if platform.system() == "Windows":  # checking OS
    geckopath = "./geckodriver.exe"
else:
    geckopath = "./geckodriver"


print("""

EDU Account Creator

by Exploit forked and fixed by pixelcookie11\n"""
      )


accounts = int(input("How many Accounts do you want?\n"))

use_captcha = input("\nWhich captcha service do you want to use?\n1. 2Captcha (Needs API Key) \n2. None (Manual)\n")
if use_captcha == "1":
    print("2Captcha!\n")
elif use_captcha == "2":
    print("Manually!\n")
else:
    print("Wrong Input!")
    time.sleep(3)
    exit()


#collage = input("Which Collage?\n1. Sacramento (Google Drive) \n2. Coastline (Azure RDP / maybe broke)\n3. Crafton Hills \n4. San Bernardino\n5. Santa Monica\n6. Solano\n7. CCSF\n8. Canada College\n9. Santa Barbara\n10. Gavilan College\n11. Orange Coast College\n")

collages = ["Sacremento", "Coastline", "Crafton Hills", "San Bernardino", "Santa Monica", "Solano Community",
            "City College of San Francisco", "Canada Collage", "Santa Barbara City College", "Gavilan College", "Orange Coast College"]

print("Which Collage?")

for index, name in enumerate(collages):
    print(str(index + 1) + ". " + name)

index = int(input("")) - 1

print("[*] " + collages[index])

collage = str(index + 1)

# In future to enable posibility of creating edu accounts without creating openccc
# if(accounts == 1):
#     showChoice = True
#     while showChoice:
#         createOpenccc = input(
#             "\nDo you want to create an openccc account? [Y/N]\n")
#         if createOpenccc == "n" or createOpenccc == "N":
#             showChoice = False
#             name = input("\nPlease enter username:\n")
#             pw = input("\nPlease enter password:\n")
#             email = input("\nPlease enter email:\n")
#             first = input("\nPlease enter first name:\n")
#             last = input("\nPlease enter last name:\n")
#             number = input("\nPlease enter number:\n")
#             ssn = input("\nPlease enter ssn:\n")
#             street = input("\nPlease enter street address:\n")
#             city = input("\nPlease enter city:\n")
#             zipcode = input("\nPlease enter zipcode:\n")
#             time.sleep(1)
#             print("\n\nAll done! Please wait while we create your account.\n\n")
#             time.sleep(1)
#             try:
#                 onlyCollege(name, pw, email, first, last, number,
#                             ssn, street, city, zipcode, collage)
#             except:
#                 onlyCollege(name, pw, email, first, last, number,
#                             ssn, street, city, zipcode, collage)
#         elif createOpenccc == "y" or createOpenccc == "Y":
#             showChoice = False
#             createaccount(collage, use_captcha)
#         else:
#             print("\n\nPlease eneter 'y' for yes or 'n' for no.\n\n")


while accounts > generated:
    createaccount(collage, use_captcha)
    #Bot(collage, use_captcha)
