'''from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


conn.commit()

@app.post("/")
async def handle_request(request: Request):
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('username')


            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()


            if user:
                # Username exists, do something with the existing user
                username = user[0]
                response_content = {
                    "fulfillmentText": f"Welcome back, {username}! Your current score is {user[2]}"
                }
            else:
                # Username doesn't exist, create a new user record
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
                user = cursor.fetchone()
                username = user[0]
                conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {username}! Your score is now set to 0."
                }



            # Send the response
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})

'''
'''
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


conn.commit()

@app.post("/")
async def handle_request(request: Request):
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('username')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[2]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

            # Send the response using the stored username
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

conn.commit()

@app.post("/")
async def handle_request(request: Request):
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('name')
            print("Extracted Username:", username)

            # Check if the username already exists in the database
            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index to match the column order in your table
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[2]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                conn.commit()
                stored_username = username
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

            # Send the response using the stored username
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})

import json
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

conn.commit()

@app.post("/")
async def handle_request(request: Request):
    logging.basicConfig(level=logging.INFO)

    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        logging.info("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        logging.info("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Get the username from the request
            username = json.loads(request.body.decode())["queryResult"]["parameters"]["name"]

            # Log the username
            logging.info(f"Received username: {username}")

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            # If the username exists, welcome back the user and return their current score
            if user:
                stored_username = user[0]
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[2]}"
                }
            else:
                # Insert the new user into the database and welcome them
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                conn.commit()
                stored_username = username
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

            # Return the response
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log the exception
        logging.error(f"Error processing request: {str(e)}")

        # Return a 500 Internal Server Error response
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})
import json
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

conn.commit()

@app.post("/")
async def handle_request(request: Request):
    logging.basicConfig(level=logging.INFO)

    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        logging.info("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        logging.info("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Get the username from the request
            username = json.loads(request.body.decode())["queryResult"]["parameters"]["name"]

            # Log the username
            logging.info(f"Received username: {username}")

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            # If the username exists, welcome back the user and return their current score
            if user:
                stored_username = user[0]
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[2]}"
                }
            else:
                # Insert the new user into the database and welcome them
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                conn.commit()
                stored_username = username
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

            # Return the response
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log the exception
        logging.error(f"Error processing request: {str(e)}")

        # Return a 500 Internal Server Error response
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

conn.commit()

@app.post("/")
async def handle_request(request: Request):
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')


            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM USER_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index if necessary
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[2]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

            # Send the response using the stored username
            return JSONResponse(content=response_content)

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})


from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

conn.commit()

@app.post("/")
async def handle_request(request: Request):
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index if necessary
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[1]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

        elif intent_display_name == "answer":
            # Extract the user's response
            user_response = payload['queryResult']['queryText']

            # Find a matching question in QUE_table based on user's response
            cursor.execute("SELECT * FROM que_table WHERE answer = %s", (user_response,))
            matching_question = cursor.fetchone()

            # Retrieve the username from the payload
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if matching_question:
                if user:
                    # Username exists, update the score
                    cursor.execute("UPDATE user_TABLE SET score = score + 1 WHERE username = %s", (username,))
                    conn.commit()

                    stored_username = user[0]  # Adjust the index if necessary
                    response_content = {
                        "fulfillmentText": f"Correct, {stored_username}! Your score is now {user[1] + 1}."
                    }
                else:
                    # Username doesn't exist, handle accordingly
                    response_content = {
                        "fulfillmentText": "Username not found. Please provide a valid username."
                    }
            else:
                # No matching question found
                response_content = {
                    "fulfillmentText": f"Good luck next time! Your current score is {user[1] if user else 0}."
                }

        # Rest of the code remains unchanged


    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

@app.on_event("startup")
def startup_event():
    # Create a connection pool on startup
    app.state.conn = mysql.connector.connect(**db_config)
    app.state.cursor = app.state.conn.cursor()

@app.on_event("shutdown")
def shutdown_event():
    # Close the connection pool on shutdown
    app.state.conn.close()

@app.route("/", methods=["GET", "POST"])
async def handle_request(request: Request):
    try:
        # Create a new cursor for each request
        cursor = app.state.conn.cursor()

        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index if necessary
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[1]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                app.state.conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

        elif intent_display_name == "answer":
            # Extract the user's response
            user_response = payload.get('queryResult', {}).get('parameters', {}).get('text')

            # Find a matching question in QUE_table based on user's response
            cursor.execute("SELECT * FROM que_table WHERE answer = %s", (user_response,))
            matching_question = cursor.fetchone()

            # Retrieve the username from the payload
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if matching_question:
                if user:
                    # Username exists, update the score
                    cursor.execute("UPDATE user_TABLE SET score = score + 1 WHERE username = %s", (username,))
                    app.state.conn.commit()

                    stored_username = user[0]  # Adjust the index if necessary
                    response_content = {
                        "fulfillmentText": f"Correct, {stored_username}! Your score is now {user[1] + 1}."
                    }
                else:
                    # Username doesn't exist, handle accordingly
                    response_content = {
                        "fulfillmentText": "Username not found. Please provide a valid username."
                    }
            else:
                # No matching question found
                response_content = {
                    "fulfillmentText": f"Good luck next time! Your current score is {user[1] if user else 0}."
                }

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        # Close the cursor within a finally block
        cursor.close()

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

@app.post("/")
async def handle_request(request: Request):
    cursor = None
    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor = mysql.connector.connect(**db_config).cursor()
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index if necessary
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[1]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                cursor.connection.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

        elif intent_display_name == "answer":
            # Extract the user's response
            user_response = payload.get('queryResult', {}).get('parameters', {}).get('text')

            # Find a matching question in QUE_table based on user's response
            cursor = mysql.connector.connect(**db_config).cursor()
            cursor.execute("SELECT * FROM que_table WHERE answer = %s", (user_response,))
            matching_question = cursor.fetchone()

            # Retrieve the username from the payload
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if matching_question:
                if user:
                    # Username exists, update the score
                    cursor.execute("UPDATE user_TABLE SET score = score + 1 WHERE username = %s", (username,))
                    cursor.connection.commit()

                    stored_username = user[0]  # Adjust the index if necessary
                    response_content = {
                        "fulfillmentText": f"Correct, {stored_username}! Your score is now {user[1] + 1}."
                    }
                else:
                    # Username doesn't exist, handle accordingly
                    response_content = {
                        "fulfillmentText": "Username not found. Please provide a valid username."
                    }
            else:
                # No matching question found
                response_content = {
                    "fulfillmentText": f"Good luck next time! Your current score is {user[1] if user else 0}."
                }

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        # Close the cursor within a finally block if it's not None
        if cursor:
            cursor.close()

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}

def get_db_cursor():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

def close_db_connection(connection, cursor):
    cursor.close()
    connection.close()

@app.post("/")
async def handle_request(request: Request):
    connection, cursor = get_db_cursor()

    try:
        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user['username']
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user['score']}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                connection.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

        elif intent_display_name == "answer":
            # Extract the user's response
            user_response = payload.get('queryResult', {}).get('parameters', {}).get('text')

            # Find a matching question in QUE_table based on the user's response
            cursor.execute("SELECT * FROM que_table WHERE answer = %s", (user_response,))
            matching_question = cursor.fetchone()

            # Retrieve the username from the payload
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if matching_question:
                if user:
                    # Username exists, update the score
                    cursor.execute("UPDATE user_TABLE SET score = score + 1 WHERE username = %s", (username,))
                    connection.commit()

                    stored_username = user['username']
                    response_content = {
                        "fulfillmentText": f"Correct, {stored_username}! Your score is now {user['score'] + 1}."
                    }
                else:
                    # Username doesn't exist, handle accordingly
                    response_content = {
                        "fulfillmentText": "Username not found. Please provide a valid username."
                    }
            else:
                # No matching question found
                response_content = {
                    "fulfillmentText": f"Good luck next time! Your current score is {user['score'] if user else 0}."
                }

    except Exception as e:
        # Log any exceptions for debugging
        print("Error processing request:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        # Close the cursor and connection within a finally block
        close_db_connection(connection, cursor)

    # Return a default response if no specific condition is met
    return JSONResponse(content={"fulfillmentText": "Default response"})
'''
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import mysql.connector

