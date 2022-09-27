# SponsorBlockStats

This repo contains tools for visualization of SponsorBlock segments and their statistics across a given YouTube channel.

## Goals

The main purpose of this project was to familiarize myself with the Pandas python library and test out interactive plots in Matplotlib. Additionally, I wanted to create some tools for feature engineering that could be used in a future data science project.

## SponsorBlock

SponsorBlock is a [Chrome extension](https://sponsor.ajay.app/), created in July of 2019 by Ajay Ramachandran, which allows users to automatically skip sponsorship segments in YouTube videos. It relies on a crowdsourced approach where users submit segments to a database, which can be voted on by other users, with the highest voted segments being distributed to the general userbase

<p align="center">
	<img src="gifs/sponsorblock_example.gif" width="600" height="160" />
</p>


At the time of writing it has X active users, Y total user submited segments, and has saved people a upwards of Z years in wasted time. 


Support exists for multiple segments types including
- [Sponsor](https://youtu.be/siSP4X_94M0?t=157)
	- *Before we go any further I've got to tell you a little bit about this video's sponsor, Helix Sleep*
- [Unpaid/Self Promotion](https://youtu.be/HCXQzLbDrgs?t=1059)
	- *Merch Sales. We've got everything from pillows to t-shirts to plushies, to the upcoming backpack*
- [Interaction Reminder](https://youtu.be/qDMY_n5b348?t=321)
	- *If you are enjoying this video, than a sub would be elec*
- [Intermission/Intro Animation](https://youtu.be/9XozhdsYHDc?t=23)
	- *And we are off to a really good start here, as you can plainly see*
- [Endcards/Credits](https://youtu.be/-wpHszfnJns?t=1759)
	- *So are you like new around here, or...? (Made by Brian David Gilbert)*
- [Preview/Recap](https://www.youtube.com/watch?v=UOJ4IS0gSw0?t=0)
	- *Good Morning, or should I say goodnight. It is day 9 of trying to cross America starting from one penny to deliver it to Mr. Beast ...*
- [Music: Non-Music Section](https://www.youtube.com/watch?v=FLGCGc7sAUw?t=0)
	- *Welcome to match made, home of the perfect woman. Come on in and decide the girl of your dreams ... (Bella Poarch - Build a B\*tch)*
- [Point of Interest, Highlight](https://www.youtube.com/watch?v=7YuiFlhe8j4?t=140)
	- *Yes, can confirm, the major YouTuber that we sponsored to do a video about the LTT screwdriver, or featuring the LTT screwdriver, was Marques*
- [Filler](https://youtu.be/HCXQzLbDrgs?t=100)
	- *I make sure their shoots happen on time, and when they do I get ice-cream sandwhiches for everyone*

All of this comes together to provide an opensource, publicly validated database of information about hundreds of thousands of videos all across YouTube.

## Example: Linus Tech Tips

Linus Tech Tips is a popular channel and is well known for having multiple sponsored segments per video, as well as frequently promoting their merchandise.


- Total duration of all segments, broken down by type
<p align="center">
	<img src="images/StackedSegBar.svg" alt="Stacked Segment Bar Chart" width="750"/>
</p>



- Content percentage, calculated by $(\mathrm{Total \, Length}-\sum\mathrm{Segment \, Length}) / \mathrm{Total \, Length}$
<p align="center">
	<img src="images/ScatterContentPercentage.svg" alt="Scatter Plot, Content Percentage" width="750"/>
</p>


<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>length</th>      <th>views</th>      <th>title_length_words</th>      <th>title_length_characters</th>      <th>title_capital_concentration</th>      <th>description_length_words</th>      <th>description_length_characters</th>      <th>description_length_lines</th>      <th>description_links</th>      <th>keyword_length_words</th>      <th>keyword_length_characters</th>      <th>sponsor_total_dur</th>      <th>selfpromo_total_dur</th>      <th>interaction_total_dur</th>      <th>intro_total_dur</th>      <th>outro_total_dur</th>      <th>preview_total_dur</th>      <th>music_offtopic_total_dur</th>      <th>filler_total_dur</th>      <th>sponsor_total_num</th>      <th>selfpromo_total_num</th>      <th>interaction_total_num</th>      <th>intro_total_num</th>      <th>outro_total_num</th>      <th>preview_total_num</th>      <th>music_offtopic_total_num</th>      <th>filler_total_num</th>    </tr>  </thead>  <tbody>    <tr>      <th>count</th>      <td>40.000000</td>      <td>4.000000e+01</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.00000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.0</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.000000</td>      <td>40.0</td>      <td>40.000000</td>    </tr>    <tr>      <th>mean</th>      <td>2197.050000</td>      <td>1.517982e+06</td>      <td>7.800000</td>      <td>41.375000</td>      <td>9.175000</td>      <td>256.200000</td>      <td>2217.550000</td>      <td>55.100000</td>      <td>17.950000</td>      <td>9.525000</td>      <td>76.900000</td>      <td>83.436100</td>      <td>166.281275</td>      <td>1.016075</td>      <td>8.94730</td>      <td>11.130150</td>      <td>8.898350</td>      <td>0.0</td>      <td>88.085450</td>      <td>2.575000</td>      <td>3.850000</td>      <td>0.125000</td>      <td>0.750000</td>      <td>0.800000</td>      <td>0.175000</td>      <td>0.0</td>      <td>5.850000</td>    </tr>    <tr>      <th>std</th>      <td>3012.287613</td>      <td>5.812317e+05</td>      <td>2.409383</td>      <td>13.474929</td>      <td>4.254033</td>      <td>111.240373</td>      <td>731.483282</td>      <td>18.273983</td>      <td>8.227378</td>      <td>5.148998</td>      <td>47.256963</td>      <td>81.205994</td>      <td>422.711374</td>      <td>3.663252</td>      <td>9.42795</td>      <td>7.443707</td>      <td>24.373421</td>      <td>0.0</td>      <td>212.564205</td>      <td>1.972731</td>      <td>4.736925</td>      <td>0.404304</td>      <td>0.543021</td>      <td>0.464095</td>      <td>0.446496</td>      <td>0.0</td>      <td>12.037442</td>    </tr>    <tr>      <th>min</th>      <td>34.000000</td>      <td>5.743070e+05</td>      <td>3.000000</td>      <td>14.000000</td>      <td>1.000000</td>      <td>51.000000</td>      <td>316.000000</td>      <td>3.000000</td>      <td>1.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.00000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.0</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>0.0</td>      <td>0.000000</td>    </tr>    <tr>      <th>25%</th>      <td>816.250000</td>      <td>1.188210e+06</td>      <td>6.000000</td>      <td>32.000000</td>      <td>6.000000</td>      <td>231.750000</td>      <td>2166.750000</td>      <td>51.000000</td>      <td>15.750000</td>      <td>7.250000</td>      <td>44.750000</td>      <td>50.106000</td>      <td>9.863500</td>      <td>0.000000</td>      <td>0.00000</td>      <td>6.403500</td>      <td>0.000000</td>      <td>0.0</td>      <td>5.071250</td>      <td>2.000000</td>      <td>1.000000</td>      <td>0.000000</td>      <td>0.000000</td>      <td>1.000000</td>      <td>0.000000</td>      <td>0.0</td>      <td>1.000000</td>    </tr>    <tr>      <th>50%</th>      <td>1035.000000</td>      <td>1.394560e+06</td>      <td>7.500000</td>      <td>40.000000</td>      <td>9.000000</td>      <td>251.500000</td>      <td>2322.500000</td>      <td>58.000000</td>      <td>20.000000</td>      <td>11.000000</td>      <td>80.500000</td>      <td>68.803000</td>      <td>20.305000</td>      <td>0.000000</td>      <td>9.09200</td>      <td>12.898000</td>      <td>0.000000</td>      <td>0.0</td>      <td>20.922000</td>      <td>2.000000</td>      <td>2.000000</td>      <td>0.000000</td>      <td>1.000000</td>      <td>1.000000</td>      <td>0.000000</td>      <td>0.0</td>      <td>2.000000</td>    </tr>    <tr>      <th>75%</th>      <td>1589.000000</td>      <td>1.780632e+06</td>      <td>10.000000</td>      <td>54.250000</td>      <td>12.250000</td>      <td>287.750000</td>      <td>2499.750000</td>      <td>64.250000</td>      <td>22.000000</td>      <td>12.000000</td>      <td>105.250000</td>      <td>85.225250</td>      <td>51.382000</td>      <td>0.000000</td>      <td>9.40050</td>      <td>16.519000</td>      <td>0.000000</td>      <td>0.0</td>      <td>58.576500</td>      <td>3.000000</td>      <td>4.250000</td>      <td>0.000000</td>      <td>1.000000</td>      <td>1.000000</td>      <td>0.000000</td>      <td>0.0</td>      <td>5.250000</td>    </tr>    <tr>      <th>max</th>      <td>10348.000000</td>      <td>3.145553e+06</td>      <td>14.000000</td>      <td>70.000000</td>      <td>18.000000</td>      <td>577.000000</td>      <td>3851.000000</td>      <td>94.000000</td>      <td>38.000000</td>      <td>19.000000</td>      <td>165.000000</td>      <td>404.451000</td>      <td>2098.831000</td>      <td>18.610000</td>      <td>42.88300</td>      <td>26.279000</td>      <td>105.384000</td>      <td>0.0</td>      <td>1120.801000</td>      <td>10.000000</td>      <td>21.000000</td>      <td>2.000000</td>      <td>2.000000</td>      <td>2.000000</td>      <td>2.000000</td>      <td>0.0</td>      <td>73.000000</td>    </tr>  </tbody></table>

## Requirements
The only specialty packages required is the Python wrapper for the SponsorBlock API
- ```sponsorblock.py v0.2.2```. See <https://github.com/wasi-master/sponsorblock.py>.