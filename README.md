

#プロジェクト名：uf_webapp_django

[進め方]
1.URL を決める  
2.ページを作成して、ある程度遷移できるようにしておく。  
3.モデルを作成する。  


# 機能名　　　 ： matching_place


# DB
    [Master]
        Job    職業マスタ
        Junle  職種マスタ
        Area   エリアマスタ
        Membar メンバーマスタ

    [Transaction]

# ユーザ作成

    python manage.py createsuperuser
     #username:admin
     #Email-address:akira248o@gmail.com
     #password:******1*1*

# Migration

    python manage.py makemigrations matching_place
    python namage.py migrate


# fake
    python manage.py showmigrations
    python manage.py migrate --fake matching_place zero
    python manage.py migrate --fake
    python manage.py migrate

# データベースデータの一括削除
    python manage.py help flush
    python manage.py flush --database=default


# データベースの一括削除

    db.sqlite3を消す


# VIEW
画面

    --- Member
       models.pyにて実装済み
    
    --- Place
    	*mail_address
    	*password
    	*name
    	tel
    	zip_code
    	address1
    	address2
    	address3
    	president_name
    
    --- Matching
    	*member_id
    	*place_id
