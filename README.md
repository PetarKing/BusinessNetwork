# BusinessNetwork
An Interview Test Project

## Running the project
To run the project:

* Start the backend following the instructions in the BackEnd folder
* Start the frontend following the instructions in the FrontEnd folder

## About the project
This project is made as a part of the interview process for the [30Hills](http://30hills.com/) 2018 spring internship program.

### The Problem
> The goal of this test is to create a method of examining a Social Network. You are given dataset (data.json) representing a group
> of people, in the form of a social graph. Each person listed has one or more connections to the group.
> 
> Use data.json provided. You should then create a Web app or an API endpoint, which provides functionality to choose a person
> within the group stored in the database and display the following information about this person:
> 
> * Direct friends: those people who are directly connected to the chosen user (required);
> * Friends of friends: those who are two steps away from the chosen user but not directly connected to the chosen user (required);
> * Suggested friends: people in the group who know 2 or more direct friends of the chosen user but are not directly connected to
> the chosen user (optional);
> 
> General Requirements:
> You can use any software design patterns you think are appropriate for the implementation.

### The Solution
The solution I propose for this probelem is a website prototype, themed as a business network.
For the purpose of this project, I created a Python Flask backend and the Vue JS frontend.

* BackEnd
  * Direct friends
  * Friends of friends
  * Suggested friends
  * Liking system prototype
    * Generating likes for all the posts and then storing and serving them

* FrontEnd
  * Bootsrap Design
  * Business News feed
    * Restful API
    * 3 Different Publishers
  * Interactive User inspection
    * Quility design for data repsentation
    * Smart Searching by full names or gender
    * User image based on gender
    * Quick user switching

 
