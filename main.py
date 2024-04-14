from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b")

response = llm.invoke("who is capital of pakistan")
print(response)