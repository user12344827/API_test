from flask_jwt_extended import create_access_token
from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
import util
from resource import login_router_model
from datetime import timedelta
from resource import mydb

class Register(MethodResource):
    @doc(description="User Registration", tags=["Login"])
    @use_kwargs(login_router_model.RegisterSchema, location="form")
    @marshal_with(login_router_model.RegisterResponse, code=201)
    def post(self, name, account, password):
        db, cursor = mydb.db_init()
        try:
            # 檢查帳號是否已存在
            check_sql = "SELECT * FROM user1 WHERE account = %s"
            cursor.execute(check_sql, (account,))
            if cursor.fetchone():
                return util.failure("Account already exists", status_code=400)
            
            # 新增用戶
            sql = """
                INSERT INTO user1 (name, account, pwd)
                VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (name, account, password))
            db.commit()
            return util.success(status_code=201)
            
        except Exception as e:
            db.rollback()
            return util.failure(str(e), status_code=500)
        finally:
            db.close()

class Login(MethodResource):
    @doc(description="User Login", tags=["Login"])
    @use_kwargs(login_router_model.LoginSchema, location="form")
    @marshal_with(login_router_model.LoginResponse, code=200)
    def post(self, account, password):
        db, cursor = mydb.db_init()
        try:
            # 檢查帳號密碼是否正確
            sql = "SELECT * FROM user1 WHERE account = %s AND pwd = %s"
            cursor.execute(sql, (account, password))
            user = cursor.fetchone()
            
            if user:
                # 如果驗證成功，創建 JWT token
                token = create_access_token(
                    identity={"account": account}, 
                    expires_delta=timedelta(days=1)
                )
                return util.success(token)
            else:
                return util.failure("Account or password is wrong", status_code=401)
                
        except Exception as e:
            return util.failure(str(e), status_code=500)
        finally:
            db.close()