!pip install langchain langchain-google-genai langchain_experimental mysql-connector-python-rf

import getpass
import os
import langchain
import langchain_google_genai

os.environ["GOOGLE_API_KEY"]= 'AIzaSyA7mO8b51xqWmDyH0ijZETCxDdWv-xkAuI'

from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///Chinook.db")

from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

from langchain.prompts import PromptTemplate
import mysql.connector

explain_prompt_template: str = """
You are an expert data analyst called 'Datable'. Explain and analyze the sql query results. Use the following format:
'''
's/'SQL Result :'s/'{sql_result}'s/'
's/'Answer:'s/'What you want to explain to the User's/'
'''

Tables schema:
CREATE TABLE user (
  ID int(6) NOT NULL AUTO_INCREMENT,
  Password varchar(255) NOT NULL,
  User_Name varchar(255) NOT NULL,
  Department_ID int(6) NOT NULL,
  Admin_ID int(6),
  PRIMARY KEY (ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID),
  FOREIGN KEY (Admin_ID) REFERENCES user (ID)
);

CREATE TABLE log (
  Log_ID int(6) NOT NULL AUTO_INCREMENT,
  Item_ID int(6) NOT NULL,
  User_ID int(6) NOT NULL,
  Department_ID int(6) NOT NULL,
  Log_Borrow_Date datetime NOT NULL,
  Log_Return_Date datetime NOT NULL,
  Log_Status tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (Log_ID),
  FOREIGN KEY (Item_ID) REFERENCES item (Item_ID),
  FOREIGN KEY (User_ID) REFERENCES user (ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID)
);

CREATE TABLE item (
  Item_ID int(6) NOT NULL AUTO_INCREMENT,
  Item_Name varchar(255) NOT NULL,
  Department_ID int(6) NOT NULL,
  Admin_ID int(6),
  PRIMARY KEY (Item_ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID),
  FOREIGN KEY (Admin_ID) REFERENCES user (ID)
);

CREATE TABLE department (
  Department_ID int(6) NOT NULL AUTO_INCREMENT,
  Department_Name varchar(255) NOT NULL,
  PRIMARY KEY (Department_ID)
);

CREATE TABLE category (
  Category_Name varchar(255) NOT NULL,
  Item_ID int(6) NOT NULL,
  PRIMARY KEY (Category_Name),
  FOREIGN KEY (Item_ID) REFERENCES item (Item_ID)
);
"""

prompt_template: str = """
You are an expert data analyst called 'Datable'. Given an input question: {user_question}. First create a syntactically correct query to run, tell the user. Use the following format:
'''
's/'Use_SQL:'s/'Y or N's/'
's/'SQLQuery:'s/'SQL Query to run's/'
's/'Answer:'s/'What you want to tell the User's/'
'''

Only use the following tables schema:
CREATE TABLE user (
  ID int(6) NOT NULL AUTO_INCREMENT,
  Password varchar(255) NOT NULL,
  User_Name varchar(255) NOT NULL,
  Department_ID int(6) NOT NULL,
  Admin_ID int(6),
  PRIMARY KEY (ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID),
  FOREIGN KEY (Admin_ID) REFERENCES user (ID)
);

CREATE TABLE log (
  Log_ID int(6) NOT NULL AUTO_INCREMENT,
  Item_ID int(6) NOT NULL,
  User_ID int(6) NOT NULL,
  Department_ID int(6) NOT NULL,
  Log_Borrow_Date datetime NOT NULL,
  Log_Return_Date datetime NOT NULL,
  Log_Status tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (Log_ID),
  FOREIGN KEY (Item_ID) REFERENCES item (Item_ID),
  FOREIGN KEY (User_ID) REFERENCES user (ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID)
);

CREATE TABLE item (
  Item_ID int(6) NOT NULL AUTO_INCREMENT,
  Item_Name varchar(255) NOT NULL,
  Department_ID int(6) NOT NULL,
  Admin_ID int(6),
  PRIMARY KEY (Item_ID),
  FOREIGN KEY (Department_ID) REFERENCES department (Department_ID),
  FOREIGN KEY (Admin_ID) REFERENCES user (ID)
);

CREATE TABLE department (
  Department_ID int(6) NOT NULL AUTO_INCREMENT,
  Department_Name varchar(255) NOT NULL,
  PRIMARY KEY (Department_ID)
);

CREATE TABLE category (
  Category_Name varchar(255) NOT NULL,
  Item_ID int(6) NOT NULL,
  PRIMARY KEY (Category_Name),
  FOREIGN KEY (Item_ID) REFERENCES item (Item_ID)
);
"""
explain_prompt = PromptTemplate.from_template(template=explain_prompt_template)
prompt = PromptTemplate.from_template(template=prompt_template)

def run_sql_query(stop, input_a):
  if input_a == "Y":
    explain_prediction = "Connecting..."
    print(explain_prediction)
    stop += 1
    try:
      con = mysql.connector.connect(host="localhost", user="admin", password="admin")
      cursor = con.cursor()

      cursor.execute(sql_query)
      table = cursor.fetchall()
      explain_prompt_formatted_str: str = explain_prompt.format(sql_result=table)
      explain_prediction = llm.predict(explain_prompt_formatted_str)
      print(explain_prediction)
    except:
      explain_prediction = "An exception occurred. Can't connect."
      print(explain_prediction)
      stop += 2
  else:
    explain_prediction = "Cancel. No action has been taken."
    stop += 2
    print(explain_prediction)

user_question = input("Type your question: ")
print("====================================")

prompt_formatted_str: str = prompt.format(user_question=user_question)
prediction = llm.predict(prompt_formatted_str)

sections = prediction.split("'s/'")
use_SQL = sections[2]
SQLQuery = sections[5]
Answer = sections[(len(sections)-2)]
if use_SQL == "N":
  bot_message = Answer
  print(bot_message)
elif use_SQL == "Y":
  sql_query = SQLQuery
  print(f"""
==================================================================

Do you sure to run this sql query? Say 'Y' to run, 'N' to cancel.

SQL Query:
'''
{sql_query}
'''

==================================================================
  """)
  input_a = input()
  stop = 0
  run_sql_query(stop, input_a)