DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;


Create table Users(
UserId Varchar(25)not null unique,
Fname Varchar(30),
Lname Varchar(30),
Gender varchar (15),
DOB date,
Primary key(UserId)
);

Create table Profiles(
ProfileId varchar(25)not null unique,
Username varchar(30) not null unique,
Password Varchar(30),
Bio varchar(200),
RelationshipStatus varchar(20),
Primary key(ProfileId)
);

Create table User_profile(
UserId varchar(25),
ProfileId varchar(25),
Primary key (UserId,ProfileId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);
Create table profile_email(
ProfileId varchar(25),
email varchar(30),
Primary key(ProfileId,email),
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);
Create table profile_phonenumber(
ProfileId varchar(25),
PhoneNumber varchar(20),
Primary key (ProfileId,PhoneNumber),
Foreign key (ProfileId) REFERENCES Profiles(profileId) ON DELETE CASCADE
);

insert into Profiles values('profileId','username','password','bio','relationshipStatus');
insert into Profiles values('profileId2','2username','password','bio','relationshipStatus');

insert into Profiles values('profileI4d','u5sername','password','bio','relationshipStatus');

insert into Profiles values('profileId7','u9sername','password','bio','relationshipStatus');

insert into Profiles values('profile42Id','use32rname','password','bio','relationshipStatus');

DELIMITER //
CREATE PROCEDURE NewUser(in uname varchar(30),
							profileId varchar(25),
							userId Varchar(25),
							password Varchar(30),
							bio varchar(200),
							relationshipStatus varchar(20),
							fname Varchar(30),
							lname Varchar(30),
							gender varchar (15),
							dOB date,
							email varchar(30),
							phoneNumber varchar(20)
)
begin
	IF EXISTS (SELECT 1 FROM Profiles WHERE Username = uname) then
	BEGIN
	 SELECT 'Taken';
	END ;
	ELSE
	BEGIN
	 
	insert into Profiles values(profileId,uname,password,bio,relationshipStatus);
	insert into Users values(userId,fname,lname,gender,dOB);
	insert into User_profile values(userId,profileId);
	insert into profile_email values(profileId,email);
	insert into profile_phonenumber values(profileId,phoneNumber);
	COMMIT;
	select 'user added';
	END;
	END IF ;
end //

DELIMITER ;


CALL NewUser('theusername','theprofileid','theuserid','thepassword','thebio','shipStatus','thefname','thelname','thegender',now(),'themail','thephonenumber');

select *from Users;
select *from Profiles;
select *from User_profile;
select *from profile_email;
select *from profile_phonenumber;


/*
LOAD DATA LOCAL INFILE './profiles.csv'
INTO table Profiles 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


select count(ProfileId)+100000 from Profiles;
*/
