# Import libraries
from dotenv import load_dotenv
import openai
import langchain
import os
from langchain.llms import OpenAI

# Load the environment variables from the .env file
load_dotenv()


# Now fetch the API key from the environment variables
#my_key = os.getenv("OPENAI_API_KEY")
my_key="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"
# Initialize the OpenAI object with the fetched API key
llm = OpenAI(temperature=0, OPENAI_API_KEY= my_key)

# Example query
text = "Give me a spicy salmon sushi recipie"
print(llm(text))

