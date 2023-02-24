**Applicant Scoring System**
-
This script takes an input file with attribute values of both applicants and
team members. We use the team member scores to determine the team average for each
attribute. Then we score each applicant based on whether they improve the average
or make it worse. Sample input:
\
\
<code>{
"team": [
{
"name": "Eddie",
"attributes": {
"intelligence": 1,
"strength": 5,
"endurance": 3,
"spicyFoodTolerance": 1
}
},
{
"name": "Will",
"attributes": {
"intelligence": 9,
"strength": 4,
"endurance": 1,
"spicyFoodTolerance": 6
}
},
{
"name": "Mike",
"attributes": {
"intelligence": 3,
"strength": 2,
"endurance": 9,
"spicyFoodTolerance": 5
}
}
],
"applicants": [
{
"name": "John",
"attributes": {
"intelligence": 4,
"strength": 5,
"endurance": 2,
"spicyFoodTolerance": 1
}
},
{
"name": "Jane",
"attributes": {
"intelligence": 7,
"strength": 4,
"endurance": 3,
"spicyFoodTolerance": 2
}
},
{
"name": "Joe",
"attributes": {
"intelligence": 1,
"strength": 1,
"endurance": 1,
"spicyFoodTolerance": 10
}
}
]
}
</code>\
\
Sample Output:\
<code>{
"scoredApplicants": [
{
"name": "John",
"score": 0.25
},
{
"name": "Jane",
"score": 0.5
},
{
"name": "Joe",
"score": 0.25
}
]
}</code>
\
\
**How to run the script**\
Ensure you have a Python 3 virtual env setup and run the following command\
<code>python applicants.py</code>