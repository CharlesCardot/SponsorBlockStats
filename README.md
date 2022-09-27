# SponsorBlockStats

This repo contains tools for visualization of SponsorBlock segments and their statistics across a given YouTube channel.

## Goals

The main purpose of this repo was to familiarize myself with the Pandas python library and to get some experience with interactive plots in Matplotlib. Additionally, I wanted to create some tools for feature engineering that could potentially be used in a future data science project.

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

<p align="center">
	<img src="images/StackedSegBar.svg" alt="Stacked Segment Bar Chart" width="750"/>
</p>

<p align="center">
	<img src="images/ScatterContentPercentage.svg" alt="Scatter Plot, Content Percentage" width="750"/>
</p>


<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>length</th>\n      <th>views</th>\n      <th>title_length_words</th>\n      <th>title_length_characters</th>\n      <th>title_capital_concentration</th>\n      <th>description_length_words</th>\n      <th>description_length_characters</th>\n      <th>description_length_lines</th>\n      <th>description_links</th>\n      <th>keyword_length_words</th>\n      <th>keyword_length_characters</th>\n      <th>sponsor_total_dur</th>\n      <th>selfpromo_total_dur</th>\n      <th>interaction_total_dur</th>\n      <th>intro_total_dur</th>\n      <th>outro_total_dur</th>\n      <th>preview_total_dur</th>\n      <th>music_offtopic_total_dur</th>\n      <th>filler_total_dur</th>\n      <th>sponsor_total_num</th>\n      <th>selfpromo_total_num</th>\n      <th>interaction_total_num</th>\n      <th>intro_total_num</th>\n      <th>outro_total_num</th>\n      <th>preview_total_num</th>\n      <th>music_offtopic_total_num</th>\n      <th>filler_total_num</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>101.000000</td>\n      <td>1.010000e+02</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.0</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.000000</td>\n      <td>101.0</td>\n      <td>101.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>1856.930693</td>\n      <td>1.666854e+06</td>\n      <td>8.544554</td>\n      <td>46.564356</td>\n      <td>8.851485</td>\n      <td>231.613861</td>\n      <td>2031.336634</td>\n      <td>50.118812</td>\n      <td>16.782178</td>\n      <td>9.762376</td>\n      <td>85.217822</td>\n      <td>73.114950</td>\n      <td>159.727673</td>\n      <td>0.738871</td>\n      <td>7.931287</td>\n      <td>10.475594</td>\n      <td>7.952713</td>\n      <td>0.0</td>\n      <td>83.961149</td>\n      <td>2.039604</td>\n      <td>3.099010</td>\n      <td>0.089109</td>\n      <td>0.623762</td>\n      <td>0.782178</td>\n      <td>0.168317</td>\n      <td>0.0</td>\n      <td>6.178218</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>2629.378121</td>\n      <td>8.742076e+05</td>\n      <td>2.471942</td>\n      <td>13.012621</td>\n      <td>3.835065</td>\n      <td>114.004734</td>\n      <td>818.606319</td>\n      <td>20.135187</td>\n      <td>8.156720</td>\n      <td>5.725641</td>\n      <td>53.155734</td>\n      <td>75.084578</td>\n      <td>420.914992</td>\n      <td>3.013901</td>\n      <td>10.320244</td>\n      <td>7.804561</td>\n      <td>23.245080</td>\n      <td>0.0</td>\n      <td>161.192084</td>\n      <td>1.611960</td>\n      <td>4.075549</td>\n      <td>0.319343</td>\n      <td>0.614027</td>\n      <td>0.460521</td>\n      <td>0.448761</td>\n      <td>0.0</td>\n      <td>9.741043</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>22.000000</td>\n      <td>5.398480e+05</td>\n      <td>3.000000</td>\n      <td>14.000000</td>\n      <td>1.000000</td>\n      <td>14.000000</td>\n      <td>71.000000</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>630.000000</td>\n      <td>1.139436e+06</td>\n      <td>7.000000</td>\n      <td>34.000000</td>\n      <td>6.000000</td>\n      <td>207.000000</td>\n      <td>2010.000000</td>\n      <td>49.000000</td>\n      <td>8.000000</td>\n      <td>7.000000</td>\n      <td>61.000000</td>\n      <td>16.550000</td>\n      <td>2.515000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.020000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>2.599000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>1.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>1011.000000</td>\n      <td>1.497888e+06</td>\n      <td>9.000000</td>\n      <td>50.000000</td>\n      <td>9.000000</td>\n      <td>241.000000</td>\n      <td>2234.000000</td>\n      <td>56.000000</td>\n      <td>19.000000</td>\n      <td>11.000000</td>\n      <td>82.000000</td>\n      <td>62.286000</td>\n      <td>18.004000</td>\n      <td>0.000000</td>\n      <td>9.033000</td>\n      <td>10.913000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>33.120000</td>\n      <td>2.000000</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>3.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>1515.000000</td>\n      <td>2.018003e+06</td>\n      <td>10.000000</td>\n      <td>57.000000</td>\n      <td>11.000000</td>\n      <td>268.000000</td>\n      <td>2448.000000</td>\n      <td>62.000000</td>\n      <td>22.000000</td>\n      <td>12.000000</td>\n      <td>114.000000</td>\n      <td>80.308000</td>\n      <td>40.121000</td>\n      <td>0.000000</td>\n      <td>9.435000</td>\n      <td>15.782000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>84.514000</td>\n      <td>2.000000</td>\n      <td>3.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.0</td>\n      <td>8.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>10348.000000</td>\n      <td>5.345727e+06</td>\n      <td>14.000000</td>\n      <td>73.000000</td>\n      <td>21.000000</td>\n      <td>577.000000</td>\n      <td>3851.000000</td>\n      <td>94.000000</td>\n      <td>38.000000</td>\n      <td>30.000000</td>\n      <td>256.000000</td>\n      <td>404.451000</td>\n      <td>2098.831000</td>\n      <td>18.610000</td>\n      <td>42.883000</td>\n      <td>34.149000</td>\n      <td>105.384000</td>\n      <td>0.0</td>\n      <td>1120.801000</td>\n      <td>10.000000</td>\n      <td>21.000000</td>\n      <td>2.000000</td>\n      <td>2.000000</td>\n      <td>2.000000</td>\n      <td>2.000000</td>\n      <td>0.0</td>\n      <td>73.000000</td>\n    </tr>\n  </tbody>\n</table>
## Requirements
The only specialty packages required is the Python wrapper for the SponsorBlock API
- ```sponsorblock.py v0.2.2```. See <https://github.com/wasi-master/sponsorblock.py>.