from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .Module.UseMongoDB import RecSysLogsToMongo
import json
import glob
from django.db import connection
from django.contrib.auth.decorators import login_required


db = RecSysLogsToMongo()

def index(request):
    static_list = glob.glob('web/static/music/*.mp3')
    name_of_musics = [f.split('/')[-1].split('.')[0] for f in  static_list]
    return render(request,'index.html',{
        'mp3_list':name_of_musics,
    })

@csrf_exempt
def music_record_logs(request):
    if request.method == 'POST':
        # db.insert_log_to_mongodb(request.body)
        return HttpResponse(request.body)

@csrf_exempt
def add_to_playlist(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        user = data['user']
        track_info = data['track'].split(':')
        print(track_info)
        ablum_id, track_id = track_info[0], track_info[1]
        row = (user, track_id, ablum_id)
        sql = "INSERT INTO tracks.tracks_userslike (`user`, `track`, `album`) VALUES "+ str(row) + ";"
        run_sql_cmd(sql)
        with connection.cursor() as cursor:
                cursor.execute(sql)
        return HttpResponse('Add')

@csrf_exempt
def remove_from_playlist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data['user']
        track_info = data['track'].split(':')
        ablum_id, track_id = track_info[0], track_info[1]
        sql = "delete from tracks_userslike where user ='" + user+ "' and track ='"+ track_id +"' and album ='" +ablum_id+ "';"
        with connection.cursor() as cursor:
                cursor.execute(sql)
        return HttpResponse('Remove')


@login_required
def browser_artist(request):
    # Every time user refresh page will get 30 different artists.
    sql = 'select * from tracks_artist order by rand() limit 30'
    dict_row = run_sql_cmd(sql)
    return render(request,'browserArtist.html',{
        'artist_list':dict_row,
    })

@login_required
def browser_artist_from_letter(request, letter):
    sql = "SELECT * from  tracks.tracks_artist where Name LIKE '" + letter +"%'"
    dict_row = run_sql_cmd(sql)
    return render(request,'selected_artist.html',{
        'artist_list':dict_row,
    })

@login_required
def artist_info(request, artist_id):
    sql = "select * from tracks_album where artist_id ='" + artist_id +"'ORDER BY release_date DESC;"
    dict_row = run_sql_cmd(sql)
    return render(request,'artistInfo.html',{
        'artist_album':dict_row,
    })

@login_required
def ablum_info(request, album_id):
#     user_name = request.user
    user_name = request.user    
    sql = "select track_id, artist, artist_id, album_name, album_id, img, name, preview_url, user  from ( \
	select  features.id as track_id, M.artist, M.artist_id, M.album_name, M.album_id,  M.img, features.id, features.name, features.preview_url \
	from tracks_features as features INNER JOIN  ( \
	SELECT artist.name as artist, artist.id as artist_id, album.name as album_name, \
	album.img_url as img, album.id as album_id \
	FROM tracks_artist as artist \
	INNER JOIN tracks_album as album \
	where album.artist_id = artist.id) M \
        where M.album_id = features.album_id and M.album_id = '" + album_id + "' ) Album \
	left Join tracks.tracks_userslike as L  on L.track = Album.id and L.user = '" + str(user_name) + "'"
    dict_row = run_sql_cmd(sql)
    
    for item in dict_row:
        if item['user'] == None:
                item['user'] = ''
    return render(request,'album.html',{
        'album':dict_row,
    })


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    
    return [dict(zip(columns, row))
        for row in cursor.fetchall()]

def run_sql_cmd(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return dictfetchall(cursor)

'''
def sql_join_table_example(request):
    sql = "select * from tracks_features as features INNER JOIN  ( \
            SELECT artist.name as artist, artist.id as artist_id, album.name as album_name, \
            album.img_url as img, album.id as album_id \
            FROM tracks_artist as artist \
            INNER JOIN tracks_album as album where album.artist_id = artist.id) M where M.album_id = features.album_id;" 
    dict_row = run_sql_cmd(sql)
    
    return HttpResponse(
                json.dumps(dict_row, sort_keys=False, indent=2), 
                content_type="application/json")  
'''