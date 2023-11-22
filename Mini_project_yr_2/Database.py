import mysql.connector


def create_db():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Romero23?", database="library")
    cur = conn.cursor()

    cur.execute("""create table if not exists btops(btid int(3) not null auto_increment primary key, topic char(45),
    unique(topic));""")

    cur.execute("""create table if not exists loan_sts(lbin binary(1), loan_status char(20) not null, 
primary key (lbin), unique(loan_status));""")

    cur.execute("""create table if not exists utype(uint int(1), usertype char(25) not null, 
    primary key (uint), unique(usertype));""")

    cur.execute("""create table if not exists usertb(uid int(1) not null auto_increment primary key, u_type int default 0, 
    username varchar(20), passw varchar(45), 
    constraint ubinary foreign key (u_type) references utype(uint), unique(username));""")

    cur.execute("""create table if not exists books(b_id int not null auto_increment primary key, b_title varchar(45),
    b_author char(45), bookscon int default 5, loaned binary(1) not null, 
    constraint lstat foreign key (loaned) references loan_sts(lbin),
    check ((bookscon>=0) AND (bookscon < 10)));""")

    cur.execute("""create table if not exists loan(lid int not null auto_increment primary key, bid int, uid int(1),
    loanout datetime not null, exreturn datetime not null, overdue int(4), returndate datetime, primary key (lid),
    constraint userid foreign key (uid) references user(uid), 
    constraint bidloan foreign key (id) references books(bid));""")

    cur.execute("""create table if not exists topicmid(bid int, btid int(3), 
        constraint topicbid foreign key (bid) references books(bid), 
        constraint topicid foreign key (btid) references btios(btid));""")

    conn.commit()
    cur.close()
    conn.close()
