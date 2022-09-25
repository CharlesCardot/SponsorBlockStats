import pytube

import numpy as np
import pandas as pd

# Local
import video_stats

def collapse_segment_lists(channel_df, method, categories):
    """
    Collapse the segment data contained in each segment list into
    single values (ex: Total length of all segments of
    a single type, or total number of a single type of segment.)

    Parameters
        ----------
        channel_df : Pandas DataFrame
            The pandas DataFrame for the entire channel, with each row being a particular
            video, and having the format: video_id, video specific data (length, views, ect),
            segment information (how many segments, segment types, lengths, ect)
        method : str
            The method to be used for performing the segment collapse.
              'segment_dur' : Use the total duration of the segments
              'segment_num' : Use the total number of segments
        categories : list
            The list of segment categories to consider
    """

    if method == "segment_dur":
        data = [
            [
                video_stats.total_segment_duration(channel_df.iloc[i], [category]) 
            for category in categories
            ] 
        for i in range(len(channel_df))
        ]
    elif method == "segment_num":
        data = [
            [
                len(channel_df.iloc[i][category]) 
                if not(channel_df.iloc[i][category][0]["duration"] == 0 
                    and len(channel_df.iloc[i][category]) == 1) 
                else 0
                for category in categories 
            ] 
        for i in range(len(channel_df))
        ]
    return data

def channel_content_percentage(channel_df, categories):
    """
    Calculate the content percentage for every video on the channel

    Parameters
        ----------
        channel_df : Pandas DataFrame
            The pandas DataFrame for the entire channel, with each row being a particular
            video, and having the format: video_id, video specific data (length, views, ect),
            segment information (how many segments, segment types, lengths, ect)
        categories : list
            The list of segment categories to consider
    """

    data = [
        video_stats.content_percentage(channel_df.iloc[i], categories) for i in range(len(channel_df))
    ]

    return data
    
