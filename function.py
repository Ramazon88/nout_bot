import sqlite3

con = sqlite3.connect('nout_baza.db', check_same_thread=False)
cur = con.cursor()

def add_user(user_id):
    try:
        sql = f"""
        insert into users(user_id) values({user_id})
        """
        cur.execute(sql)
        con.commit()
    except:
        pass

def get_step(user_id):
    sql = f"""
    select qadam from users where user_id = {user_id}
"""
    cur.execute(sql)
    return cur.fetchone()

def upd_step(user_id, qadam):
    sql = f"""
    update users set qadam = "{qadam}" where user_id = {user_id} 
"""
    cur.execute(sql)
    con.commit()
    return get_step(user_id)

def for_inform(user, qadam):
    try:
        sql = f"""
        insert into inform(user_id, username, ism, phone_number, joylashuv)
        values({user.id}, "{user.username}", "{qadam.get('ism', '')}","{qadam.get('tel', '')}","{qadam.get('locatsiya', '')}")
        """
        cur.execute(sql)
        con.commit()
    except:
        pass

def del_inform(user_id):
    sql = f"""
    delete from inform where user_id = {user_id}
"""
    cur.execute(sql)
    con.commit()
def get_brand():
    sql = "select brand_name from brand"
    cur.execute(sql)
    return cur.fetchall()


def get_brand_name(brand_id, ctg_id):

    sql = f"""select product_id, name from brand_inform
where brand_id = {brand_id} and ctg_id = {ctg_id} """
    cur.execute(sql)
    return cur.fetchall()

def for_ctg():
    sql = "select * from kategoriyalar"
    cur.execute(sql)
    return cur.fetchall()


def for_brand(ctg_id):
    sql = f"""select brand_id, brand_name from brand where ctg_id = {ctg_id}
    """
    cur.execute(sql)
    return cur.fetchall()

def get_inform(product_id):
    sql = f"""
    select inform, image, price from brand_inform 
    where product_id = {product_id}
"""
    cur.execute(sql)
    return cur.fetchall()
def get_contact(user_id):
    sql = f"select * from inform where user_id = {user_id}"
    cur.execute(sql)
    return cur.fetchall()

def get_inform_finally(product_id):
    sql = f"""
        select name, price from brand_inform 
        where product_id = {product_id}
    """
    cur.execute(sql)
    return cur.fetchall()
def add_inform_ctg(ctg_id):
    sql = f"""
    insert into brand_inform(ctg_id) values({ctg_id})
    
    """
    cur.execute(sql)
    con.commit()

def del_product_id():
    sql = """
    select product_id from brand_inform
    """
    cur.execute(sql)
    product_id = cur.fetchall()
    last_product = product_id[-1][0]
    sql1 = f"""
    delete from brand_inform where product_id = {last_product}
    """
    cur.execute(sql1)
    con.commit()
    return last_product

def last_product():
    sql = """
        select product_id from brand_inform
        """
    cur.execute(sql)
    product_id = cur.fetchall()
    last_product = product_id[-1][0]
    return last_product

def upd_brand_id(brand_name):
    sql1 = """
        select product_id from brand_inform
        """
    cur.execute(sql1)
    product_id = cur.fetchall()
    last_product = product_id[-1][0]
    sql = f"""
    select brand_id from brand where brand_name = "{brand_name}"
    """
    cur.execute(sql)
    product_id = cur.fetchall()
    brand = product_id[0][0]
    sql2 = f"""
    update brand_inform set brand_id={brand} where product_id = {last_product}
"""
    cur.execute(sql2)
    con.commit()
    return brand
def get_direct_ctg(ctg_name):
    sql = f"""select * from kategoriyalar where ctg_name = "{ctg_name}" """
    cur.execute(sql)
    return cur.fetchall()



def del_brand_id():
    sql = """
            select product_id from brand_inform
            """
    cur.execute(sql)
    product_id = cur.fetchall()
    last_product = product_id[-1][0]
    sql1 = f"""
    update brand_inform set brand_id = NULL where product_id = {last_product}
    """
    cur.execute(sql1)
    con.commit()
def upd_inform_name(inform_name):
    last_product_id = last_product()
    sql = f"""
    update brand_inform set name = "{inform_name}" where product_id = {last_product_id}
    """
    cur.execute(sql)
    con.commit()

def del_inform_name():
    last_product_id = last_product()
    sql1 = f"""
        update brand_inform set name = NULL where product_id = {last_product_id}
        """
    cur.execute(sql1)
    con.commit()

def upd_inform_inform(inform_name):
    last_product_id = last_product()
    a = get_inform_finally(last_product_id)
    sql = f"""
    update brand_inform set inform = "<b>{a[0][0]}</b>\n\n{inform_name}\n\n<b>{a[0][1]} SO`M</b>" where product_id = {last_product_id}
    """
    cur.execute(sql)
    con.commit()


def del_inform_inform():
    last_product_id = last_product()
    sql1 = f"""
            update brand_inform set inform = NULL where product_id = {last_product_id}
            """
    cur.execute(sql1)
    con.commit()

def upd_inform_price(inform_price):
    last_product_id = last_product()
    sql = f"""
    update brand_inform set price = {inform_price} where product_id = {last_product_id}
    """
    cur.execute(sql)
    con.commit()
def del_inform_price():
    last_product_id = last_product()
    sql1 = f"""
            update brand_inform set price = NULL where product_id = {last_product_id}
            """
    cur.execute(sql1)
    con.commit()

def upd_inform_image(inform_image):
    last_product_id = last_product()
    sql = f"""
        update brand_inform set image = "media/{inform_image}.jpg" where product_id = {last_product_id}
        """
    cur.execute(sql)
    con.commit()
def del_inform_image():
    last_product_id = last_product()
    sql1 = f"""
            update brand_inform set image = NULL where product_id = {last_product_id}
            """
    cur.execute(sql1)
    con.commit()

def inform_del():
    sql = "select product_id, name from brand_inform "
    cur.execute(sql)
    return cur.fetchall()


def del_del(product_id):
    try:
        sql = f"""
        delete from brand_inform where product_id = {product_id}
        
        """
        cur.execute(sql)
        con.commit()
    except:
        pass
def for_admin(user_id):
    sql = f"select user_id, phone_number from inform where user_id = {user_id}"
    cur.execute(sql)
    return cur.fetchall()

def add_admin(id):
    sql = f"""
    insert into admin(admin, phone_number) values({id[0][0]}, "{id[0][1]}") 
    """
    cur.execute(sql)
    con.commit()


def admin_inform():
    sql = "select admin from admin"
    cur.execute(sql)
    return cur.fetchall()

def get_admin_inform():
    sql = f"""
        select * from admin 
        """
    cur.execute(sql)
    return cur.fetchall()

def del_admin(id):
    try:
        sql = f"""
        delete from admin where admin_id = {id}

        """
        cur.execute(sql)
        con.commit()
    except:
        pass

print(admin_inform())




