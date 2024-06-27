from bottle import *
import sqlite3
import json


actual_data = ['', '', '']
actual_customer = '1'
actual_stadium = '1'
actual_match = ''
global data


match_query="""
SELECT 
    meccs.id AS meccs_id,
    szektor.id AS szektor_id,
    szabad.szabad,
    szabad.ar
FROM 
    szabad
INNER JOIN 
    meccs ON szabad.meccs_id = meccs.id
INNER JOIN 
    szektor ON szabad.szektor_id = szektor.id;
 """
 
query="""
SELECT 
    csapat.nev AS csapat_nev, 
    meccs.vendeg, 
    meccs.datum, 
    stadion.nev AS stadion_nev, 
    stadion.varos,
    meccs.id AS meccs_id
FROM 
    meccs
INNER JOIN 
    csapat ON meccs.hazai_id = csapat.id
INNER JOIN 
    stadion ON csapat.stadion_id = stadion.id;
"""

@route('/')
@route('/home')
def display_matches():
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    cur.execute(query)
    global meccsek
    meccsek = cur.fetchall()
    conn.close()
    return template('index.html', meccsek = meccsek)
    
def ticket_choose_core():
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    actual_data[0] = actual_match
    cur.execute(match_query)
    global all
    all = cur.fetchall()
    for a in all:
        if str(a[0]) == str(actual_match) and str(a[1]) == str(actual_data[1]):
            global uzenet
            uzenet = [a[2], a[3]]                    
    conn.close()
        
def ticket_choose():
    @route('/'+str(actual_match)+'/vip_tickets', method= ['POST', 'GET']) 
    def vip_tickets():
        actual_data[1] = '1' 
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)

    
    @route('/'+str(actual_match)+'/a_tickets', method= ['POST', 'GET']) 
    def a_tickets():
        actual_data[1] = '2'
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)
  
    
    @route('/'+str(actual_match)+'/b_tickets', method= ['POST', 'GET']) 
    def b_tickets():
        actual_data[1] = '3'
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)
    
    
    @route('/'+str(actual_match)+'/c_tickets', method= ['POST', 'GET']) 
    def c_tickets():
        actual_data[1] = '4'
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)

        
    @route('/'+str(actual_match)+'/d_tickets', method= ['POST', 'GET']) 
    def d_tickets():
        actual_data[1] = '5'
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)
    
    
    @route('/'+str(actual_match)+'/guest_tickets', method= ['POST', 'GET']) 
    def guest_tickets():
        actual_data[1] = '6'
        ticket_choose_core()
        return template('ticket_buy_complete.html', uzenet = uzenet)
    

def match_choose_core():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    m = cur.execute('SELECT id FROM MECCS')
    matches = m.fetchall()
    global allmatch
    allmatch = [match[0] for match in matches]

def match_choose():

    match_choose_core()
    
    @route('/1', method= ['POST', 'GET'])
    def match1():
        global actual_match
        actual_match = allmatch[0]
        ticket_choose()
        return template('ticket_buy.html')
    
    @route('/2', method= ['POST', 'GET'])
    def match2():
        global actual_match
        actual_match = allmatch[1]
        ticket_choose()
        return template('ticket_buy.html')

    @route('/3', method= ['POST', 'GET'])
    def match3():
        global actual_match
        actual_match = allmatch[2]
        ticket_choose()
        return template('ticket_buy.html')

    @route('/4', method= ['POST', 'GET'])
    def match4():
        global actual_match
        actual_match = allmatch[3]
        ticket_choose()
        return template('ticket_buy.html')

    @route('/5', method= ['POST', 'GET'])
    def match5():
        global actual_match
        actual_match = allmatch[4]
        ticket_choose()
        return template('ticket_buy.html')

match_choose()

@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./static')


@route('/receive_data', method=['POST']) 
def receive_data():
    global data
    data = request.json
    print(f"Received data: {data}")
    response.content_type = 'application/json'
    return {"status": "success", "received": data}


@route ('/no_tickets')
def no_tickets():
    return template ('no_tickets.html')

