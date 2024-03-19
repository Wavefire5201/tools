from helium import *
from selenium.webdriver import ChromeOptions
from config import *

# Open Chrome using existing profile so Google login is saved
options = ChromeOptions()
options.add_argument(USER_DATA_DIR)
start_chrome("https://docs.google.com/forms/d/e/1FAIpQLSefs3_3DMXQYMdwcVjv6lLtsVannYa-vnNCv6TTZyOYJG212g/viewform", maximize=True, options=options)

# EMAIL, NAME, DATE
write(EMAIL, into=TextField(below="Email"))
write(NAME, into=TextField(below="Name"))
write(DATE, into=S("//html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input"))

# TIME
write(TIME_HOUR, into=S('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'))
write(TIME_MINUTE, into=S('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input'))

# LOCATION
write(LOCATION, into=TextField(below="Work Location"))

# PRACTICUM PARTNER
click(PRACTICUM_PARTNER)
click(PRACTICUM_PARTNER)

# ID NUMBER
write(ID_NUMBER, into=TextField(below="ID Number"))

# SECTION
click(S('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[1]/div[1]/span'))
click(SECTION)

# PATHWAY
click(S('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div[1]/div[1]/span'))
click(PATHWAY)

# CAMPUS
click(S('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[1]/div[1]/span'))
click(CAMPUS)

# SUBMIT
click("Submit")
print("done")