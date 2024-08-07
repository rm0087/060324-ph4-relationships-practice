#!/usr/bin/env python3

from config import app, db
from models import Artist, Album, Song
from faker import Faker
from datetime import datetime

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Artist.query.delete()
        Album.query.delete()
        Song.query.delete()

        print("Generating artists...")
        a1 = Artist(name="Meatloaf")
        a2 = Artist(name="The Strokes")
        a3 = Artist(name="")

        db.session.add_all([a1,a2])
        db.session.commit()

        print("Generating albums...")
        alb1 = Album(title="Bat Out of Hell", date_of_release=datetime.strptime('10-21-1977', '%m-%d-%Y'), artist_id=a1.id)
        alb2 = Album(title="Is This It", date_of_release=datetime.strptime('7-30-2001', '%m-%d-%Y'), artist_id=a2.id)
        alb3 = Album(title="Room on Fire", date_of_release=datetime.strptime('10-28-2003', '%m-%d-%Y'), artist_id=a2.id)

        db.session.add_all([alb1,alb2,alb3])
        db.session.commit()

        print("Generating songs...")
        s1 = Song(title="Bat Out of Hell", album_id=alb1.id)
        s2 = Song(title="Someday", album_id=alb2.id)
        s3 = Song(title="Reptillia", album_id=alb3.id)

        db.session.add_all([s1,s2,s3])
        db.session.commit()

        print("Seeding complete!")
