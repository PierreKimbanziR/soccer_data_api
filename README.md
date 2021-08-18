# Premier League Rest Api  

## Motivations behind this project  

I am currently working on a machine learning model that predicts the final results of Premier League football matches. In order to be able to make these predictions, the model requires statistical data on each player and each team during the matches. 
To make the data ingestion process more fluid it is almost essential to have a database and a rest api to issue queries against this database. 
This api will be part of a data pipeline which is also under development

## Objectives 
- Program a rest api to serve previously collected data from the English football championships.

##  Technologies
- Django
- Django Rest Framework 
- Postgresql

## Project structure

Below you can see the structure of the rest api. The major components will be detailled further in the readme.

![bpmn](soccer_api/assets/images/rest_api_bpmn.png)

## Data
The data is scrapped on the website [Fbref.com](https://fbref.com/en/). 
For the moment it is the statistics of the 2020-21 season.  
I plan to add more types of data in the future.  
They are divided into 2 categories: 
- Seasonal statistics for a team 
- Seasonal statistics for a player
### Examples

This is what an entry looks like for a team :  

![team_entry](soccer_api/assets/images/team_data.png)  

This is what an entry looks like for a player :  

![team_entry](soccer_api/assets/images/playersrealdata.png)
