
<h1>Exploratory Data Analysis </h1>

During our EDA, we found that there are 16000+ unique players in our dataset but only about 6000 were currently playing. We found out the that the data set had the name, age, physical attributes, financial attributes and international attributes. There were a total of 65 columns.
<br>

<h1>Research Questions </h1>

<h2>Question 1:</h2>

<h3>What is the relationship between a players financial figures and their other attributes?</h3>

<p>
First, we look at a heat map of some playing characteristics and their relationship to the financial data.<br>

<img src ="images/Analysis1/Fig1.png" width='500px'> <br>

We can see that the age of a player barely has any correlation with the players value and release clause. But Age plays a significant role in the overall of a player.
We can also see that the overall rating of a player has a greater effect on their wage than value. And since age has a correlation with overall, we can say that even though it is not apparent in the heatmap, there is some correlation between the age and value.
We also see strong connections of the release clause with value and wage.<br>
</p>

<hr/>
<br>


<p>
Next,  we see if physical attributes have an effect on value. For this we will use a heat map again as it gives us the most detail.<br>

<img src ="images/Analysis1/Fig2.png" width='500px'><br>

We see that physical attributes such as height and weight have no correlation with a players value and the values in the heat map are very close to 0 indicating that there is no correlation. As expected, height and weight have a strong correlation as well as value and wage. There is also some correlation between a players overall with value and wage.<br>
</p>

<br>
<hr/>
<br>

<p>
We will now plot avg. wage and avg. value vs the nationality of the players <br>

<img src ="images/Analysis1/Fig3.png" width='500px'><br>

We can make some findings from these graphs. Although England has by far the most number of players in the game, the most valuable countries are Spain and Brazil. We also noticed a correlation to the players overall and value and we can make an assumption that the overall quality of players from Spain and Brazil are higher than that of England. This can also be seen in case of the wage as the total wages are almost the same. 
We also see that the top 8 countries in both categories are from Europe and South America.
</p>
<hr/>
<br>

<p>
 Let us now see which positions are most valuable and the most highest paid.<br>

<img src ="images/Analysis1/Fig4.png" width='300px'>    
<img src ="images/Analysis1/Fig5.png" width='314px'><br>

 We notice that CF was the highest paid compared to any other position. All other positions are paid very similarly and that is around 1/3 the average wage of CF. ALthough RAM and CF have the same number of players, RAM is not even the second most paid position. This might be due to CF positions having more star players.<br>
RAM position players are most valuable players followed by LF, LAM, RCB and CF. This is surprising considering that CF players were payed much higher than any position. This maybe due to the fact that most CF players are star players and bring in a lot of sponsors for the teams compared to other positions.<br>
</p>

<hr/>
<br>


The following is what can answer the above question:
1. Age has no direct correlation to value. But, overall has some correlation to the age and value. From this, we can see that there might be some indirect correlation between age and value.
1. Wage and Release Clause have a linear relationship with Value
1. On average, players from Europe and South America are valued more and have higher wages
1. CF and RAM are the most rarest players. CF players are the most paid and RAM players are the most valued. They both are not in the top 3 of the other category.
<br>

[You can find the full analysis notebook here, including the code and the data here](./notebooks/analysis1.ipynb)


<hr/>
<br>

<img src ="images/301_graphs.png" width='500px'> <br>

<h2> Question 2: </h2>

<h3> I wish to find out if Center Attack Midfielders are generally better than players in other positions, as CAM are often thought of as the most technically gifted. </h3>
<br>
I used the five stats that have been graphed above. I used them because my knowledge of FIFA is quite limited and I thought of these stats to be the most "skillful" of what was in the data set. 
<br><br>
I used the overall rating to see where the CAM position compared to the others in general. This gave me a good starting point, so far the CAM position is really good, but is not far and above other positions.However, this led me to question wether or not certain positions on the field are more prone to more/less of a certain stats, purely based on physical position on the field. So as the CAM position is further up the field their defensive stats ended up being much lower than many other positions. I concluded that the CAM position must be in a worse place to gain defensive stats. So I removed the defensive stats from the analysis as I wanted to know if CAM players were the most technically gifted. I was left with dribbling, short passing, crossing, and shot power. I found that the CAM players are still arguably contains the best offensive technical players on the field, however the position itself is not far more or less impressive than many other position.
<br>

[You can find the full analysis notebook here, including the code and the data here](./notebooks/analysis2.ipynb)
<hr/>
<br>
