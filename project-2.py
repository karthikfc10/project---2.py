import selenium
from selenium import webdriver
import time
import data
import Xpath


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome(executable_path="C:/chromedriver_win32 (1).zip/chromedriver.exe")

driver.implicitly_wait(50)
driver.maximize_window()

#To navigate the url

driver.get(data.url)
driver.implicitly_wait(30)

#To set a reset password
#forget password
driver.find_element(By.XPATH,Xpath.forgetpassword).click()
time.sleep(5)
#username
driver.find_element(By.XPATH,Xpath.user).send_keys(data.username)
time.sleep(5)
#resetpassword
driver.find_element(By.XPATH,Xpath.resetpassword).click()
time.sleep(5)

driver.get(data.url)
driver.implicitly_wait(30)

time.sleep(5)


#Test case 1
#forget password link validation on login page

driver.find_element(By.NAME,Xpath.username).send_keys(data.username)
time.sleep(5)

driver.find_element(By.NAME,Xpath.password).send_keys(data.password)
time.sleep(5)
driver.find_element(By.XPATH,Xpath.login).click()
time.sleep(5)

#Test cases 2
#Header validation on admin page

driver.find_element(By.XPATH,Xpath.Instruction).click()
time.sleep(5)


#usermanagement verification

UserManagement = driver.find_element(By.XPATH,Xpath.UserManagement).text
print(UserManagement)
read_text = "User Management"

assert read_text in UserManagement

print("UserManagement verified")

#Job verification

Job = driver.find_element(By.XPATH,Xpath.Job).text
print(Job)
read_text = "Job"

assert read_text in Job

print("Job verified")

#Organization verification

Organization = driver.find_element(By.XPATH,Xpath.Organization).text
print(Organization)
read_text = "Organization"

assert read_text in Organization

print("Organization verified")

#Qualifications verification

Qualifications = driver.find_element(By.XPATH,Xpath.Qualifications).text
print(Qualifications)
read_text = "Qualifications"

assert read_text in Qualifications

print("Qualifications verified")

#Nationalities verification

Nationalities = driver.find_element(By.XPATH,Xpath.Nationalities).text
print(Nationalities)
read_text = "Nationalities"

assert read_text in Nationalities

print("Nationalities verified")

#corporateBranding verification

CorporateBranding = driver.find_element(By.XPATH,Xpath.CorporateBranding).text
print(CorporateBranding)
read_text = "Corporate Branding"

assert read_text in CorporateBranding

print("CorporateBranding verified")

#configuration verification

Configuration = driver.find_element(By.XPATH,Xpath.Configuration).text
print(Configuration)
read_text = "Configuration"

assert read_text in Configuration

print("Configuration verified")

time.sleep(5)

#Test case 3
#Main menu validation on Admin page

#Admin verification

Admin = driver.find_element(By.XPATH,Xpath.Admin).text
print(Admin)

read_text = "Admin"

assert read_text in Admin

print("Admin verified")

#Pim verification

PIM = driver.find_element(By.XPATH,Xpath.PIM).text
print(PIM)

read_text = "PIM"

assert read_text in PIM

print("PIM verified")

#leave verification

Leave = driver.find_element(By.XPATH,Xpath.Leave).text
print(Leave)

read_text = "Leave"

assert read_text in Leave

print("Leave verified")

#Time verification

Time = driver.find_element(By.XPATH,Xpath.Time).text
print(Time)

read_text = "Time"

assert read_text in Time

print("Time verified")

#Recruitment verification

Recruitment = driver.find_element(By.XPATH,Xpath.Recruitment).text
print(Recruitment)

read_text = "Recruitment"

assert read_text in Recruitment

print("Recruitment verified")

#Myinfo verification

MyInfo = driver.find_element(By.XPATH,Xpath.MyInfo).text
print(MyInfo)

read_text = "My Info"

assert read_text in MyInfo

print("My Info verified")

#performance verification

Performance = driver.find_element(By.XPATH,Xpath.Performance).text
print(Performance)

read_text = "Performance"

assert read_text in Performance

print("Performance verified")

#Dashboard verification

Dashboard = driver.find_element(By.XPATH,Xpath.Dashboard).text
print(Dashboard)

read_text = "Dashboard"

assert read_text in Dashboard

print("Dashboard verified")

#Directory verification

Directory = driver.find_element(By.XPATH,Xpath.Directory).text
print(Directory)

read_text = "Directory"

assert read_text in Directory

print("Directory verified")

#Maintenance verification

Maintenance = driver.find_element(By.XPATH,Xpath.Maintenance).text
print(Maintenance)

read_text = "Maintenance"

assert read_text in Maintenance

print("Maintanance verified")

#Buzz verification

Buzz = driver.find_element(By.XPATH,Xpath.Buzz).text
print(Buzz)

read_text = "Buzz"

assert read_text in Buzz

print("Buzz verified")


driver.close()
driver.quit()
print("test completed")
