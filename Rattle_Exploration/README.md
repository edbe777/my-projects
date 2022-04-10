# Credit Scoring Analysis and Machine Learning Ecploration Project

Exploration of R with Rattle (interactive GUI built on top of R) 

## Steps:
Data: Old German credit dataset which I found online. File is in GitHub repo.

Take a look at the var_desc tab in the Credit_Scoring excel workbook. Workbook is in GitHub repo.
![image](https://user-images.githubusercontent.com/61211582/162616236-15c62b6b-0b87-4288-9a64-eeb00e791d8f.png)


## The objective is to build a predictive model to show if a customer is likely to pay back to loan or not.
Launch Rattle by typing Rattle() -this is the only code which you need to type

In Rattle Window, click on the file name to import the credit.csv file (included in the GitHub repo).
Source radio button should be file.

Change the 'Credit' variable to Target, and change the 'gastarb' (foreign worker) variable to Input since we are trying to predict the credit (loan good or bad). 

On the partition box, the default value is 70/15/15. Let's change the random sample value to 70/30/0   Partition = 70% of the dataset to build the model, 30% to test, and 0 because we don't need a third sample at all. 

Click execute to run this code, and it should look like the image below.

Next, let's explore the data. Click on the explore tab.
Check the summary box, and click execute. The code should look like the image below.

Uncheck the summary box, and check the describe box. The code should look like the image below. There are more options here but we will move on ti distributions.

Click the distributions radio button, and then check the credit histogram button to generate the image below. Neat!

Uncheck the credit histogram and check the duration boxplot button to generate the image below.

Click the test tab and check the correlation radio button under the paired-two-sample tests to see the P Value and confidence interval between 2 samples (I picked duration and rate) The output should look like the picture below.

We can also trashform the data in the transform tab, like Python, but with no code. We can even select the Rank and Intervals.

Click on the Cluster tab and then select Kmeans to perform a cluster analysis. The code should look like the image below. 

Rattle also has the associate tab which allows us to work with categorical variables. My data only has numerical columns, so I will skip this part.

## Models
Click on the Model tab and then select the Tree and traditional radio tabs. Make the minumim Split 40 and the min bucket 20 for faster processing time. Then click on execute. The code should look like this:

Lets go crazy and select the 'all' radio button. Then click on Execute. It will generate all models, and we can click on each radio button to see the results.


Let's evaluate the models we just made. Click on the evaluate tab and then select the tree model. Then click on the ROC and validation radio buttons. 
This generates the following Image where we can see that the random forest, ksvm, and glm models performed the best (Area under the ROC curve >0.75).


If we click on the training radio button and execute the code, we see an very informative error message. There we can see overfitting for the xgb and rf models. This can tell us a lot about the training data. 


## Log
The last tab is the Log which shows us our actions with timestamps. 










