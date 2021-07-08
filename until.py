import  sqlite3

def add_all_question(data):
    conn = sqlite3.connect("data/Woodpecker_API.db")
    sql = """
    INSERT OR REPLACE INTO question (
                         number,
                         Content
                     )
                     VALUES 
                     (?, ? ) 
    """
    conn.execute(sql, ( int(data["Number"]),str(data["Content"]) ))
    conn.commit()

    data1 = data["Options"]
    sql1 ="""
    INSERT OR REPLACE INTO option (
                         q_number,
                         OptionKey,
                         OptionContent
                     )
                     VALUES 
                     (?, ?, ?) 
    """
    for i in range(len(data1)):
        conn.execute(sql1, (int(data["Number"]), str(data1[i]["OptionKey"]), str(data1[i]["OptionContent"])))
        conn.commit()
    conn.close()


def get_all_answer(sql):
    conn = sqlite3.connect("data/Woodpecker_API.db")
    data = conn.execute(sql).fetchall()
    conn.close()
    return data