app = FastAPI()

# Replace these values with your actual MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "APARNA",
    "database": "bot",
}


@app.post("/")
async def handle_request(request: Request):
    try:
        # Move connection setup and cursor creation inside the request handler
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Retrieve the JSON data from the request
        payload = await request.json()

        # Logging for debugging
        print("Received Payload:", payload)

        # Extract the necessary information from the payload
        intent_display_name = payload['queryResult']['intent']['displayName']
        print("Intent Display Name:", intent_display_name)

        # Check if the intent matches your expected intent
        if intent_display_name == "username":
            # Extract additional information if needed
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Username exists, do something with the existing user
                stored_username = user[0]  # Adjust the index if necessary
                response_content = {
                    "fulfillmentText": f"Welcome back, {stored_username}! Your current score is {user[1]}"
                }
            else:
                # Username doesn't exist, insert into the database
                cursor.execute("INSERT INTO USER_TABLE (username, score) VALUES (%s, %s)", (username, 0))
                stored_username = username
                conn.commit()
                response_content = {
                    "fulfillmentText": f"Welcome, {stored_username}! Your score is now set to 0."
                }

        elif intent_display_name == "answer":
            # Extract the user's response
            user_response = payload.get('queryResult', {}).get('parameters', {}).get('text')

            # Find a matching question in QUE_table based on user's response
            cursor.execute("SELECT * FROM que_table WHERE answer = %s", (user_response,))
            matching_question = cursor.fetchone()

            # Retrieve the username from the payload
            parameters = payload['queryResult']['parameters']
            username = parameters.get('person', {}).get('name')

            # Check if the username already exists in the database
            cursor.execute("SELECT * FROM user_TABLE WHERE username = %s", (username,))
            user = cursor.fetchone()

            if matching_question:
                if user:
                    # Username exists, update the score
                    cursor.execute("UPDATE user_TABLE SET score = score + 1 WHERE username = %s", (username,))
                    conn.commit()

                    stored_username = user[0]  # Adjust the index if necessary
                    response_content = {
                        "fulfillmentText": f"Correct, {stored_username}! Your score is now {user[1] + 1}."
                    }
                else:
                    # Username doesn't exist, handle accordingly
                    response_content = {
                        "fulfillmentText": "Username not found. Please provide a valid username."
                    }
            else:
                # No matching question found
                response_content = {
                    "fulfillmentText": f"Your answer is incorrect. Your current score is {user[1] if user else 0}. Try again next time."
                }

        else:
            # If the intent is not recognized, provide a default response
            response_content = {"fulfillmentText": "Default response"}

        # Send the response using the stored username or default response
        return JSONResponse(content=response_content)

    except mysql.connector.Error as e:
        # Log any MySQL-related exceptions for debugging
        print("MySQL Error:", str(e))
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        # Close the cursor and connection in a finally block
        cursor.close()
        conn.close()
