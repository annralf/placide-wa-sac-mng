# Mongo Conection with mongoengine ORM

import mongoengine

mongoengine.connect(db='myFirstDatabase', 
                    host='mongodb+srv://admin:rVWMftMT4DjlIEAh@cluster0.g3uvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
                    username='admin',
                    password='rVWMftMT4DjlIEAh')

