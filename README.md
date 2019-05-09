## Intro
This project is for a music player web service by Python Django, and all of data in Database(MySQL) is from [spotify api](https://developer.spotify.com/documentation/web-api/). 

![](https://github.com/plusoneee/m.platform/blob/master/other/img/sample.gif)

### Dependencies
Python3, MySQL, MongoDB.

### Python3 Requirments
Install Python3 Requirments from `requirements.txt`, just run command:
```
pip install -r requirements.txt
```
## Before the start
Note:
* You must prepare `mp3` file in `staic/` by yourself.
* Data table format please refer to [model.py](https://github.com/plusoneee/m.platform/blob/master/tracks/models.py)

### Database Settings
Edit the file `web/my.example.cnf`, save as `web/my.cnf`, Run:
```
cp web/my.example.cnf web/my.cnf
```

### Model Migration
```
python manage.py makemigrations tracks
python manage.py migrate
```

## RUN
```
python manage.py runserver
```

