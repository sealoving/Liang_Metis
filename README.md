# First Week at Metis & Project Benson
  
## A Short and Long Week
It has been a short week, time-wise. Our Seattle Winter cohort started on a Tuesday, as the Monday was MLK day. This means that not only we had to cover more contents each day, but also we lost one precious day to work on the first project (due on Friday!). I remember feeling nervous on Monday night and had trouble falling asleep. I partly blame that on shifting my "late-owl" schedule to "early-bird". Living in Redmond, I spend on average 2.5 hours per day commuting to Seattle downtown by bus. For the first week, I probably slept less than 6 hours per day but remained surprisingly productive, which was quite unusual for me. I guess there was a bit of adrenaline rush there.
  
The outcome?
  
It turned out a long week, productivity-wise. To be honest, at the end of the week I felt exhaused just like the gym bootcamp classes I've been to, and I'm a little disappointed at myself on how the project turned out. However, this "learning feast" has been quite satisfying, and it excites my to think about what to learn and practice next. Each day at the bootcamp consists of paired programming, lectures, and project work. The paired programing and lectures laid a necessary foundation for the tools and design thinking to be applied in the project, but they are meant to be a starting point. The core of the learning happens when you try to apply what you've learned. Sites such as stackoverflow quickly became one of my best friends, but there are plenty of times I got lost. Those were the times when the our instructors and teaching assistants would offer immediate help. For someone who's normally comfortable with self-learning at home, this made a big difference for me.   

The diversity of the classmates (or should I say, my colleagues) is amazing. People bring in ideas/stories from fields like math, economics, earth sciences, astronomy, programming, etc. I personally appreciate very much the social aspects of these bootcamps. After working from home for a remote employer for months, this has been a nice change.
## Project Benson  

For the first week is a group project, and I had the honor to form a team with Alando and Natalia. A request was sent from a (fictional) client in NYC, WomenTechWomenYes(WTWY). They have an annual gala at the beginning of the summer, both for publicity of women in technology and for fundraising for their cause. The question: could we provide professional opinions on the placement of their street teams at subway stations, to obtain sign-ups from people that are most likely to attend the gala, and even better, to donate money?
  
The suggested dataset is the MTA turnstile data, which is freely available. After some discussion, the team also selected two additional datasets to add to our analysis: demographics such as women population and income level, and the locations of tech companies in NYC. In an ideal world, we were good to go and it felt like once we combine all these, magic would happen. The reality? It was quite a journey through obstacles, and we could not have learned in a better way.

#### Dealing with the Dirty and and the Messy
**Understanding the data** I bet I was not the only one that took some efforts to figure out the meaning of the columns. Each unique combination of the first 4 columns corresponses to one turnstile in the whole NYC subway system. Once that was figured out, data organized by turnstiles for each station was just one "groupby" away in pandas. 
  
**Watch for Outliers** At individual turnstile level, it was not difficult to tell the entry/exit recording was cumulative. One would assume that the numbers simply goes up monotonically - it did, mostly. Quick plots showed big outliers: sometimes it was a big drop (the recorder was reset), or a big jump (perhaps surges as some of these happen across several turnstiles at the same station). (Un)luckily, the outliers threw off the mean by magnitudes, which also made it straightforward to detect and remove them.
  
**Data Merging Relay Race** At this point we had ranked the stations by mean daily traffic volume for the year of 2017. NYC census data was available in a clean format on Kaggle. But merging the two took the longest time in our data preparation, in three steps:
* Cooridinates of the stations were in a separate csv file than the MTA turnstile data. And... stations were named differently in two files. Option 1: find another coordinates file with the same names. Option 2: figure out the naming mapping between the two. Our team went for Option 2, and Alando solved it with "FuzzyWuzzy" package. Stations were located.
* Census data were only given by census tract code. To find the corresponding census tract for each station, a "locater" has to work. Alando tried mapping to Zip code but were stopped by glitches in Google API. Without knowing better approaches, I wrote a function as a backup plan, which maps each station to their closest census tract based on centroid, which worked well for most stations, but not perfect. In the end, Natalia found a method to send online request to locate (lat,long) point to census tract directly. The relay race is finally completed. Teamwork is the best.  

#### The Presentation


## Final Thoughts
  
**Learning on the Go**


