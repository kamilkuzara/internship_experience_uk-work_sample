"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name):
        self._name = name
        self._videos = []

    @property
    def name(self) -> str:
        """Returns the name of the playlist."""
        return self._name

    def contains(self, video_id):
        """ Checks whether the playlist already contains the specified video """
        for video in self._videos:
            if video.video_id == video_id:
                return True
        return False

    def add(self, video):
        self._videos.append(video)

    def remove(self,video):
        self._videos.remove(video)

    def is_empty(self):
        if len(self._videos) == 0:
            return True
        else:
            return False

    def get_videos(self):
        return self._videos

    def clear(self):
        self._videos.clear()
