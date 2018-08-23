# uf_webapp_django

1.URL を決める
2.ページを作成して、ある程度遷移できるようにしておく。
3.モデルを作成する。
---
プロジェクト名：matching_place

機能名　　　　：（１）Member 
　　　　　　　　（２）Place
　　　　　　　　（３）Matching

# DB
    Master
        Job
        Junle
        Area
        Membar

    Transaction

python manage.py createsuperuser
   #username:admin
   #Email-address:akira248o@gmail.com
   #password:hinata1113

# Migration

python manage.py makemigrations matching_place
python namage.py migrate




python manage.py showmigrations
python manage.py migrate --fake matching_place zero
#データベースデータの一括削除
python manage.py help flush
python manage.py flush --database=default

python manage.py migrate --fake
python manage.py migrate


db.sqlite3を消す


# VIEW
画面

--- Member
	* mail_address
	first_name
	middle_name
	last_name
	*nick_name
	*password
	tel
	birthday
	gender
	zip_code
	address1
	address2
	address3
	-
	area
	junle
	time_range

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
