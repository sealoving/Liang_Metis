# First Week at Metis & Project Benson
  
## A Short and Long Week
It has been a short week, time-wise. Our Seattle Winter cohort started on a Tuesday, as the Monday was MLK day. This means that not only we had to cover more contents each day, but also we lost one precious day to work on the first project (due on Friday!). I remember feeling nervous on Monday night and had trouble falling asleep. I partly blame that on shifting my "late-owl" schedule to "early-bird". Living in Redmond, I spend on average 2.5 hours per day commuting to Seattle downtown by bus. For the first week, I probably slept less than 6 hours per day but remained surprisingly productive, which was quite unusual for me. I guess there was a bit of adrenaline rush there.
  
The outcome?
  
It turned out a long week, productivity-wise. To be honest, I felt exhausted at the end of the week just like the gym bootcamp classes I've been too, but mentally. I'm not satisfied with how the project turned out - it could have been better (as always), but I'm content with this learning feast and it excites me just thinking about how many more things to learn in the following days. Each day at the bootcamp consists of paired programming, lectures, and project work. The paired programing and lectures laid a necessary foundation for the tools and design thinking to be applied in the project, but they are meant to be a starting point. The core of the learning happens when you try to apply what you've learned. Sites such as stackoverflow quickly became one of my best friends, but there are plenty of times I got lost. Those were the times when the instructors and our teaching assistants would offer immediate help. For someone who's normally comfortable in self-learning at home, this made one of the biggest differences for me.   

The other big difference from learning at home is the diversity of the classmates (or should I say, colleagues!). It is refreshing to hear all kinds of ideas/stories from fields like math, economics, earth sciences, astronomy, etc. 

Another thing I personally appreciated was the social aspects of these bootcamps. After working from home for a remote employer for months, this environment full of interactions with people is such a nice change.
## Project Benson  

The first project is a group project and my team has three people. We got a request from a (fictional) client in NYC, WomenTechWomenYes(WTWY). They have an annual gala at the beginning of the summer, both for publicity of women in technology and for fundraising for their cause. The question: could we provide professional opinions on the placement of their street teams at subway stations, to obtain sign-ups from people that are most likely to attend the gala, and even better, to donate money?
  
The suggested dataset is the MTA turnstile data, which is freely available. After some discussion, the team also selected two additional datasets to add to our analysis: demographics such as women population and income level, and the locations of tech companies in NYC. In an ideal world, we were good to go and it felt like once we combine all these, magic would happen. The reality? It was quite a journey through obstacles, and we could not have learned in a better way.

#### Dealing with the Dirty and and the Messy
The first obstacle was to clean up the MTA turnstile data. I bet I was not the only one that took some efforts to figure out the meaning of the columns. Each unique combination of the first 4 columns corresponses to one turnstile in the whole NYC subway system. Once that was figured out, data organized by turnstiles for each station was just one "groupby" away in pandas. 
  
The second obstacle came from the turnstile entry/exit records. The number is cumulative, so one would assume it goes up monotonically. Quick plots showed big anormalies: sometimes the machine resets (big drop), or surges (big increase). The anormalies threw off the mean by several magnitude, which also makes them easy to be detected, and removed.

At this point we have ranked the stations by mean daily traffic (entries plus exits) for year 2017. Time to merge demographics. Luckily there are cleaned NYC census data availabel on Kaggle.

#### Learning on the Go

## Final Thoughts  


