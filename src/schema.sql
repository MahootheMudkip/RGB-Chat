create DOMAIN NameType AS VARCHAR(50);
CREATE DOMAIN EmailType AS VARCHAR(128) CHECK (VALUE ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$');

CREATE TABLE Users (
    id          SERIAL,
    email       EmailType UNIQUE,
    f_name      NameType,
    l_name      NameType,
    password    VARCHAR(50) NOT NULL,
    bio         VARCHAR(100) NOT NULL,
    image_url   VARCHAR(200) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Dms (
    id          SERIAL,
    name        NameType,
    PRIMARY KEY (id)
);

CREATE TABLE Dm_Members (
    "user"      INTEGER NOT NULL REFERENCES Users(id),
    dm          INTEGER NOT NULL REFERENCES Dms(id),
    PRIMARY KEY ("user", dm)
);

CREATE TABLE Messages (
    id          SERIAL,
    message     TEXT NOT NULL, 
    time_sent   DATE NOT NULL,
    sender      INTEGER NOT NULL REFERENCES Users(id),
    sent_in     INTEGER NOT NULL REFERENCES Dms(id),
    primary key (id)
);