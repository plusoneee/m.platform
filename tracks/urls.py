from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('album/info/logs', views.music_record_logs, name='music_record_logs'),
    path('sql_example', views.sql_join_table_example, name="sql_join_table_example"),
    path('album/info/<slug:album_id>', views.ablum_info, name="album_info"),
    path('browser/artist', views.browser_artist, name="browser_artist"),
    path('artist/info/<slug:artist_id>', views.artist_info, name="artist_info"),
    path('add', views.add_to_playlist, name="add_playlist_from_id")
]