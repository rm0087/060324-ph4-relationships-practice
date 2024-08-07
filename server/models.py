from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db

# Artist has many Songs
# Artist has many Albums
# Album has many Songs

class Artist(db.Model, SerializerMixin):
    
    __tablename__ = 'artist_table'
    # define a table name

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # arg 1 = type of value
    # arg x = primary_key=, nullable=, etc.

    albums = db.relationship('Album', back_populates='artist', cascade='all, delete-orphan')
    # arg 1 = name of the other class
    # arg 2 = back populates => the name of the method in the other class pointing to this class
    # arg 3 = deletes albums for artist when artist is deleted

    songs = association_proxy('albums', 'songs')
    # arg 1 = relatiionship name we're going through
    # arg 2 = the relationship that brings us to our final destination

    serialize_rules = ('-artist.albums',)
    ## use SerializerMixin to filter out related attributes from other classes to avoid infinite loops

    #### TO SET-UP TABLES ####
        ## flask db init
        ## flask db migrate -m "message here"
        ## flask db upgrade

    ## flask shell
    ## >> db.session.add(variable_to_add)
    ## >> db.session.add_all([x1, x2, x3]) ## add multiple variables in list form
    ## >> db.session.commit()

class Album(db.Model, SerializerMixin):

    __tablename__ = 'album_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date_of_release = db.Column(db.DateTime)

    artist_id = db.Column( db.Integer, db.ForeignKey('artist_table.id'))

    artist = db.relationship('Artist', back_populates='albums')

    songs = db.relationship('Song', back_populates='album', cascade='all, delete-orphan')

    serialize_rules = ('-artist.albums', '-songs.album')
    

class Song(db.Model, SerializerMixin):
    
    __tablename__ = "song_table"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    
    album_id = db.Column(db.Integer, db.ForeignKey('album_table.id'))

    album = db.relationship('Album', back_populates='songs')

    artist = association_proxy('album', 'artist')

    serialize_rules = ('-album.songs',)