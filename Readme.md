## Search Engine Integration with LangChain

This project demonstrates the integration of multiple search Engines and tools using LangChain. It provides a Streamlit web interface to query various search engines and APIs, enabling users to compare results across platforms like DuckDuckGo, Google, Serper API, Brave, and Wikipedia.

# Features

DuckDuckGo Search: Query DuckDuckGo for immediate and privacy-focused search results.

Google Search API: Fetch recent results using Google Search.

Serper API: Utilize Serper API for refined search queries.

Brave Search API: Leverage Brave's API for privacy-centric search results.

Wikipedia Query: Retrieve information directly from Wikipedia using LangChain utilities.

Streamlit Interface: Simple and interactive UI to input questions and view results from all tools.

File Overview

File Name: Search.py

This file contains:

Import statements for LangChain tools, utilities, and Streamlit.

Functions to perform searches using each tool.

A Streamlit app for user interaction.


Prerequisites

Environment Variables

Ensure the following API keys are set as environment variables:

HUGGINGFACEHUB_API_TOKEN: Hugging Face API token.

GOOGLE_CSE_ID and GOOGLE_API_KEY: Google Custom Search Engine and API keys.

SERPER_API_KEY: Serper API key.

Brave API Key: Brave Search API key.

Example:
```
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "HuggingFaceKey"
os.environ["GOOGLE_CSE_ID"] = "KEY"
os.environ["GOOGLE_API_KEY"] = "KEY"
os.environ["SERPER_API_KEY"] = "KEY"
 ```
Installation

Clone the repository:
```
git clone https://github.com/ahmadsameh8/Searching_Agent.git
cd Searching_Agent
```
Install the dependencies:
```
pip install -r requirements.txt
```
Run the Streamlit application:
```
streamlit run Search.py
```
How It Works

Launch the Streamlit app.

Enter a question or query in the text input box.

Click "Submit" to retrieve results from the following tools:

DuckDuckGo, Google Search, Serper API, Wikipedia, Brave Search

View the results displayed in the application interface.

Key Technologies

LangChain: Orchestrates the integration of multiple search APIs and utilities.

Streamlit: Creates an interactive and user-friendly web app.

Hugging Face Hub: Provides an LLM (e.g., BLOOM) for future enhancements.

