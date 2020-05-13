DROP DATABASE IF EXISTS MyBook;
CREATE DATABASE MyBook;
USE MyBook;
Drop table if exists Users;
Drop table if exists Profiles;
Drop table if exists User_profile;
Drop table if exists Profile_email;
Drop table if exists Profile_phonenumber;
Drop table if exists Profile_address;
Drop table if exists Photo;
Drop table if exists User_photo;
Drop table if exists Post;
Drop table if exists User_post;
Drop table if exists Friendship;
Drop table if exists Groups;
Drop table if exists User_group;
Drop table if exists ContentEditor;
Drop table if exists Comment;
Drop table if exists User_comment;
Drop table if exists Post_comment;
Drop table if exists Groupmembership;

/* derived from entity User */
Create table Users(
UserId Varchar(25)not null unique,
Fname Varchar(30),
Lname Varchar(30),
Gender varchar (15),
DOB date,
Primary key(UserId)
);

/* derived from entity profile */
Create table Profiles(
ProfileId varchar(25)not null unique,
Username varchar(30) not null unique,
Password Varchar(30),
Bio varchar(200),
RelationshipStatus varchar(20),
Primary key(ProfileId)
);

/* derived from User entity and profile entity relationship */
Create table User_profile(
UserId varchar(25),
ProfileId varchar(25),
Primary key (UserId,ProfileId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);

/* derived from multivalue attribute */
Create table profile_email(
ProfileId varchar(25),
email varchar(30),
Primary key(ProfileId,email),
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);

/* derived from multivalue attribute */
Create table profile_phonenumber(
ProfileId varchar(25),
PhoneNumber varchar(20),
Primary key (ProfileId,PhoneNumber),
Foreign key (ProfileId) REFERENCES Profiles(profileId) ON DELETE CASCADE
);

/* derived from multivalue attribute*/
Create table profile_address (
ProfileId varchar(25),
AddressId varchar(15),
Street varchar(30),
City varchar(30),
Primary key(ProfileId, AddressId),
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);


/* derived from entity photo */
Create table Photo(
PhotoId Varchar(15),
category varchar (30),
Photoname Varchar(30),
Primary key(PhotoId)
);

/* derived from User entity and Photo entity relationship */
Create table User_photo(
UserId varchar(15),
PhotoId varchar(15),
DateofUP Date,
Primary key(UserId,PhotoId),
foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
foreign key(PhotoId) REFERENCES Photo(PhotoId) ON DELETE CASCADE
);

/*=-------------------------to change----------------------------------*/



/* derived from friendship entity and profile entity relationship */
/* derived from self reliance relation on Profile (profile of friend .`.profileid==FriendsProfileid) */
Create table Profile_friends(
ProfileId varchar(25),
FriendsProfileId varchar(25),
FriendGroupName varchar(20),
Primary key (ProfileId,FriendsProfileId),
Foreign key (FriendsProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE,
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);

/* derived from Post entity */
Create table Post(
PostId int(11) NOT NULL AUTO_INCREMENT,
PostTypeName varchar(20),
PostBody varchar(50),
Primary key(PostId)
);


/* derived from User entity and Post entity */
Create table Profile_post(
ProfileId Varchar(25),
PostId int(11),
DateofUPO Date,
Primary key(ProfileId, PostId),
foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE,
foreign key (PostId) REFERENCES Post(PostId) ON DELETE CASCADE

);

/* derived from entity comment*/
Create table Comment(
CommentId int(11) NOT NULL AUTO_INCREMENT,
CommentBody Varchar(50),
Primary Key (CommentId)
);

/* derived from User entity and Comment entity relationship */
Create table Profile_comment(
ProfileId varchar(25),
CommentId int(11),
DateofUC Date,
Primary key (ProfileId, CommentId),
foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE,
foreign key (CommentId) REFERENCES Comment(CommentId) ON DELETE CASCADE
);

/* derived from Post entity and Comment entity relationship */
Create table Post_comment(
PostId int(11),
CommentId int(11),
Primary key(PostId,CommentId),
foreign key (PostId) REFERENCES Post(PostId) ON DELETE CASCADE,
foreign key (CommentId) REFERENCES Comment(CommentId) ON DELETE CASCADE
);


/*---------------------------------------above changed---------------------------------------------------------*/
/* derived from entity group */
Create table Groups(
GroupId varchar(15),
GroupName varchar(30),
Descriptions varchar(50),
Primary key(GroupId)
);

/* derived from User entity and Group entity relationship (User creates group) */
Create table User_group(
UserId varchar(15),
GroupId varchar(15),
DateofUCG date,
Primary key (UserId,GroupId),
foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
foreign key (GroupId) REFERENCES Groups(GroupId) ON DELETE CASCADE
);

/* derived from (User selects User )relationship */
Create table ContentEditor(
UserId varchar(15),
GroupId varchar(15),
Primary key(UserId,GroupId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key(GroupId) REFERENCES Groups(GroupId) ON DELETE CASCADE
);


/* derived from User entity and Group entity relationship (Friend is a member in group) */
Create table Groupmembership(
UserId varchar(15),
MemberTypeName varchar(20),
GroupId varchar(15),
Primary key(GroupId,UserId),
Foreign key (userId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key (GroupId) REFERENCES Groups(GroupId) ON DELETE CASCADE
);
/*--------------------------------------------------------------------------------------------*/
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
	insert into	profile_address values(profileId,profileId,profileId,profileId);
	COMMIT;
	select 'User_added';
	END;
	END IF ;
end //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE NewComment (in commentBdy Varchar(50),
	ProfileId varchar(25),
	CommentId int(11),
	PostId int(11))

begin
	insert into Comment (CommentBody)values(commentBdy);
	insert into Profile_comment values(ProfileId,CommentId,now());
	insert into Post_comment values(PostId,CommentId);
		Select "comment ADDED";
	COMMIT;

end //

show tables;

LOAD DATA LOCAL INFILE './Users.csv'
INTO table Users 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './profiles.csv'
INTO table Profiles 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

/*
LOAD DATA LOCAL INFILE './User_profile.csv'
INTO table User_profile 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
*/


LOAD DATA LOCAL INFILE './profile_email.csv'
INTO table profile_email 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './profile_phonenumber.csv'
INTO table profile_phonenumber 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './profile_address.csv'
INTO table profile_address 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

/*
LOAD DATA LOCAL INFILE './photo.csv'
INTO table Photo 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE './User_photo.csv'
INTO table User_photo 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
*/

LOAD DATA LOCAL INFILE './Post.csv'
INTO table Post 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './Profile_post.csv'
INTO table Profile_post 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE './Comment.csv'
INTO table Comment 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './Profile_comment.csv'
INTO table Profile_comment 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './Post_comment.csv'
INTO table Post_comment 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;






/*
LOAD DATA LOCAL INFILE './Friendship.csv'
INTO table Friendship 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './Groups.csv'
INTO table Groups 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './User_group.csv'
INTO table User_group 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE './ContentEditor.csv'
INTO table ContentEditor 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;





LOAD DATA LOCAL INFILE './GroupMembership.csv'
INTO table Groupmembership 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
*/