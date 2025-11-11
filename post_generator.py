from llm_helper import llm
from few_shots import FewShotPosts


few_shots = FewShotPosts()


def get_length_str(lenght):
    if lenght == "short":
        return "1 to 5 lines"
    elif lenght == "medium":
        return "6 to 10 lines"
    elif lenght == "long":
        return "11 to 15 lines"
    

def get_prompt(length, language, tag):
    length_str = get_length_str(length)
    prompt = f'''
        Generate a LinkedIn post using the below information. No preamble.

        1. Topic: {tag}
        2. Length: {length_str}
        3. Language: {language}
        
        If the language is Hinglish, it means its a mix of english and hindi.
        The script for the generated post should be always in English.

    '''
    example = few_shots.get_filtered_posts(length, language, tag)

    if len(example) > 0:
        prompt += "4) Use the writing style as per the following exapmles"
        for i, post in enumerate(example):
            post_text = post["text"]
            prompt += f"\n\n Example {i+1} \n\n {post_text}\n\n"
            if i == 1:
                break

    return prompt
    

def generate_posts(length, language, tag):

    prompt = get_prompt(length, language, tag)

    response = llm.invoke(prompt)
    return response.content
    

if __name__ == "__main__":
    post =generate_posts("short","English","Job Search")
    print(post)