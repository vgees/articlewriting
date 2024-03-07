from openai import OpenAI
import streamlit as st


clt = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=‘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’

def main():
    st.title("Article Writer")
    notes = st.text_area("Enter Topic Information:")
    content = "I want you to write short literature review on topic "+notes
    if st.button("Generate Article"):
        with st.spinner("Generating Article..."):
            response = clt.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[{'role':'user','content':content}]
            )
        description = response.choices[0].message.content
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()

