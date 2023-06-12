from flask import Flask, jsonify, make_response
import mysql.connector
import cosine_similarity

try:
	mydb = mysql.connector.connect(
		host= "localhost",
		user="root",
		password="",
		database="cupid_db"
	)
	print("[+] Database is Connected. Name :: cupid_db")
except mysql.connector.Error as err:
	print("[-]Database Error :: {}".format(err))



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_tb")

myresult = mycursor.fetchall()

app = Flask(__name__)

@app.route('/cosine')
def getData():

	person1 = {
        'lastname': 'smith',
        'age': 30,
        'height': 180,
        'gender': 'male',
        'bio': 'i am a software engineer with a passion for coding'
    }
	person2 = {
        'lastname': 'smith',
        'age': 35,
        'height': 175,
        'gender': 'female',
        'bio': 'i work as a date scientist and enjoy analyzing complex data'
    }

	cosine_result = cosine_similarity.calculateCosineSimilarity(person1, person2)
	
	response = make_response(
		jsonify(
			{"cosine_similarity": str(cosine_result)}
		),
		200
	)
	
	return response

if __name__ == "__main__":
	app.run(debug=True)