import os
from openai import OpenAI

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