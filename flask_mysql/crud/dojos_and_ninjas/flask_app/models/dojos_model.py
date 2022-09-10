from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninjas_model

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for i in results:
            dojos_instance = cls(i)
            all_dojos.append(dojos_instance)
        return all_dojos

    @classmethod
    def create_dojos(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) > 0:
            dojos_instance = cls(result[0])
            ninjas_list = []
            for i in result:
                ninja_data = {
                    'id' : i['ninjas.id'],
                    'first_name' : i['first_name'],
                    'last_name' : i['last_name'],
                    'age' : i['age'],
                    'created_at' : i['ninjas.created_at'],
                    'updated_at' : i['ninjas.updated_at'],
                    'dojo_id' : i['dojo_id']
                }
                ninjas_instance = ninjas_model.Ninjas(ninja_data)
                ninjas_list.append(ninjas_instance)
            dojos_instance.ninjas = ninjas_list
            return dojos_instance
        return False