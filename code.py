from collections import OrderedDict, deque

class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.recently_played = OrderedDict()

    def play_song(self, user, song):
        if user not in self.recently_played:
            self.recently_played[user] = deque(maxlen=self.capacity)
        self.recently_played[user].append(song)

    def get_recently_played(self, user):
        if user in self.recently_played:
            return list(self.recently_played[user])
        else:
            return []


if __name__ == "__main__":
    store = RecentlyPlayedStore(5)

    store.play_song("User1", "Song1")
    store.play_song("User1", "Song2")
    store.play_song("User1", "Song3")


    store.play_song("User2", "Song4")
    store.play_song("User2", "Song5")

    print("Recently played songs for User1:", store.get_recently_played("User1"))

    print("Recently played songs for User2:", store.get_recently_played("User2"))
