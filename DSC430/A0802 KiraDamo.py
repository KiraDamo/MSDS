#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#June 1st
#https://youtu.be/9T-l8pukHyY

import pandas as pd

#loads artist and tracks tsv files
artists_df = pd.read_csv('artists.tsv', sep='\t')
tracks_df = pd.read_csv('tracks.tsv', sep='\t')

#Identify and print the name and genre of the artist with maximum # of followers
most_followed_artist = artists_df.loc[artists_df['followers'].idxmax()]
print('Artist with the most followers: ', most_followed_artist['name'], most_followed_artist['genres'])
                                      
#Identity and print name of the most productive artist in terms of # of tracks performed
tracks_df['id_artists'] = tracks_df['id_artists'].str.split(', ') 
explode_tracks = tracks_df.explode('id_artists') #split co-artists in a list and reassigns songs to each artist
num_tracks = explode_tracks['id_artists'].value_counts()
most_productive_artist_id = num_tracks.idxmax()
most_productive_artist = artists_df[artists_df['id'] == most_productive_artist_id].iloc[0]
print('Most productive artist: ', most_productive_artist['name'])

#return df that has 3 columns: genre, total n, av. followers
def summarize_genres(genres):
    genre_data=[]
    for g in genres:
        mask = artists_df['genres'].str.contains(g, case=False, na=False)
        genre_artists = artists_df[mask]

        genre_data.append({
            'genre': g,
            'total N': len(genre_artists),
            'Av. followers': genre_artists['followers'].mean()
        })

    return pd.DataFrame(genre_data)

genre_test = ['pop', 'hip hop', 'rock', 'metal', 'jazz', 'blues', 'country',
'folklore']
summarize_genres(genre_test)

def get_genre_variants(genre):
    genre_set = set()

    for g in artists_df['genres']:
        genre_list = g.split(', ')
        for word in genre_list:
            if genre.lower() in word.lower():
                genre_set.add(word.strip())

    return sorted(genre_set)

get_genre_variants('jazz')

def summarize_artist_performance(name):
    'function provides summary of artists performance'

    artist_row = artists_df[artists_df['name'].str.lower() == name.lower()]
    if artist_row.empty:
        return
    artist_id = artist_row.iloc[0]['id']
    
    #amount of tracks by artist
    artist_tracks = explode_tracks[explode_tracks['id_artists'] == artist_id]
    total_tracks = len(artist_tracks)
    
    artist_counts_per_track = explode_tracks.groupby('id')['id_artists'].count()

    #indicates whether a song is a solo or collab
    solo_ids = artist_counts_per_track[artist_counts_per_track == 1].index
    collab_ids = artist_counts_per_track[artist_counts_per_track > 1].index

    #artist's tracks that are either solo or collabs
    solo_tracks = artist_tracks[artist_tracks['id'].isin(solo_ids)]
    collab_tracks = artist_tracks[artist_tracks['id'].isin(collab_ids)]

    #the popularity of the artist's tracks (all, collab, solo)
    avg_total_pop = artist_tracks['popularity'].mean()
    avg_total_pop_collab = collab_tracks['popularity'].mean()
    avg_total_pop_solo = solo_tracks['popularity'].mean()

    #gathers all track_ids from collabs and does not accept duplicates
    collab_track_ids = collab_tracks['id'].unique()
    collaborators = explode_tracks[
    (explode_tracks['id'].isin(collab_track_ids)) &
    (explode_tracks['id_artists'] != artist_id)
    ] #checks if each row returns True and analyzes who collabed with artist on the track
    unique_collaborators = collaborators['id_artists'].nunique() #collab artists stored
 
    print(f"Artist: {name}")
    print(f"Total number of tracks: {total_tracks}")
    print(f"Number of solo tracks: {len(solo_tracks)}")
    print(f"Number of collaborative tracks: {len(collab_tracks)}")
    print(f"Average popularity (total): {avg_total_pop:.2f}")
    print(f"Average popularity (solo): {avg_total_pop_solo:.2f}")
    print(f"Average popularity (collaborative): {avg_total_pop_collab:.2f}")
    print(f"Number of collaborators: {unique_collaborators}")

summarize_artist_performance("Michael Jackson")

