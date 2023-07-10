from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun, Tool, BraveSearch, WikipediaQueryRun
from langchain.utilities import GoogleSearchAPIWrapper,GoogleSerperAPIWrapper,WikipediaAPIWrapper
import os
from langchain import  HuggingFaceHub
import streamlit as st

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm=HuggingFaceHub(repo_id="bigscience/bloom")

def searchDuckDuckGo(inputText):
  search = DuckDuckGoSearchRun()
  return (search.run(inputText))

def googleSearch(inputText):
  os.environ["GOOGLE_CSE_ID"] = "e537a6ebee00944ae"
  os.environ["GOOGLE_API_KEY"] = "AIzaSyAoqW-8TgiLNFYUEwZZ692kxFXRaqKnXTI"
  search = GoogleSearchAPIWrapper()
  tool = Tool(
      name="Google Search",
      description="Search Google for recent results.",
      func=search.run,)
  return (tool.run(inputText))

def serperApi(inputText):
  os.environ["SERPER_API_KEY"] = "08c40fa92dadc0d27cc04ea66a91843bf527b617"
  search = GoogleSerperAPIWrapper()
  tools = [
      Tool(
          name="Intermediate Answer",
          func=search.run,
          description="useful for when you need to ask with search",
      )
    ]
  search = GoogleSerperAPIWrapper()
  results = search.run(inputText)
  return results

def braveSearch(inputText):
  api_key = "BSAv1neIuQOsxqOyy0sEe_ie2zD_n_V"
  tool = BraveSearch.from_api_key(api_key=api_key, search_kwargs={"count": 1})
  return (tool.run(inputText))

def wikipedia(inputText):
  wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
  return (wikipedia.run(inputText))

st.set_page_config(page_title="Agent research Skill", page_icon=":page_facing_up:")


st.title("Test the Agent Skill")
st.write("Enter a Question and see the answer of different Search Engines")

user_input = st.text_input('Enter your question: ')
submit = st.button("Submit")
if submit:
    st.write("\n# Search Duck Duck go result: ") 
    st.write(searchDuckDuckGo(user_input))
    st.write("\n# Google search results: ")
    st.write(googleSearch(user_input))
    st.write("\n# Serper Api results: " )
    st.write(serperApi(user_input))
    st.write("\n# wikipedia results: " )
    st.write(wikipedia(user_input))
    st.write("\n# Brave results: " )
    st.write(braveSearch(user_input))