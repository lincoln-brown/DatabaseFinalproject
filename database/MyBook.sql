DROP DATABASE IF EXISTS MyBook;
CREATE DATABASE MyBook;
USE MyBook;


/* derived from entity User */
Create table Users(
UserId Varchar(15),
Fname Varchar(30),
Lname Varchar(30),
Gender varchar (15),
Passwordd Varchar(30),
Primary key(UserId)
);

/* derived from entity profile */
Create table Profiles(
ProfileId varchar(15),
Username varchar(30),
Bio varchar(50),
RelationshipStatus varchar (20),
Primary key(ProfileId)
)

/* derived from User entity and profile entity relationship */
Create table User_profile(
UserId varchar(15),
ProfileId varchar(15),
Primary key (UserId,Username),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);

/* derived from multivalue attribute */
Create table User_email(
UserId varchar(15),
email varchar(30),
Primary key(UserId,email),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
);

/* derived from multivalue attribute */
Create table profile_phonenumber(
ProfileId varchar(15),
PhoneNumber varchar(20),
Primary key (Username,PhoneNumber),
Foreign key (ProfileId) REFERENCES Profiles(profileId) ON DELETE CASCADE
);

/* derived from multivalue attribute*/
Create table profile_address (
ProfileId varchar(15),
AddressId varchar(15),
Street varchar(30),
City varchar(30),
Primary key(ProfileId, AddressId),
Foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE
);


/* derived from entity photo */
Create table Photo(
PhotoId Varchar(15),
images varchar (30),
Photoname Varchar(30),
Primary key(PhotoId)
);

/* derived from User entity and Photo entity relationship */
Create table User_photo(
UserId varchar(15),
PhotoId varchar(15),
DateofUP Date,
Primary key(ProfileId,PhotoId),
foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
foreign key(PhotoId) REFERENCES Photo(PhotoId) ON DELETE CASCADE
);


/* derived from Post entity */
Create table Post(
PostId varchar(15),
PostTypeName varchar(20),
PostBody varchar(50),
Primary key(PostId)
);


/* derived from User entity and Post entity */
Create table User_post(
UserId Varchar(15),
PostId Varchar(15),
DateofUPO Date,
Primary key(UserId, PostId),
foreign key (ProfileId) REFERENCES Profiles(ProfileId) ON DELETE CASCADE,
foreign key (PostId) REFERENCES Post(PostId) ON DELETE CASCADE
);

/* derived from self reliance relation on User (User is a friend to another user) */
Create table Friendship(
UserId varchar(15),
FriendId varchar(15),
FriendTypeName varchar(20),
FStatus Boolean,
Primary key(UserId,FriendId),
Foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE, 
);


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

/* derived from entity comment*/
Create table Comment(
CommentId varchar(15),
CommentBody Varchar(50),
Primary Key (CommentId)
);

/* derived from User entity and Comment entity relationship */
Create table User_comment(
UserId varchar(15),
CommentId varchar(15),
DateofUC Date,
Primary key (UserId, CommentId),
foreign key (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,
foreign key (CommentId) REFERENCES Comment(CommentId) ON DELETE CASCADE
);

/* derived from Post entity and Comment entity relationship */
Create table Post_comment(
PostId varchar(15),
CommentId varchar(15),
Primary key(PostId,CommentId),
foreign key (PostId) REFERENCES Post(PostId) ON DELETE CASCADE,
foreign key (CommentId) REFERENCES Comment(CommentId) ON DELETE CASCADE
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


