#Backend 
from nordvpn_switcher import initialize_VPN,rotate_VPN
import time
import time
from Twitter_Signup import signup
from Highlevelhelper import *
from Twitterlogin import *
from databseoperations import *
email_listed=[
    {'email':'twittertesting165@gmail.com','password':'twitQKrSAtidsqnssg494'},
    {'email':'hamahama@gmail.com','password':'sdqdsqdsq'}
]
'''
instructions = initialize_VPN(area_input=['France']) # <-- Be aware: the area_input parameter expects a list, not a string

def Create_n_account(emails):
    accounts_to_create = email_to_account(emails)
    

    i=0
    for account in accounts_to_create:
        #temporary to test one
        if i < 2 :
            if i%5==0:
                rotate_VPN(instructions)
                time.sleep(3)
            try:
                signup(account["originalmail"],account["password"],account["email"])
            except:
                print("Could not create account")
            i=i+1

    # for i in 1->5 signup + create into database
    return 0
    '''
def like_high_level(link):
    all_accounts=database_read_accounts()
    for account in all_accounts:
        #add nord
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        post_like(driver,link)
        driver.quit()
    #driver = high_level_login()
def Comment_high_level(link,Comment_value):
    all_accounts=database_read_accounts()
    for account in all_accounts:
        #add nord
        driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
        print("Done Connecting ..")
        comment_post(driver,link,Comment_value)
        driver.quit()
    #driver = high_level_login()

def get_followers_high_level(max,user_id):
    all_accounts=database_read_accounts()
    #TODO specific account
    account = random.choice(all_accounts)
        #add nord
    driver = high_level_login(account["Email"],account["Password"],account["username"],account["OriginalMail"],account["Password"])
    print("Done Connecting ..")
    get_followers(driver,user_id)
    follower_links = find_n_followers(driver,max).keys()
    i=0
    for linked in follower_links:
        if i<max:
        #to add database
            follower_template = {"link": linked}
            database_write_follower(follower_template)
            i=i+1
    print("Read followers from databse :")
    print(database_read_followers())
    print("New Length :",len(database_read_followers()))
    driver.quit()
def follow_high_level():
    return 0
def change_bio_high_level():
    return 0
def check_dmable_high_level():
    return 0
def dm_high_level(message,n):
    #Segment to accounts
    return 0


#rotate_VPN(instructions)
Profile_id="elonmusk"
post_link="https://twitter.com/elonmusk/status/1642026231766953985"
message = "Based"
get_followers_high_level(100,Profile_id)
#Comment(post_link,message)
#like(link)
#Create_n_account(email_listed)

#At each step save to database

#Frontend
#Show Scraped Followers
#Show Created Accounts
#Create Accounts Form
#Get Followers Form
#Check Dmable Form
# Dm form
# Follow Form
# List + form