import os
import pytube

import pandas as pd
import sponsorblock as sb


def get_categories(include = [], exclude = []):
    """
    Return the appropriate list of categories based on whether include
    or exclude was specified.

        Parameters
        ----------
        include : list, optional
            The list of segment categories to include when calculating the content density
        exclude : list, optional
            The list of segment categories to NOT include when calculating the content density

        Notes
        ----------
        There is no reason to define both 'include' and 'exclude'. From basic set theory,
        you only need one or the other to entirely define the set you care about.
        
    """

    include_invalid = [x for x in include if x not in sb.utils.ALL_CATEGORIES]
    exclude_invalid = [x for x in exclude if x not in sb.utils.ALL_CATEGORIES]
    if include_invalid or exclude_invalid:
        raise ValueError("The categorie(s) '" + "', '".join(include_invalid + exclude_invalid) + "' are invalid")

    if not(include) and not(exclude):
        raise TypeError("Category lists 'include' or 'exclude' arguments must be defined")

    if include and exclude:
        warning = """Please define only 'include' or 'exclude'. Any
        categories not included in one list will automatically be considered
        as apart of the other."""
        # Stops warnings from printing out out weird
        warning = " ".join([chunk.strip() for chunk in warning.split("\n")])
        raise ValueError(warning)

    if set(exclude) == set(sb.utils.ALL_CATEGORIES):
        print("Warning! You are excluding every category!")
        return "{:.3f}".format(0)

    if include:
        categories = [x for x in sb.utils.ALL_CATEGORIES if x in include]
    elif exclude:
        categories = [x for x in sb.utils.ALL_CATEGORIES if x not in exclude]
    
    return categories


def get_video_rawdata(client, url):
    """
    Return the, video id, raw pytube Youtube object, and SponsorBlock skip segment objects
    for later processing

        Parameters
        ----------
        client : instance of SponsorBlock Client class
            client = sb.Client()
        url : str
            Youtube video url
        
    """

    try:
        data_chunk = [vars(x) for x in client.get_skip_segments(url)]
        for key,val in enumerate(data_chunk):
            val["youtube_object"] = pytube.YouTube(url)
            val["video_id"] = pytube.extract.video_id(url)
            data_chunk[key] = val
        return data_chunk
    except Exception as e:
        # If 404 Not Found, this is because no one has submited
        # segments for this particular video. It is still a valid
        # data point, so we just fill it will 'empty' segment info.
        if str(e) == "Not Found: 404 Not Found":
            data_chunk = [
                vars(sb.models.Segment(
                    category = category,
                    start = 0,
                    end = 0,
                    duration = 0
                )) for category in sb.utils.ALL_CATEGORIES
            ]
            for key,val in enumerate(data_chunk):
                val["youtube_object"] = pytube.YouTube(url)
                val["video_id"] = pytube.extract.video_id(url)
                data_chunk[key] = val
            return data_chunk
        else:
            print(url, e)

def get_rawdata(urls, update = False):
    """
    Return an unprocessed database with all the info for each url
    in 'urls'. Database is stored as a pickled object because it 
    contains pytube instances

        Parameters
        ----------
        client : list
            List of urls that you want to get out of the database
        update : bool, optional
            Force the database to grab new data for every url.
            This is usefull if more segments have recently been
            added to the videos you want to include in your
            dataset.
        
    """

    import pickle

    data = []
    client = sb.Client()
    if os.path.exists("raw_database.pickle"):
        with open("raw_database.pickle", 'rb') as pickle_file:
            raw_database = pickle.load(pickle_file)
        if update:
            for url in urls:
                data_chunk = get_video_rawdata(client=client,url=url)
                if (data_chunk):
                    data = data + data_chunk
        else:
            for url in urls:
                if pytube.extract.video_id(url) not in pd.DataFrame(raw_database)["video_id"].tolist():
                    print(url)
                    data_chunk = get_video_rawdata(client=client,url=url)
                    if (data_chunk):
                        raw_database = raw_database + data_chunk
            data = raw_database            
    else:
        for url in urls:
            data_chunk = get_video_rawdata(client=client,url=url)
            if (data_chunk):
                data = data + data_chunk

    with open("raw_database.pickle", "wb") as f:
        pickle.dump(data,f)
    
    data = [single_data for single_data in data 
        if single_data["video_id"] in [pytube.extract.video_id(url) for url in urls]]
    return data    
        

