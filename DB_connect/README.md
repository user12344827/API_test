# DB_connect

用Flask架設API連接資料庫內容，以Swagger頁面呈現Get、Post、Put等功能。

# 程式碼

```bash=
# api設定
api.py


# 回應設定
util.py


# /resource
# 登入設定
login.py
login_route_model.py


# 使用者設定
user.py
user_route_model.py


# 資料庫連結
mydb.py
```

# 成果展示

## Swagger頁面

1. Register
![圖片描述](../photo/register.png)

2. Login
![圖片描述](../photo/login.png)

3. Get
![圖片描述](../photo/get.png)

4. Post
![圖片描述](../photo/post.png)

5. Put
![圖片描述](../photo/put.png)

6. Delete
![圖片描述](../photo/delete.png)

## 資料庫畫面
1. 在Swagger註冊資料後，資料庫呈現
![圖片描述](../photo/register_DB.png)

2. Get/Post 打入資料到資料庫
![圖片描述](../photo/1_get_2_post_kiki_put.png)

3. 在Swagger刪除資料後，資料庫呈現
![圖片描述](../photo/delete_DB.png)