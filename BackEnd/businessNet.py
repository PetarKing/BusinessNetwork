#Flask is a pythonic and minimalistic web framework, a perfect candidate for this task
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

#Due to running the front-end and back-end on two different adresses/ports, we need CORS
from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#Pandas is a high-performance data manipulation tool
import json
import pandas as pd
users = json.load(open('data.json'))
users = pd.DataFrame(users)

#Cleaning the data is necessary for healthy perfomance
users = users.dropna(subset = ['id', 'firstName'])
users = users.fillna("(private)")

#Getting the column names, for later usage
cols = [col for col in users]

#Helper functions
def to_dict_array(data):
    return [dict(row[1]) for row in data.iterrows()]

def get_user(id):
    return to_dict_array(users[users["id"]==int(id)])[0]

def top(n):
    return to_dict_array(users.head(n))

#Greeting message
@app.route("/")
def welcome():
    return "<h3>Welcome to the Business Network Backend!</h3>"


#Allowing real-time search of users based on their names or gender
@app.route("/search")
@cross_origin()
def search():
    query = request.args.get('query')
    if query == None:
        return jsonify(top(12))
    elif query == "male":
        return jsonify(to_dict_array(users[users["gender"]=="male"].head(15)))
    elif query == "female":
        return jsonify(to_dict_array(users[users["gender"]=="female"].head(15)))
    else:
        return jsonify(to_dict_array(users[(users["firstName"] + users["surname"]).str.lower().str.contains(query.lower())]))


#Returning the data about a singe user based on his ID
@app.route("/user")
@cross_origin()
def user():
    id = request.args.get('id')
    return jsonify(get_user(id))


#Searching user's fist and second level connections
@app.route("/friends")
def friends():
    id = request.args.get('id')
    level = request.args.get('level')

    user = get_user(id)
    friends = users[users["id"].isin(user['friends'])]

    return_data = ""
    
    if(level == "1"):
        return_data = to_dict_array(friends)

    elif(level == "2"):
        f_two = pd.DataFrame()

        for list_of_friends in friends["friends"]:
            friends_friends = users[users["id"].isin(list_of_friends)]
            f_two = f_two.append(friends_friends[~friends_friends["id"].isin(user['friends'])])

        f_two = f_two[f_two["id"] != int(id)].drop_duplicates(subset="id")
        return_data = to_dict_array(f_two)
        
    else:
        return jsonify(return_data)
    
    return jsonify(return_data)


#Getting the suggested new connections, based on the users social circle
@app.route("/suggest")
@cross_origin()
def suggest():
    id = request.args.get('id')

    user = get_user(id)
    friends = users[users["id"].isin(user['friends'])]

    f_two = pd.DataFrame()

    #Getting the friends of user's friends , but excluding the 1-st level friends
    for list_of_friends in friends["friends"]:
        friends_friends = users[users["id"].isin(list_of_friends)]
        f_two = f_two.append(friends_friends[~friends_friends["id"].isin(user['friends'])])

    #Getting rid of the duplicates
    f_two = f_two[f_two["id"] != int(id)].drop_duplicates(subset="id")

    #Checking which of these people know 2 or more of the user's friends
    result = []
    for person in zip(f_two["id"], f_two["friends"]):
        if len(set(person[1]).intersection(friends["id"].tolist())) > 1:
            result.append(person[0])

    #Getting rid of the duplicates
    result = list(set(result))

    f_two = f_two[f_two["id"].isin(result)]
    return jsonify(to_dict_array(f_two))


#Adding the demonstration of a liking sysyem
likes = {'url': ["1"], 'users': [3]}
likes_df = pd.DataFrame(data=likes)

#Numpy is a powerful linear algebra tool
import numpy as np

#Generating "mock" likes, or serving them once generated
@app.route("/likes")
@cross_origin()
def getLikes():
    global likes_df
    url = request.args.get('url')

    result = ""
    liked = likes_df[likes_df["url"] == url]["users"]
    liked = users[users["id"].isin(liked.tolist())]
    for person in zip(liked["firstName"],liked["surname"]):
        result = result+person[0]+" "+person[1]+"<br>"

    #If likes don't exist, generate a random array of people
    if result == "":
        liked = np.random.randint( 1, 20, size=np.random.randint(10))
        for user_id in liked.tolist():
            likes_df = likes_df.append({"url": url, "users": user_id}, ignore_index=True)
        liked = users[users["id"].isin(liked.tolist())]

        #Getting rid of potential duplicates
        liked = liked.drop_duplicates(subset="id")

        #Generating the HTML display of likes
        for user in zip(liked["firstName"],liked["surname"]):
            result = result+user[0]+" "+user[1]+"<br>"
        
    return result

#Running the app!
if __name__ == '__main__':
    app.run()
