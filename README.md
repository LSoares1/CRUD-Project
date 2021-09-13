# CRUD-Project

## Project Brief

The objective of this project was to create an app with full CRUD functionality using the supporting methodologies taught during training. This meant using the Flask micro-framework and storing information on a MySQL database with a minimum of two tables sharing a relationship.

## App Design

My initial thoughts for this project were to create an Olympics insight app where users could enter athlete details, result details, event details and venue details. The entity relationship diagram for this idea is shown below:

![full ERD](https://user-images.githubusercontent.com/88770768/133034390-b90f2db6-3c20-4aac-aef8-28ec4d49a4e5.JPG)

However, after some thought I decided to just create an app with athletes and results with a one-to-many relationship. The ERD for this final idea is shown below:
This final idea has two tables called athletes and results with the athletes table containing 6 fields including a primary key named athlete_ID. The results table contains 5 fields with a primary key named result_ID and a foreign key named athlete_ID. This demonstrates that there is a relationship between the two tables as each result can only be associated with one athlete, but each athlete can have more than one result. 


![final ERD](https://user-images.githubusercontent.com/88770768/133034498-6f3dca01-8c26-479f-8af0-0972f112fbb3.JPG)


## Risk Assessment

Before the development of the app began a risk assessment was performed to identify and evaluate all the potential risks and hazards associated with the project which is shown below:

![Risk assessment](https://user-images.githubusercontent.com/88770768/133037637-b3a6782a-fed7-4d4d-9576-a8e7c0cb39f4.JPG)


## Project Tracking

Tracking the progress of the project was a key step in ensuring that the MVP was achieved with a working application and full documentation. Trello was used to create a project tracking board where items were assigned user stories and were tracked using a MOSCOW approach. This meant that items that were necessary for the MVP were classed as must have and additional elements that I wanted to implement were designated as should have as seen in the figure below:

![Trello](https://user-images.githubusercontent.com/88770768/133034574-b47dbe62-bfc0-47f7-9960-2fc850fe953f.JPG)
![User story](https://user-images.githubusercontent.com/88770768/133034699-77c55d9a-f7f0-4173-a82b-915016122364.JPG)


## CI Pipeline

A virtual environment within a virtual machine hosted on Amazon Web Services was used for most of this project as this meant that pip installs would not conflict with any previous installs on the same machine.

Jenkins was used to automate the testing of the application which implemented webhooks that looked for changes within the git repository and automatically ran the tests when any new code was pushed to the repo.

My CI Pipeline is shown below:

![CI pipeline](https://user-images.githubusercontent.com/88770768/133034763-74f74f14-8088-4f7e-ab89-4be3cffa53dc.JPG)


## Testing

Unit Tests were used to test the functionality of the app which confirmed that information could be created, read, updated, and deleted. Tests were also developed to ensure that the different webpages within the app loaded up correctly. If any of these tests failed, then the build would be considered unsuccessful.

![all tests successful](https://user-images.githubusercontent.com/88770768/133034823-5241d193-b9f4-49a9-9937-768767401345.JPG)
![Coverage Report](https://user-images.githubusercontent.com/88770768/133034859-af100080-5174-4d0d-b5ce-e77c8725d696.JPG)

## The App

When the app is first launched the user is shown the home page. From the home page the user can add and view athletes and results

![Home](https://user-images.githubusercontent.com/88770768/133036228-4a763414-0b25-4fc6-87f5-02727eb11811.JPG)

On the add athletes page the user is presented with a form where athlete information can be entered
![Add athlete](https://user-images.githubusercontent.com/88770768/133036852-758e1b54-d53f-4a92-abbe-9ba3c3153395.JPG)

On the add results page the user is presented with a form where results can be entered with a dropdown menu to assign the result to a specific athlete within the database
![Add Result](https://user-images.githubusercontent.com/88770768/133036863-3b0ee9e8-a07c-49da-8cc9-856668a44822.JPG)

From the view athletes page the user can choose to update or remove the athlete from the database
![View athlete](https://user-images.githubusercontent.com/88770768/133036882-f96e60c5-d2a4-40ff-8630-07be92193924.JPG)

From the view results page the user can choose to update or remove results from the database
![View result](https://user-images.githubusercontent.com/88770768/133036896-d02e4d56-04fe-4ef3-a56d-e91a46047702.JPG)


## Sprint Review

Overall, I feel like the project went well as culminating all the knowledge gained over the course of the training has helped me gain a better grasp of key concepts. This project has also helped me to understand how to work in an agile way by using project tracking to keep on top of my workload.

Some aspects of the project were especially challenging such as testing as I feel like this is where my knowledge is lacking. This meant that I spent longer than I wanted to testing my application which slowed my progress. Given more time I would have liked to use Jenkins to build and run the application as this would automate the process.


