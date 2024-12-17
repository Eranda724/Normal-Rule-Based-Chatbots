import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("Mental_Health_FAQ.csv")
df = df.drop("Question_ID", axis=1)

vec = TfidfVectorizer()
vec.fit(np.concatenate((df["Questions"], df["Answers"])))
df_vec = vec.transform(df["Questions"])

def get_response(input_q):
    input_qvec = vec.transform([input_q])
    similarity = cosine_similarity(input_qvec, df_vec)
    close_answer = np.argmax(similarity, axis=1)
    return df["Answers"].iloc[close_answer].values[0]

if __name__ == "__main__":
    print("Hello! How can I help you? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
