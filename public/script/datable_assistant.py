from assistant_setup import assistant_setup
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
  run_sql_query()