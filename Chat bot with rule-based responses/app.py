import streamlit as st
from rag_with_palm import RAGPaLMQuery
import KeywordMatching as kw
# import NLPclassifier as nlp

# Instantiate the class
rag_palm_query_instance = RAGPaLMQuery()

st.title(f"**Book Recommender Assistant**📚")  # Add emojis and colors to the title
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Need info? Drop your question here!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    classification, keyword = kw.classify_user_input(prompt)
    
    # classification = nlp.classify_user_input_bert(prompt)
    if classification == "General":
        model_response = rag_palm_query_instance.query_response(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(model_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": model_response})
    else:
        model_response = rag_palm_query_instance.query_response(prompt)
        response = "This will be generated from ML model"
        combined_response = str(model_response) + "\n\n" + response
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            # st.markdown("As you're interested in **{}**, I recommend you the following books:".format(keyword))
            st.markdown(combined_response)
        # Add assistant responses to chat history
        st.session_state.messages.append({"role": "assistant", "content": combined_response})

    
    