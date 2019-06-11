from flask import Flask, request, abort, jsonify
import logging
import psycopg2
from config import config
from flask import send_file
import os


app = Flask(__name__)



@app.route("/")
def hello():
    return "Server is running"

@app.route("/addData", methods=['POST'])
def addData():
    data = request.get_json()
    print(data)
    text = data['data']
    print(type(text))
    print(text)
    sql = "insert into testtable(data) values(%s) RETURNING id;"

    conn = None
    dataID = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (text,))
        dataID = cur.fetchone()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return str(dataID)

@app.route("/getAllData", methods=['GET'])
def getAllData():
    sql="""SELECT * FROM testtable"""
    conn = None
    data =   {}
    dataList = []


    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        allData = cur.fetchall()

        for singleData in allData:

            dataId = singleData[1]
            text = singleData[0]

            dataAsDict = {
                'id:': dataId,
                'text': text
            }

            dataList.append(dataAsDict);

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
        data.update({'data': dataList})
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

