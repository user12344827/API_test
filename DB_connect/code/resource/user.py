from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from . import user_route_model
from flask_jwt_extended import jwt_required

from . import mydb
import util

mydb.create_db_account()
mydb.create_user()

class Users(MethodResource):
    # GET_ALL
    @doc(description="Get Users info.", tags=["User"])
    @use_kwargs(user_route_model.UserGetSchema, location="query")
    @marshal_with(user_route_model.UserGetResponse, code=200)
    def get(self, name, gender, birth, note): # 增加3個變數
        db, cursor = mydb.db_init()
        try:
            sql = """
                INSERT INTO user2 (name, gender, birth, note)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (name, gender, birth, note))
            db.commit()
            return util.success(status_code=201)
        except Exception as e:
            db.rollback()
            return util.failure(str(e), 500)
        finally:
            db.close()

    # Create User
    @doc(description="Get Users info.", tags=["User"])
    @use_kwargs(user_route_model.UserPostSchema, location="form")
    @marshal_with(user_route_model.UserPostResponse, code=201)
    def post(self, name, gender, birth, note): # 增加3個變數
        db, cursor = mydb.db_init()
        try:
            sql = """
                INSERT INTO user2 (name, gender, birth, note)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (name, gender, birth, note))
            db.commit()
            return util.success(status_code=201)
        except Exception as e:
            db.rollback()
            return util.failure(str(e), 500)
        finally:
            db.close()

class User(MethodResource):
    @doc(description="Get Users info.", tags=["User"])
    @marshal_with(user_route_model.UserSingleGetResponse, code=200)
    # "Get" single by id，用get查找資料
    def get(self, id):
        db, cursor = mydb.db_init()
        try:
            sql = "SELECT * FROM user2 WHERE id = %s"
            cursor.execute(sql, (id,))
            user = cursor.fetchone()
            
            if user is None:
                return util.failure(f"User id {id} not found.", status_code=404)
            return util.success(user)
        except Exception as e:
            return util.failure(str(e), 500)
        finally:
            db.close()
    
    @doc(description="Get Users info.", tags=["User"])
    @use_kwargs(user_route_model.UserPutSchema, location="form")
    @marshal_with(user_route_model.UserPutResponse, code=400)
    def put(self, id, name, birth, gender, note):
        db, cursor = mydb.db_init()
        try:
            sql = """
                UPDATE user2 
                SET name = %s, birth = %s, gender = %s, note = %s
                WHERE id = %s
            """
            result = cursor.execute(sql, (name, birth, gender, note, id))
            if result == 0:
                return util.failure(f"User id {id} not found.", status_code=404)
            
            db.commit()
            return util.success()
        except Exception as e:
            db.rollback()
            return util.failure(str(e), 500)
        finally:
            db.close()
    
    @doc(
        description="Delete Single Users info.",
        tags=["User"],
        security=[{"bearer": []}],
    )
    @marshal_with(user_route_model.UserSingleDeleteResponse, code=204)
    @jwt_required()
    def delete(self, id):
        db, cursor = mydb.db_init()
        try:
            sql = "DELETE FROM user2 WHERE id = %s"
            result = cursor.execute(sql, (id,))
            if result == 0:
                return util.failure(f"User id {id} not found.", status_code=404)
            
            db.commit()
            return util.success(status_code=204)
        except Exception as e:
            db.rollback()
            return util.failure(str(e), 500)
        finally:
            db.close()