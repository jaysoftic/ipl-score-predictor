# IPL Score Predictor :india:
![GIF](readme_resources/ipl_teams.jpg)

#### The IPL Score Predictor project is about predicting score of batting team.
#### This web application have IPL 2021 teams where you can predict score of batting team.

## Overview
- I have IPL matches records from year 2008 to 2020.
- I have trained machine learning model for 8 teams which were playing in year 2021.
- Here i have performed hyperparameter tunning on various model and i got **Random Forest** as best model for this problem statement.
- Gradient Booost algorithm gives **0.850539 r2_score** & **1.632532 MAE** on train dataset and **0.871335 r2_score** & **6.438084 MAE** on test dataset.
- Random Forest algorithm gives **0.672894 r2_score** & **11.296707 MAE** on train dataset and **0.681484 r2_score** & **12.173585 MAE** on test dataset.
- Difference of train dataset MAE and test dataset MAE is **4.805552** for Gradient Boost.
- Difference of train dataset MAE and test dataset MAE is **0.876878** for Random Forest.
- Here accuracy or **r2_score** of Gradient Boost algorithm is higher than Random Forest but Random Forest's **MAE** difference between train and test dataset is lower than Gradient Boost.
- If i select Gradient Boost algorithm which has high r2_score then our model will **not perform stable** as it performed on train dataset because **MAE** difference between train and test dataset is **high** that's why it might generate **overfitting** issue.
- If i select Radom Forest algorithm which does not have high r2_score still it will perfrom **stable** as it performed on train dataset because MAE difference between train and test dataset is **low**.
- Here i have selected **Random Forest** algorithm with it's hyperparamter which best fit for this problem statement with around **68%** of accuracy.
- Application developed using Flask, Javascript, Bootstrap, CSS and HTML

## Data Source
- In this project i have used IPL dataset from kaggle, you can get it from [here](https://www.kaggle.com/patrickb1912/ipl-complete-dataset-20082020)

## Demo
- I have deployed this on Heroku platform
Link: [https://ipl-jaysoftic.herokuapp.com/](https://ipl-jaysoftic.herokuapp.com/)

![GIF](readme_resources/IPL.gif)

## How to use
- Select venue, batting team, bowling tean and fill the inputs with proper information then click on predict button you will get predicted score of batting team.

## Technologies Used
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png"></code>
<code><img height="30" src="https://github.com/tomchen/stack-icons/raw/master/logos/bootstrap.svg"></code>
<code><img height="30" src="https://symbols.getvecta.com/stencil_80/56_flask.3a79b5a056.jpg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Heroku_logo.svg"></code>

<code><img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code>
<code><img height="30" src="https://matplotlib.org/_static/logo2.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/330px-Scikit_learn_logo_small.svg.png"></code>

## Team
[![Jay Soni](https://avatars3.githubusercontent.com/u/49163967?s=400&u=be22bbe1409ff51991b04026f038c1373174a02a&v=4)](https://in.linkedin.com/in/jaysoftic) |
-|
[Jay Soni](https://in.linkedin.com/in/jaysoftic) |)

## Credits
- Entire credits goes to My God

## 
- If you like my work and it helped you in anyway then please do ⭐ the repository it will motivate me to make more amazing projects
