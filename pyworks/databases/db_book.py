# 도서 관리 db
# 테이블 생성 - book
# 방식 - 동적 바인딩 방식 ('?' 기호 사용)
# DB의 레코드(행)의 자료 구조는 튜플임
# 요소가 1개일 때 (a, ) - 콤마를 찍어야 함
import sqlite3

def getconn():
    conn = sqlite3.connect('./output/bookdb.db')  # db 연결
    return conn

def create_book():
    #db가 없으면 생성되고 있으면 연결
    conn = getconn() #getconn() 호출
    cursor = conn.cursor() #작업 객체
    sql = """
        CREATE TABLE IF NOT EXISTS book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL, 
            price INTEGER NOT NULL
        );
    """
    cursor.execute(sql)
    conn.commit() # commit() 해줌
    conn.close()
def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? - 동적 바인딩
    sql = "INSERT INTO book(title, author, price) VALUES (?, ?, ?)"
    cursor.execute(sql, ('점프 투 파이썬', '박응용', 19800))
    conn.commit()
# create_book()
# insert_book()
def select_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? - 동적 바인딩
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cursor = conn.cursor()
    # '천 개의 파랑'의 가격을 15000원으로 변경하기
    sql = "UPDATE book SET price = ? WHERE title = ?"
    cursor.execute(sql, (15000, '천개의 파랑'))
    conn.commit()
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    # 책 번호가 2번인 도서의 정보 검색
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2,))
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete_book():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_book()
    select_book()
    
# update_book()
# insert_book()
# select_book()
