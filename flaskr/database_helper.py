def db_select(mysql, cmd, params):
    cursor = mysql.connection.cursor()
    cursor.execute(cmd, params)
    results = cursor.fetchall()
    cursor.close()
    return results


def db_commit(mysql, cmd, params):
    cursor = mysql.connection.cursor()
    cursor.execute(cmd, params)
    mysql.connection.commit()
    cursor.close()
    return
