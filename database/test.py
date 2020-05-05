import csv
from faker import Faker
fake=Faker()
FGender=['Male','Female']

#populating populating Users 
with open('mycsv.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','FirstName','LastName','Gender','Password'])
     for i in range(1,500000):
        
        thewriter.writerow([fake.random_int(min=1, max=500000),fake.first_name(),fake.last_name(),fake.random.choice(FGender),fake.password(length=10)])

#populating table profiles
FRelationshipStatus=['Single','Married']
with open('mycsv1.csv','w',newline='') as f:
         thewriter = csv.writer(f)
         thewriter.writerow(['ProfileId','Username','Bio','RelationshipStatus'])
         for i in range (1,500000):
            thewriter.writerow([fake.random_int(min=1, max=500000),fake.bothify(text='User???##'),fake.sentence(nb_words=6, variable_nb_words=False, ext_word_list=None),fake.random.choice(FRelationshipStatus)])


# populating table User_profile
with open('mycsv2.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','ProfileId'])
     for i in range (1,500000):
        thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000)])

# populating table User_email
with open('mycsv3.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','Email'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.email()])

# populating table profile_phonenumber
with open('mycsv4.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['ProfileId','PhoneNumber'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.phone_number()])
     
#populating table profile_address 
with open('mycsv5.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['ProfileId','AddressId','Street','City'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.street_name(),fake.city()])
 
#populating table photo
with open('mycsv6.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['PhotoId','Images','Photoname'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.file_name(category='image', extension='jpg'),fake.word()])

#populating table User_photo
with open('mycsv7.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','PhotoId','DateUP'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.date_between(start_date='-10y', end_date='today')])

#populating table Post
FPostType=['Text','Pic']
with open('mycsv8.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['PostId','PostTypeName','PostBody'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random.choice(FPostType),fake.sentence(nb_words=6, variable_nb_words=False, ext_word_list=None)])

#populating table User_post
with open('mycsv9.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','PostId','DateUPO'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.date_between(start_date='-10y', end_date='today')])

#populating table Friendship
FFriendTypeName=['Work','Relative','School']
with open('mycsv10.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','FriendId','FriendTypeName','FStatus'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.random.choice(FFriendTypeName),fake.boolean(chance_of_getting_true=75)])

#populating table Groups
with open('mycsv11.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['GroupId','Groupname','Description'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.word(),fake.sentence(nb_words=6, variable_nb_words=False, ext_word_list=None)])

#populating table User_group
with open('mycsv12.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','GroupId','DateUG'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.date_between(start_date='-8y', end_date='today')])

#populating table ContentEditor
with open('mycsv13.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','GroupId'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000)])

#populating table Comment
with open('mycsv14.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['CommentId','CommentBody'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.sentence(nb_words=6, variable_nb_words=False, ext_word_list=None)])

#populating table User_comment
with open('mycsv15.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','CommentId','DateUC'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000),fake.date_between(start_date='-5y', end_date='today')])

#populating table Post_comment
with open('mycsv15.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['PostId','CommentId'])
     for i in range (1,500000):
          thewriter.writerow([fake.random_int(min=1, max=500000),fake.random_int(min=1, max=500000)])

#populating table GroupMembership
FMemberType=['Editor','Regular']
with open('mycsv16.csv','w',newline='') as f:
     thewriter = csv.writer(f)
     thewriter.writerow(['UserId','MemberType','GroupId'])
     for i in range (1,500000):
         thewriter.writerow([fake.random_int(min=1, max=500000),fake.random.choice(FMemberType),fake.random_int(min=1, max=500000)])

