import orm_sqlite 


def database_write_account(account):
    account['VerifiPhone']=0
    pomodoro = Account(account)
    pomodoro.save()

def database_read_accounts():
    return Account.objects.all()

class Account(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    Email = orm_sqlite.StringField()
    Password = orm_sqlite.StringField()
    username = orm_sqlite.StringField()
    OriginalMail = orm_sqlite.StringField()
    VerifiPhone = orm_sqlite.IntegerField()

def delete_by_id(id):
    Account.objects.get(pk=id).delete()
def update_email_by_id(id, email):
    obj = Account.objects.get(pk=id)
    obj['Email'] = email
    obj.update()
db = orm_sqlite.Database('UserInfo.db')
Account.objects.backend = db
import orm_sqlite 


def database_write_follower(follower):
    follower['checked_dmable']=0
    follower['dmable']=0
    follower['already_dmed']=0
    pomodoro = Follower(follower)
    pomodoro.save()

def database_read_followers():
    return Follower.objects.all()

class Follower(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    link = orm_sqlite.StringField()
    checked_dmable = orm_sqlite.IntegerField()
    dmable = orm_sqlite.IntegerField()
    already_dmed=orm_sqlite.IntegerField()

def delete_by_id(id):
    Follower.objects.get(pk=id).delete()
'''def update_email_by_id(id, dmable):
    obj = Follower.objects.get(pk=id)
    obj['Email'] = email
    obj.update()'''
def check_link_id(link):
    all_followers = database_read_followers()
    for follower in all_followers:
        if follower["link"] == link:
            return follower["id"]
def checked_and_dmable(link):
    link_id =check_link_id(link)
    obj = Follower.objects.get(pk=link_id)
    obj['checked_dmable'] = 1
    obj['dmable'] = 1
    obj.update()
def checked_and_not_dmable(link):
    link_id =check_link_id(link)
    obj = Follower.objects.get(pk=link_id)
    obj['checked_dmable'] = 1
    obj['dmable'] = 0
    obj.update()
def get_all_dmable_and_not_dmed():
    dmable_list=[]
    all_followers=database_read_followers()
    for follower in all_followers:
        if follower["dmable"] == 1 and follower["already_dmed"] == 0:
            dmable_list.append(follower)
    return dmable_list
def get_all_dmable():
    dmable_list=[]
    all_followers=database_read_followers()
    for follower in all_followers:
        if follower["dmable"] == 1 :
            dmable_list.append(follower)
    return dmable_list
db2 = orm_sqlite.Database('Follwer.db')
Follower.objects.backend = db2
'''
database_write_follower(follower_template)
print(database_read_followers())'''