@route('/success', method=['POST', 'GET'])
def success_buy():
        actual_data[2] = str(data)
        conn = sqlite3.connect('./database.db')
        cur = conn.cursor()
        cur.execute('SELECT meccs_id, szektor_id, szabad FROM szabad;')
        all = cur.fetchall()
        for a in all:
            if str(a[0]) == str(actual_data[0]) and str(a[1]) == str(actual_data[1]):
                global update_value
                update_value = int(a[2]) - int(actual_data[2])
        cur.execute('UPDATE szabad SET szabad ='
                    + str(update_value)+' WHERE meccs_id = '
                    + str(actual_data[0])
                    + ' AND szektor_id ='
                    + str(actual_data[1]))
        cur.execute('INSERT INTO jegyek (meccs_id, vasarlo_id, stadion_id, szektor_id, db)'
                    'VALUES ('+ str(actual_data[0])+', '+str(actual_customer)+', '+str(actual_stadium)+', '+str(actual_data[1])+', '+str(actual_data[2])+')')
        conn.commit()
        return template('success.html')

@route ('/tickets', method=['POST', 'GET'])
def my_tickets():
        conn = sqlite3.connect('./database.db')
        cur = conn.cursor()
        query = """
            SELECT csapat.nev AS hazai, meccs.vendeg, stadion.nev, stadion.varos, szektor.kategoria, meccs.datum, jegyek.db
            FROM jegyek
            INNER JOIN meccs ON jegyek.meccs_id = meccs.id
            INNER JOIN csapat ON meccs.hazai_id = csapat.id
            INNER JOIN stadion on jegyek.stadion_id = stadion.id
            INNER JOIN szektor ON jegyek.szektor_id = szektor.id
        """
        cur.execute(query)
        ticks = cur.fetchall()
        return template('tickets.html', ticks = ticks)
    
    
@route('/admin')
def admin():
    return template('admin.html')

@route('/create')
def create():
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    query = """
        SELECT
        csapat.nev AS csapat_nev,
        meccs.vendeg,
        meccs.datum,
        stadion.nev AS stadion_nev,
        stadion.varos
    FROM
        meccs
    INNER JOIN
        csapat ON meccs.hazai_id = csapat.id
    INNER JOIN
        stadion ON csapat.stadion_id = stadion.id;
    """
    cur.execute(query)
    meccsek = cur.fetchall()
    return template('create.html', meccsek = meccsek)

@route('/delete')
def delete():
    ms = []
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    cur.execute(query)
    meccsek = cur.fetchall()
    return template('delete.html', meccsek= meccsek)

@route('/receive-array', method='POST')
def receive_array():
    try:
        data = request.json # Receive JSON data from frontend
        if data is None:
            return {"status": "error", "message": "No JSON data received"}
        
        # Assuming data is a JSON array with two elements
        if len(data) != 8:
            return {"status": "error", "message": "Expected array length is not 2"}
        
        gName = data[0]
        mDate = data[1]
        arVIP = data[2]
        arA = data[3]
        arB = data[4]
        arC = data[5]
        arD = data[6]
        arGuest = data[7]
        
        # Process the data as needed (e.g., insert into database)
        insertMatch(gName, 1,  mDate)
        
        insertPrices(arVIP, arA, arB, arC, arD, arGuest)
        
        return {"status": "success", "message": "Data received and processed"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    
def insertMatch(first_item, constant_value, second_item):
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO meccs (vendeg, hazai_id, datum) VALUES (?, ?, ?)', (first_item, constant_value, second_item))
    conn.commit()
    conn.close()

def insertPrices(VIP, A, B, C, D, Guest):
    arlist = [VIP, A, B, C, D, Guest]
    conn = sqlite3.connect('./database.db')
    cur = conn.cursor()
    cur.execute('''SELECT stadion.vip_max, stadion.a_max, stadion.b_max, stadion.c_max, stadion.d_max, stadion.vendeg_max FROM Stadion''')
    res = cur.fetchall()
    cur.execute('SELECT id FROM Meccs')
    res2 = cur.fetchall()
    for i in range(6):
        cur.execute('INSERT INTO szabad (meccs_id, szektor_id, stadion_id, szabad, ar) VALUES (?, ?, ?, ?, ?)',(res2[len(res2)-1][0], i+1, 1, res[0][i], arlist[i]))
        conn.commit()
    conn.close()

@route('/remove-row', method='POST')
def delete_row():
    try:
        data = request.json
        row_id = data.get('id')
        row_id = int(row_id)
        
        if row_id is None:
            return {"status": "error", "message": "ID is required"}
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = 'DELETE FROM meccs WHERE id = ?'
        cursor.execute(query, (row_id,))
        conn.commit()
        query = 'DELETE FROM Szabad WHERE meccs_id = ?'
        cursor.execute(query, (row_id,))
        conn.commit()
        conn.close()
        
        return {"status": "success", "message": "Row deleted successfully"}
    
    except sqlite3.Error as error:
        return {"status": "error", "message": str(error)}
    


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

