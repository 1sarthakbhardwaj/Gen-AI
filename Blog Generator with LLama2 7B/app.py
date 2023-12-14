import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# fucntions to get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):

    #LLAma 2 called from Ctransformers - used to call models directly from huggingface
    llm = CTransformers(model = 'models/llama-2-7b.Q2_K.gguf',
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01,
                        })
    
    # Prompt Template

    template= """
        Write a blog in {style} tone for a topic {text} withing 
        {no_words} words.
        """

    prompt = PromptTemplate(input_variables=["style", "text", "no_words"],
                        template=template)

# Generate the response

    response = llm(prompt.format(style=blog_style, text=input_text, no_words=no_words))
    print(response)
    return response



# frontend thing
st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')


st.header("Blog Generator")

input_text=st.text_input("Enter the Topic")

# creating two more columns for additional two more fields

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox("Mention the tone of the blog",('Conversational', 'Formal', 'Casual', 'humour'))   

submit = st.button("Generate") 

# Final response

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))