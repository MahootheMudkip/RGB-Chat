create Table Users (
    id serial,
    email text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    password text NOT NULL,
    bio text NOT NULL,
    image_url text NOT NULL,
    PRIMARY KEY (id)
)