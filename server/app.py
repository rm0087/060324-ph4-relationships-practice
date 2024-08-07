#!/usr/bin/env python3

from flask import request
from config import app, db
from models import Artist, Album, Song

@app.get('/')
def index():
    return "Hello world"

@app.get('/artists') ## ARTISTS ##################################################################################
def all_artists():
    #1. Get all artists from the db
    artist_list = Artist.query.all()

    #2. Convert into dictionaries
    artist_dicts = [artist.to_dict() for artist in artist_list]

    #3. Send a response to the client
    return artist_dicts, 200

@app.get('/artists/<int:id>')
def get_artist(id):
    #1. SQLAlchemy query to get an artist by their id
    found_artist = Artist.query.where(Artist.id == id).first()
    
    #2. Conditional if the artist exists
    if found_artist:
        return found_artist.to_dict(), 200
    else:
        return {'error': "Not found"}, 404

@app.post('/artists')
def create_artist():
    #1. Get the information from the body/json
    data = request.json

    try:
        #2. Make a new artist
        new_artist = Artist(name=data['name'])

        #3.Put it in the database
        db.session.add(new_artist)
        db.session.commit()

        #4. Return the new artist to the client
        return new_artist.to_dict(), 201
    except:
        return {'error': 'invalid data'}, 400

@app.patch('/artists/<int:id>')
def update_artist(id):
    #1. Get the artist
    found_artist = Artist.query.where(Artist.id == id).first()

    #2. Conditional for getting/not getting the artist
    if found_artist:
        data=request.json
        try:
            for key in data:
                setattr( found_artist, key, data[key])
            db.session.add(found_artist)
            db.session.commit()

            return found_artist.to_dict(),202
        
        except Exception as e:
            return {'error': str(e)}, 400
    
    else:
        return {'error': 'not found'}, 404
    
@app.delete('/artists/<int:id>')
def delete_song(id):
    
        found_artist = Artist.query.where(Artist.id == id).first()

        if found_artist:
            db.session.delete(found_artist)
            db.session.commit()
            return {}, 204
        else:
            return {'error': 'Not found'},400
   

    
@app.get('/songs/') ## SONGS ##################################################################################
def all_songs():
    song_list = Song.query.all()
    
    song_dicts = [song.to_dict() for song in song_list]

    return song_dicts, 200

@app.get('/songs/<int:id>')
def get_song(id):
    found_song = Song.query.where(Song.id == id).first()
    if found_song:
        return found_song.to_dict(), 200
    else:
        return {'error': 'Not found'}, 404
    
@app.post('/songs')
def create_song():
    data = request.json

    try:
        new_song = Song(title=data['title'], album_id=data['album_id'])

        db.session.add(new_song)
        db.session.commit()

        return new_song.to_dict(), 201
    except:
        return {'error': 'invalid data'}, 400
    
@app.patch('/songs/<int:id>')
def update_song(id):
    found_song = Song.query.where(Song.id == id).first()

    try:
        if found_song:
            data = request.json
            for key in data:
                setattr( found_song, key, data[key])
            db.session.add(found_song)
            db.session.commit()
            return found_song.to_dict(), 202
        else:
            return {'error': 'song not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 400
    



@app.get('/albums') ## ALBUMS ##################################################################################
def all_albums():
    album_list = Album.query.all()
    album_dicts = [album.to_dict() for album in album_list]
    return album_dicts, 200

@app.get('/albums/<int:id>')
def get_album(id):
    found_album = Album.query.where(Album.id == id).first()

    if found_album:
        return found_album.to_dict(), 200
    else:
        return {'error': 'Not found'}


if __name__ == '__main__':
    app.run(port=5555, debug=True)
