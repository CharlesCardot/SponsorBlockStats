import numpy as np
import sponsorblock as sb

# Local
import general


def total_segment_duration(video, categories):
    """
    Calculate the total duration of all the segments
    in all the specified categories for the specified video
    """

    total_segment_duration = 0
    for category in categories:
        for segment in video[category]:
            total_segment_duration += float(segment["duration"])
    return round(total_segment_duration,3)


def content_percentage(video, categories):
    """
    Calculate the content percentage for a particular video using the formula
    (Total Video Length - SUM(Segment Lengths) / (Total Video Length)). This
    tells you how much of the video is actual content and not sponsored content,
    selfpromo content, ect.

        Parameters
        ----------
        video : Pandas series
            A row from a dataframe containing information about the video_id, video specific data (length, views, ect),
            and the segment information (how many segments, segment types, lengths, ect)
        categories : list
            The list of segment categories to consider
        
    """
    
    duration = total_segment_duration(video, categories)
    percentage = (video["length"] - duration) / video["length"]
    return "{:.3f}".format(round(percentage,3))


def segment_percentage(video, categories):
    """
    Calculate the segment percentage percentage for a particular video using the formula
    (SUM(Segment Lengths) / (Total Video Length)). This tells you how much
    of a video is made up of a particular segment.

        Parameters
        ----------
        video : Pandas series
            A row from a dataframe containing information about the video_id, video specific data (length, views, ect),
            and the segment information (how many segments, segment types, lengths, ect)
        categories : list
            The list of segment categories to consider
        
    """
    
    duration = total_segment_duration(video, categories)
    percentage = duration / video["length"]
    return "{:.3f}".format(round(percentage,3))


def calculate_all_stats(video, categories):
    """
    Calculate all the features for a single row from channel_df
    and return the updated row.
    """
    
    video["title_length_words"] = len(video["title"].split())
    video["title_length_characters"] = len(video["title"])
    video["title_capital_concentration"] = sum(1 for c in video["title"] if c.isupper())

    video["description_length_words"] = len(video["description"].split())
    video["description_length_characters"] = len(video["description"])
    video["description_length_lines"] = len(video["description"].split("\n"))
    video["description_links"] = video["description"].count("https")

    video["keyword_length_words"] = len(video["keywords"]) # Stored as a list
    video["keyword_length_characters"] = sum(len(word) for word in video["keywords"])

    data_total_dur = [total_segment_duration(video, [category]) 
        for category in categories]
    for key,dur in enumerate(data_total_dur):
        video[categories[key] + "_total_dur"] = dur

    data_total_num = [len(video[category]) 
        if not(video[category][0]["duration"] == 0 
            and len(video[category]) == 1) 
        else 0
        for category in categories]
    for key,num in enumerate(data_total_num):
        video[categories[key] + "_total_num"] = num

    return video