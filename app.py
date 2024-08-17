from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

model_llama3_8b_8192 = "llama3-8b-8192"
model_llama31_8b_131k = "llama-3.1-8b-instant"

groq_key = "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"

chat = ChatGroq(temperature=0.5, groq_api_key = groq_key, model_name = model_llama3_8b_8192)

# each function stands for a step/level/test of feature

def s0_chat_invoke():
    """ 
    Simplest way to invoke a model: use the method invoke() of chat object. [invoke() implies it is a RUNNABLE]
    Langhchain handles the intermediate step of wrapping the string into an object HumanMessage
    """
    response = chat.invoke("Tell me a joke about bears!")
    print("s0: when asked a joke about bears: ", response.content)

def s1_prompt_template_invoke():
    """
    Use class ChatPromptTemplate to build a prompt before pushing it into the model.
    HumanMessage and SystemMessage are explored in this function
    """
    # create the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world class comedian."),
        ("human", "Tell me a joke about {topic}")
    ])

    # compose the prompt with invoke() -> when you see method invoke() it implies it is a RUNNABLE -> runnables can be chained
    #my_prompt = prompt.invoke({"topic": "pyramids"})
    #print("Prompt is: ", my_prompt)
    return prompt

def s2_first_chain():
    prompt = s1_prompt_template_invoke()
    chain = prompt | chat
    chain.invoke({'topic': 'pyramids'})
    str_chain = chain | StrOutputParser() 
    str_chain.invoke({'topic': 'pyramids'})
    print(chain)
    print(str_chain)


if __name__ == "__main__":
    # s0_chat_invoke()
    # s1_prompt_template_invoke()
    s2_first_chain()
