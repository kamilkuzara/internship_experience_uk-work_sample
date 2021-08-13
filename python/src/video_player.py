"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random
import math

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlists = []
        self._currently_playing = None
        self._paused = None

    def get_video(self, video_id):
        return self._video_library.get_video(video_id)

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        descriptions = []
        for video in self._video_library.get_all_videos():
            descriptions.append(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")
        descriptions.sort()

        for item in descriptions:
            print(item)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self.get_video(video_id)
        if video == None:
            print("Cannot play video: Video does not exist")
        elif self._currently_playing == None:
            print( f"Playing video: {video.title}" )
            self._currently_playing = video
            self._paused = False
        else:
            print( f"Stopping video: {self._currently_playing.title}" )
            print( f"Playing video: {video.title}" )
            self._currently_playing = video
            self._paused = False

    def stop_video(self):
        """Stops the current video."""

        if self._currently_playing == None:
            print( "Cannot stop video: No video is currently playing" )
        else:
            print( f"Stopping video: {self._currently_playing.title}" )
            self._currently_playing = None
            self._paused = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        index = math.floor(random.random() * len(self._video_library.get_all_videos()))
        video = self._video_library.get_all_videos()[index]

        if self._currently_playing == None:
            print( f"Playing video: {video.title}" )
            self._currently_playing = video
            self._paused = False
        else:
            print( f"Stopping video: {self._currently_playing.title}" )
            print( f"Playing video: {video.title}" )
            self._currently_playing = video
            self._paused = False

    def pause_video(self):
        """Pauses the current video."""

        if self._currently_playing == None:
            print( "Cannot pause video: No video is currently playing" )
        elif self._paused == True:
            print( f"Video already paused: {self._currently_playing.title}" )
        else:
            print( f"Pausing video: {self._currently_playing.title}" )
            self._paused = True

    def continue_video(self):
        """Resumes playing the current video."""

        if self._currently_playing == None:
            print( "Cannot continue video: No video is currently playing" )
        elif self._paused == False:
            print( f"Cannot continue video: Video is not paused" )
        else:
            print( f"Continuing video: {self._currently_playing.title}" )
            self._paused = False

    def show_playing(self):
        """Displays video currently playing."""

        if self._currently_playing == None:
            print( "No video is currently playing" )
        else:
            video = self._currently_playing
            output = f"Currently playing: {video.title} ({video.video_id}) [{' '.join(video.tags)}]"
            if self._paused == True:
                output += " - PAUSED"
            print(output)

# ------------------------------------------------------------------------------------------------------

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_name = playlist_name.replace(" ", "_")

        if self.get_playlist(playlist_name) != None:
            print("Cannot create playlist: A playlist with the same name already exists")
            return

        self._playlists.append(Playlist(playlist_name))
        print( f"Successfully created new playlist: {playlist_name}" )

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        # check if both the playlist and the video exist
        playlist = self.get_playlist(playlist_name)
        video = self.get_video(video_id)

        if playlist == None:
            print( f"Cannot add video to {playlist_name}: Playlist does not exist" )
            return

        if video == None:
            print( f"Cannot add video to {playlist_name}: Video does not exist" )
            return

        # check if the video not already in the playlist
        if playlist.contains(video_id):
            print( f"Cannot add video to {playlist_name}: Video already added" )
            return

        # finally, add the video to the playlist
        playlist.add(video)
        print( f"Added video to {playlist_name}: {video.title}" )

    def get_playlist(self, playlist_name):
        for playlist in self._playlists:
            if(playlist.name.lower() == playlist_name.lower()):
                return playlist
        return None

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self._playlists) == 0:
            print( "No playlists exist yet" )
            return

        names = []
        for playlist in self._playlists:
            names.append(playlist.name)

        names.sort(key = str.lower)

        print("Showing all playlists:")
        for name in names:
            print(f"  {name}")


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        # check if playlist exists
        playlist = self.get_playlist(playlist_name)
        if playlist == None:
            print( f"Cannot show playlist {playlist_name}: Playlist does not exist" )
            return

        # check if playlist not empty
        if playlist.is_empty():
            print( f"Showing playlist: {playlist_name}" )
            print( "  No videos here yet" )
            return

        # finally, show the videos
        videos = playlist.get_videos()
        print(f"Showing playlist: {playlist_name}")
        for video in videos:
            print(f"  {video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        # check if both the playlist and the video exist
        playlist = self.get_playlist(playlist_name)
        video = self.get_video(video_id)

        if playlist == None:
            print( f"Cannot remove video from {playlist_name}: Playlist does not exist" )
            return

        if video == None:
            print( f"Cannot remove video from {playlist_name}: Video does not exist" )
            return

        # check if the video is in the playlist
        if not playlist.contains(video_id):
            print( f"Cannot remove video from {playlist_name}: Video is not in playlist" )
            return

        # remove the video from the playlist
        playlist.remove(video)
        print( f"Removed video from {playlist_name}: {video.title}" )

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # check if the playlist exists
        playlist = self.get_playlist(playlist_name)

        if playlist == None:
            print( f"Cannot clear playlist {playlist_name}: Playlist does not exist" )
            return

        # clear the playlist
        playlist.clear()
        print( f"Successfully removed all videos from {playlist_name}" )

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # check if playlist exists
        playlist = self.get_playlist(playlist_name)
        if playlist == None:
            print( f"Cannot delete playlist {playlist_name}: Playlist does not exist" )
            return

        # delete the playlist
        self._playlists.remove(playlist)
        print( f"Deleted playlist: {playlist_name}" )

# ------------------------------------------------------------------------------------------------------

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()

        # filter out the videos that don't contain the search term
        filtered = []
        for video in videos:
            if video.title.lower().find(search_term.lower()) != -1:
                filtered.append(video)

        # if no results found, quit
        if len(filtered) == 0:
            print(f"No search results for {search_term}")
            return

        # format the info for printing
        formatted = []
        for video in filtered:
            formatted.append(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

        # sort alphabetically
        formatted.sort(key = str.lower)

        print(f"Here are the results for {search_term}:")
        i = 0
        while i < len(formatted):
            print(f"  {i+1}) {formatted[i]}")
            i += 1

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")

        # read the response and act upon it
        try:
            index = int(input()) - 1
            if index >= 0 and index < len(formatted):
                requested_video_id = formatted[index][formatted[index].find("(") + 1 : formatted[index].find(")")]
                self.play_video(requested_video_id)
        except ValueError:
            """ Do nothing """

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()

        # filter out the videos whose tag lists don't contain the search tag
        filtered = []
        for video in videos:
            should_append = False
            for tag in video.tags:
                if tag.lower() == video_tag.lower():
                    should_append = True
            if should_append:
                filtered.append(video)

        # if no results found, quit
        if len(filtered) == 0:
            print(f"No search results for {video_tag}")
            return

        # format the info for printing
        formatted = []
        for video in filtered:
            formatted.append(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

        # sort alphabetically
        formatted.sort(key = str.lower)

        print(f"Here are the results for {video_tag}:")
        i = 0
        while i < len(formatted):
            print(f"  {i+1}) {formatted[i]}")
            i += 1

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")

        # read the response and act upon it
        try:
            index = int(input()) - 1
            if index >= 0 and index < len(formatted):
                requested_video_id = formatted[index][formatted[index].find("(") + 1 : formatted[index].find(")")]
                self.play_video(requested_video_id)
        except ValueError:
            """ Do nothing """

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
