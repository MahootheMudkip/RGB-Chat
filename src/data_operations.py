import psycopg2

# Connect to pg database


def on_connection(function):
    def wrapper(*args, **kwargs):
        result = ''
        db = psycopg2.connect(user="postgres",
                              password="RGBadmin",
                              host="localhost",
                              port="8080",
                              database="postgres")
        try:
            result = function(db, *args, **kwargs)
        except Exception as e:
            db.rollback()
        else:
            db.commit()
        finally:
            db.close()
        return result
    return wrapper


@on_connection
def add_user(db, email, f_name, l_name, password, bio, profile_img_url):

    cur = db.cursor()
    query = '''
        INSERT INTO Users(email, first_name, last_name, password, bio, image_url)
        VALUES (%s, %s, %s, %s, %s, %s);
    '''
    cur.execute(query, (email, f_name, l_name, password, bio, profile_img_url))

    query = '''
        SELECT COUNT(*)
        FROM Users
    '''

    cur.execute(query)

    idthing = cur.fetchone()
    print(idthing)
    db.commit()

    return idthing[0] - 1