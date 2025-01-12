import sqlite3
import pandas as pd 

conn = ""
try:
    conn = sqlite3.connect("strive.db")
except Exception as ex:
    print(ex)


def sql_query(stc):
    try:
        c = conn.cursor()
        reply = c.execute(stc)
        conn.commit()
        return reply
    except Exception as ex:
        print(ex)

def pandas_select(stc):
    try:
        if stc.split()[0].lower() == "select":
            df = pd.read_sql_query(stc, conn)
            return df
        else:
            return pd.DataFrame()
    except Exception as ex:
        print(ex)
        return pd.DataFrame()

def upload_data(name, path, head = 0):
    try:
        df = pd.read_csv(path)
        frame = df.to_sql(name, conn, if_exists = 'replace', index=False)
        return frame
    except Exception as ex:
        print(ex)   

#conn close is only required for client, it should be open for others
def close():
    conn.close() 