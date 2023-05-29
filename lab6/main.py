import cherrypy as cherrypy
from peewee import *

db = SqliteDatabase('database.db')


class MyTable(Model):
    class Meta:
        database = db
        db_table = 'lab6'

    idx = PrimaryKeyField(unique=True)
    date = DateField()
    cost = IntegerField()
    name = TextField()

    def Add(self, date, cost, name):
        MyTable(date=date, cost=cost, name=name).save()

    def Update(self, idx, date, cost, name):
        table = MyTable.get(idx=idx)
        table.date = date
        table.cost = cost
        table.name = name
        table.save()

    def getColumn(self):
        cursor = db.cursor()
        cursor.execute('PRAGMA table_info("lab6")')
        columns = [i[1] for i in cursor.fetchall()]
        return columns

    def getStrings(self):
        cursor = db.cursor()
        sqlite_select_query = """SELECT * from lab6"""
        cursor.execute(sqlite_select_query)
        result = cursor.fetchall()
        return result


class IndexPage(object):

    def __init__(self, columns, data):
        self.columns = columns
        self.data = data

    @cherrypy.expose
    def index(self):
        return f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>Лаба 6</title>
                <style>
                    body {{
                        font-family: 'Roboto', sans-serif;
                        background-color: #1a1a1a;
                        color: #fff;
                        margin: 0;
                        padding: 0;
                    }}
                    
                    h1 {{
                        color: #ebebeb;
                        text-align: center;
                        margin-top: 50px;
                        font-size: 3rem;
                        font-weight: bold;
                    }}
                    
                    table {{
                        margin: auto;
                        max-width: 800px;
                        width: 80%;
                        box-shadow: 0px 2px 2px rgba(255, 255, 255, 0.25);
                        border-collapse: collapse;
                        margin-top: 50px;
                    }}
                    
                    td, th {{
                        border: 1px solid #4f4f4f;
                        padding: 10px;
                        text-align: center;
                        font-size: 1.2rem;
                    }}
                    
                    th {{
                        background-color: #ff6b6b;
                        color: white;
                    }}
                    
                    tr , td {{
                        transition: all 0.2s ease-in-out;
                    }}
                    
                    tr:hover {{
                        transform: scale(1.05);
                        background-color: #ff9b9b;
                        cursor: pointer;
                    }}
                    
                    td:hover {{
                        color: white;
                        transform: scale(1.05);
                        background-color: #ff6b6b;
                    }}
                </style>
            </head>
            <body>
                <h1>Лабораторная 6</h1>
                <table>
                    <tr>
                        {
        "".join(["<th>" + i + "</th>"
                 for i in self.columns])
        }
                    </tr>
                    {self.data}
                </table>
            </body>
        </html>
        '''


def table_style(strings):
    table_line = ""
    for tr in strings:
        table_line += "<tr>"
        for td in tr:
            table_line += f"<td style='padding: 10px; text-align:center; font-size: 15px;" \
                          f" border: 1px solid #ddd;'> {td} </td>"
        table_line += "</tr>"
    return table_line


if __name__ == '__main__':
    table = MyTable()

    columns = table.getColumn()
    lines = table.getStrings()

    table_line = table_style(lines)

    cherrypy.quickstart(IndexPage(columns, table_line))

    db.close()
