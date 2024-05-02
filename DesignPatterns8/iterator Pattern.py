from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass


class Playlist(ABC):
    @abstractmethod
    def createIterator(self):
        pass

    @abstractmethod
    def addSong(self, song):
        pass


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class PlaylistImpl(Playlist):
    def __init__(self):
        self.songs = []

    def createIterator(self):
        return PlaylistIterator(self)

    def addSong(self, song):
        self.songs.append(song)


class PlaylistIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def hasNext(self):
        return self.index < len(self.playlist.songs)

    def next(self):
        if self.hasNext():
            song = self.playlist.songs[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration


if __name__ == "__main__":
    my_playlist = PlaylistImpl()

    my_playlist.addSong(Song("Rock Back", "Simon"))
    my_playlist.addSong(Song("Kuz", "Sadraddin"))
    my_playlist.addSong(Song("NEW MAGIC WAND", "Tyler, The Creater"))

    iterator = my_playlist.createIterator()
    while iterator.hasNext():
        song = iterator.next()
        print(f"Now playing: {song.title} by {song.artist}")
