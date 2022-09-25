import numpy as np
import pandas as pd
import sponsorblock as sb
import matplotlib.pyplot as plt

# Local
import general
import video_stats
import channel_stats

plt.rcParams['font.sans-serif'] = "Times New Roman"
plt.rcParams['font.family'] = "sans-serif"

COLORS = ["tab:blue","tab:orange","tab:green","tab:red","tab:purple","tab:pink","tab:gray","tab:olive","tab:brown"]
COLORS_DICT = {sb.utils.ALL_CATEGORIES[i]: COLORS[i] for i in range(len(COLORS))}

def make_channel_plot(channel_df, x_axis, plot_type, include = [], exclude = [], video_num_max = 40, **kwargs):
    """
    Make a plot vizualizing data over the whole channel.

        Parameters
        ----------
        channel_df : Pandas DataFrame
            Cleaned data for a particular channel, with entires for all segment types
        x_axis : Pandas Series
            One of the column labels for channel_df, to be the x axis of the plot
        plot_type : str
            The type of plot to be generated (ex: StackedSegBar)
        include : list, optional
            The list of segment categories to plot
        exclude : list, optional
            The list of segment categories to NOT plot
        video_num_max: int, optional
            Maximum number of videos from a channel to include in the bar
            chart. Defaults to most recently released videos.
        **kwargs : dict
            method : str, optional
            {"segment_num", "segment_dur"} Defines whether to use
            the number of segments of a specific type, or the 
            total duration (in seconds) of all segments of a specific type
        
    """

    if len(channel_df) > video_num_max:
        channel_df = channel_df.head(video_num_max)
    
    def date_from_datetime(datetime):
        return datetime.date()

    indices = channel_df[x_axis]
    if x_axis == "publish_date":
        indices = indices.apply(date_from_datetime)
    
    global categories
    categories = general.get_categories(include, exclude)
    colors = [COLORS_DICT[category] for category in categories]
    x_ticks = np.arange(0, min(len(channel_df),video_num_max), 1)

    if "title" in kwargs.keys():
        title = kwargs["title"]
    else:
        print("add a 'title' argument to set the plot title")
        title = "CHANNEL_NAME"
    if "tight_layout_padding" in kwargs.keys():
        tight_layout_padding = kwargs["tight_layout_padding"]
    else:
        tight_layout_padding = 1.08 # Default matplotlib value

    ## Stacked Segment Bar Chart ##
    if plot_type == "StackedSegBar":

        if kwargs["method"]:
            method = kwargs["method"]
        else:
            raise TypeError("missing required positional argument: 'method'")

        data = channel_stats.collapse_segment_lists(
            channel_df, method, categories)

        if method == "segment_dur":
            ylabel = "Duration of Segments (seconds)"
        elif method == "segment_num":
            ylabel = "Number of Segments"
            
        data_df = pd.DataFrame(data, index=indices, columns=categories)     
        fig, ax = plt.subplots(figsize=(8,6))
        width = 0.5
        
        for key, category in enumerate(categories):
            if key == 0:
                ax.bar(x_ticks, data_df[category], label=category, 
                    width=width, color=COLORS_DICT[category])
                bottom = data_df[category]
            else:
                ax.bar(x_ticks, data_df[category], bottom=bottom, 
                    width=width, label=category, color=COLORS_DICT[category])
                bottom += data_df[category]

        ax.set_xticks(x_ticks, indices, fontsize=10, rotation = 80)
        ax.tick_params(axis='y', which='major', labelsize=15)
        
        ymin, ymax = ax.get_ylim()
        ax.set_ylim(ymin,ymax*1.2)

        plt.margins(x=0.01,tight=True)

        ax.legend(fancybox=True, fontsize=13, loc=9, ncol=int((len(categories)+1) / 2), 
        handletextpad=0.2, columnspacing=1.0, shadow=True)

        plt.tight_layout(pad=tight_layout_padding)
        
    ## Content Percentage Scatter Plot ##
    if plot_type == "ScatterContentPercentage":
        
        from matplotlib.widgets import CheckButtons

        data = channel_stats.channel_content_percentage(channel_df, categories)
        data_df = pd.DataFrame(data, index=indices, columns=["percentage"])
        fig, ax = plt.subplots(figsize=(8,6))

        fig.subplots_adjust(right=0.82)
        fig.subplots_adjust(bottom=0.20)
        
        ylabel = "Content Percentage"

        l, = ax.plot(x_ticks, [float(x) for x in data_df["percentage"].tolist()], 
            ms=5, color='tab:blue', marker='o', ls='')
        ax.set_xticks(x_ticks, indices, fontsize=10, rotation = 80)
        ax.tick_params(axis='y', which='major', labelsize=15)
        ax.set_ylim(0,1.05)

        axcolor = 'lightgoldenrodyellow'
        rax = fig.add_axes([0.83, 0.5, 0.15, 0.30], facecolor=axcolor)
        actives = [True for i in categories]
        box_text = categories
        radio = CheckButtons(rax, box_text, actives)

        def redrawfunc(label):
            
            global categories
            temp_categories = [categories[i] for i in range(len(radio.lines)) if radio.lines[i][0].get_visible()]
            
            data = channel_stats.channel_content_percentage(channel_df, temp_categories)
            data_df = pd.DataFrame(data, index=indices, columns=["percentage"])
            
            l.set_ydata([float(x) for x in data_df["percentage"].tolist()])
            plt.draw()
                
        radio.on_clicked(redrawfunc)

    
    # ### Interactive
    # # '%matplotlib widget' required
    ax.set_picker(10)
    def on_click(event):
        ax = event.inaxes
        x = event.xdata
        try:
            labels = ax.get_xticklabels()
            index = int(x.round())
            label = labels[index].get_text()
            video_id = channel_df.iloc[index]["video_id"]
            url = "https://www.youtube.com/watch?v=" + video_id
            
            print("Opening video " + url + ", because you clicked on " + str(label))
            
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            pass
    
    fig.canvas.callbacks.connect('button_press_event', on_click)
    ###

    ax.set_xlabel(x_axis,fontsize=20)
    ax.set_ylabel(ylabel,fontsize=20)
    ax.set_title(title,fontsize=20)
    
    plt.show()
    
        