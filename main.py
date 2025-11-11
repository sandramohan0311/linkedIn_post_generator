import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_posts

length_options = ["short", "medium", "long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Gnerator: Codebasics")



    col1,col2,col3 = st.columns(3)
    fs = FewShotPosts()

    with col1:
       Selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        Selected_length = st.selectbox("Length", options=length_options)
    
    with col3:
        #dropdown for language
        Selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_posts(Selected_length,Selected_language,Selected_tag)
        # st.write(posts)
        st.write(post)


if __name__ == "__main__":
    main()