\# Recipe Recommendation App



\## 1. Project goal



The project aims to help users plan their daily meals by recommending suitable recipes based on:



\* available ingredients

\* user preferences

\* dietary restrictions

\* calorie requirements

\* previously liked recipes



The application will consist of a mobile client and a Python backend.



\## 2. MVP features



The first version will include:



1\. User registration and authentication

2\. Adding available ingredients

3\. Recipe database

4\. Recipe recommendation system

5\. Recipe details:



&#x20;  \* ingredients

&#x20;  \* quantities

&#x20;  \* cooking instructions

6\. Mobile user interface

7\. REST API connecting the mobile application with the backend



The initial MVP will focus on recommending recipes based primarily on available ingredients and user preferences.



\## 3. System architecture



The application will use a client-server architecture.



\### Mobile application



\* Flutter

\* Communicates with the backend through REST API

\* Displays recipes and user information

\* Allows users to manage their ingredients and preferences



\### Backend



\* Python

\* FastAPI

\* Handles authentication

\* Processes user requests

\* Communicates with the database

\* Runs the recommendation algorithm



\### Database



\* PostgreSQL

\* Stores users, recipes, ingredients, preferences and other application data



\### General architecture



Mobile App

↓

REST API

↓

FastAPI Backend

↓

Recommendation Service

↓

PostgreSQL Database



\## 4. Database schema



The initial database will contain:



\### User



\* id

\* email

\* password\_hash

\* created\_at



\### Recipe



\* id

\* name

\* description

\* instructions

\* calories

\* created\_at



\### Ingredient



\* id

\* name



\### RecipeIngredient



\* recipe\_id

\* ingredient\_id

\* quantity

\* unit



\### UserIngredient



\* user\_id

\* ingredient\_id

\* quantity

\* unit



\### UserPreference



\* user\_id

\* preference

\* value



The database structure may be expanded as new features are added.



\## 5. API endpoints



Initial endpoints:



\### Authentication



POST /auth/register



POST /auth/login



\### Ingredients



GET /ingredients



POST /users/me/ingredients



GET /users/me/ingredients



DELETE /users/me/ingredients/{ingredient\_id}



\### Recipes



GET /recipes



GET /recipes/{recipe\_id}



\### Recommendations



POST /recommendations



The API will be expanded as the application develops.



\## 6. Recommendation algorithm



The recommendation system will initially use a rule-based approach.



The system will consider:



\* how many required ingredients the user already has

\* missing ingredients

\* user preferences

\* dietary restrictions

\* calorie requirements



Each recipe will receive a recommendation score.



Machine learning will be introduced after the MVP has collected enough user interaction data.



Potential future ML approaches include:



\* classification models

\* regression models

\* decision trees

\* recommendation algorithms

\* content-based filtering

\* collaborative filtering



The final ML approach will be selected based on the available data and recommendation problem.



\## 7. Mobile screens



The initial mobile application will contain:



1\. Welcome / registration screen

2\. Login screen

3\. Main screen

4\. My Ingredients screen

5\. Add Ingredient screen

6\. Recommended Recipes screen

7\. Recipe Details screen

8\. Profile / Preferences screen



\## 8. Future features



Potential future features include:



\* calorie tracking

\* allergies

\* dietary preferences

\* restricted ingredients

\* favorite recipes

\* recipe ratings

\* personalized recommendations

\* meal planning

\* shopping list generation

\* recipe history

\* nutritional information

\* AI-powered recipe recommendations

\* personalized weekly meal plans

