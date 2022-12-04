# Final Report #
by Sherwan Thomas 

# Research Question
I would like to find out relationsips 1) between  age of the player with position and performance and then 2) using specific stats that comprise the main attributes : Shooting(SHO), Pace(PAC), Physical (PHY), Defence (DEF), Dribbling(DRI) and Passing(PAS).

# Introduction
We chose to work on this dataset since it was simple to grasp and few of our members were very interested in FIFA and football (**not soccer**).This dataset proved useful for learning exploratory data analysis. We first organised a team and began looking for a suitable dataset. We then created a shared repository for us to work on at any time with seamless integration and were taught how to use GitHub. We learned project management skills and worked on preparing our dataset. We processed and cleaned our dataset, performed exploratory data analysis (EDA), built some data visualisations, and experimented with Pandas method chaining. Finally, we exhibited our efforts in a Tableau Dashboard. We were also given feedback and given opportunity to tweak our project.

This data set was found on kaggle.com from the author, BRYANB. The author was able to procure the date from another website called Sofifa which houses data about players and teams from various FIFA games and this dataset includes 16000+ unique player stats from FIFA 22. This data consists of aggregated data such as name of the players, age, country and detailed data such as offensive potential, defense, acceleration. The dataset we use is specifically for the FIFA 22 game and was updated last on October 2022. This data was collected using beautifulsoup from the website Sofifa. General information from was scraped from the main page and each player's webpage was scraped individually. This was done by defining a batch size to parallelize the retrieving of data and then the dataframes were merged and cleaned.
 

# Exploratory Data Analysis

# Question 1 - Relationship Between Age and Performance
To find out a relationship between age and performance, we use a simple scatter plot with age on y-axis and player performance or overall rating on the x-axis.
We can clearly see a linear positive relationship as age increases, overall increases but we do see an overplot in certain regions indicating that most of the players are in that overall and age region.
![Relationship Between Age and Performance](scatter1.png)
![Count of Players in an age with Overall](project-group28/images/Analysis3/barplot.png)

# Question 2 - Using specific stats with Age and Performance
We took a few different plots to see the specific differences between stats and overall and age
a) Heatmap of Overall, Shooting Attributes and Age: a positive correlation with age and shot power (indicating an increase in shot power with age) and shooting attributes with overall 
![Using ATTACK with Age and Performance](project-group28/images/Analysis3/heatmap.png)
![Using DRIBBLING with Age and Performance](project-group28/images/Analysis3/dribbling1.png)


b) Dristribution of Player Age and Overall with Dribbling Rating: shows that the dribbling rating usually peaks around age 24-27 and tends to drop after that age.
![Relationship Between Age and Performance](project-group28/images/Analysis3/heatmap.png)

c) Specific Age and Overall vs ATT, DEF, PAC, PHY, DRI, and PAS plots are shown on Dashboard3, interesting trends such as a positive correlation relationship between technical attributes (ATT, DEF, DRI, PAS) while there is a negative correlation with PHY and PAC attributes with an exception in Strength as age increases.
![Relationship Between Age and Performance with Physical Attributes](project-group28/images/Analysis3/tableau1.png)
![Relationship Between Age and Performance with Technical Attributes](project-group28/images/Analysis3/tableua2.png)


# Summary and Conlusion
