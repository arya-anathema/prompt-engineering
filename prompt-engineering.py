import os
from openai import OpenAI
import pandas as pd
from tqdm import tqdm


def get_response(max_tokens, model, temp, prompt, role=""):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{prompt}"},] if role == ""
        else [{"role": "system", "content": f"{role}"},{"role": "user", "content": f"{prompt}"},],
        max_tokens=max_tokens,
        temperature=temp,
        )
    return response.choices[0].message.content


def get_all_responses(max_tokens, temp, prompt, role):
    response_list = []
    for model in model_choices:
        response_list.append(get_response(max_tokens, model, temp, prompt))
        response_list.append(get_response(max_tokens, model, temp, prompt, role))
    return response_list

if __name__ == "__main__":
    # Create your PAT token by following instructions here:
    # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    # grab the token from the token.txt file
    with open("token.txt", "r") as f:
        os.environ["GITHUB_TOKEN"] = f.read().strip()


    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.environ["GITHUB_TOKEN"],
    )

    # List of available models
    model_choices = ["gpt-4o", "gpt-4.1"]

    df = pd.read_csv("prompts.csv")

    #create cols if they don't exist
    for col in ["4o zero-shot", "4o role-play", "4.1 zero-shot", "4.1 role-play"]:
        if col not in df.columns:
            df[col] = ""
        
    for index, row in tqdm(df.iterrows()):
        responses = get_all_responses(1024, 1, row['zero-shot'], row['roleplay-role'])
        df.at[index, "4o zero-shot"] = responses[0]
        df.at[index, "4o role-play"] = responses[1]
        df.at[index, "4.1 zero-shot"] = responses[2]
        df.at[index, "4.1 role-play"] = responses[3]

    df.to_csv("prompts_with_responses.csv", index=False)
