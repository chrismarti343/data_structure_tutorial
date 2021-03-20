

class Playlist_app:

    def __init__(self):
        """
        Initialize an empty list, this is the list where the song will be at
        """
        self.queue = []

    class Music:

        def __init__(self,song,album,genre):

            """
            Starting the playlist
            """
            self.song = song
            self.album = album
            self.genre = genre

        def __str__ (self):
            """
            Return a string of the song with album and genre
            """
            return self.song + " (" +self.album + "), "  + self.genre


    def add_new_song(self):

        """
        Prompt the user the song, album and genre, and they are appended to the queue list.
        """

        song = input("Song name: ")
        album = input("Album: ")
        genre = input("Genre: ")
        print('---------------------')

        music = Playlist_app.Music(song,album,genre)
        self.queue.append(music)

    def play_song(self):
        """
        This function Dequeu the song and display the song that is playing right now
        """

        # Check if there are not songs in the list
        if len(self.queue) == 0:
            return 'No songs in list'

        else:

            # Remove the song from the Queue
            music = self.queue[0]
            del self.queue[0]
            return music


print('Test1')
play = Playlist_app()
play.add_new_song()
play.add_new_song()
print('Now playing: ', play.play_song())

print('\n')
print('==========================')
print('Test2')
play = Playlist_app()
print('Now playing: ', play.play_song())

print('\n')
print('==========================')
print('Test3')
play = Playlist_app()
play.add_new_song()
play.add_new_song()
play.play_song()
print('Now playing: ', play.play_song())


print('\n')
print('==========================')
print('Test4')
play = Playlist_app()
play.add_new_song()
play.add_new_song()
play.play_song()
play.play_song()
print('Now playing: ', play.play_song())


