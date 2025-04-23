# prompt-engineering
Explore the power of in-context learning by designing effective prompts to perform various software engineering tasks. The goal is to compare GPT-4o and GPT-4.1 using two different prompting strategies, zero-shot prompting and role-playing prompting. Each strategy is applied to the two models by `prompt_engineering.py` and the results are saved to a csv file. These results can be quantitatively analyzed and compared using `evaluation.py`, which generates graphs using different metrics depending on whether the results are natural langauge or code-based. These graphs can be found in the `./graphs` directory.

In this project, 22 tasks are compared between the different models and strategies. These cover Code Summarization, Code Generation, Code Completion, Bug Fixing, and Bug Detection.

The existing prompts are saved in `prompts.csv` and the model responses are saved in `prompts_with_responses.csv`.

# Installation:
1. Install [python 3.9+](https://www.python.org/downloads/) locally
2. Clone the repository to your workspace:  
```shell
~ $ git clone https://github.com/arya-anathema/prompt-engineering.git
```
3. Navigate into the repository:
```shell
~ $ cd prompt-engineering
~/prompt-engineering $
```
4. Set up a virtual environment and activate it:
```shell
~/ngram-recommender $ python -m venv ./venv/
```
- For macOS/Linux:
```shell 
~/prompt-engineering $ source venv/bin/activate
(venv) ~/prompt-engineering $ 
```
- For Windows:
```shell
~\prompt-engineering $ .\venv\Scripts\activate.bat
(venv) ~\prompt-engineering $ 
```

5. To install the required packages: 
```shell
(venv) ~/prompt-engineering $ pip install -r requirements.txt
```

6. Generate a [GitHub Personal Access Token](https://github.com/settings/personal-access-tokens) and copy the contents to `token.txt` in the root directory.

# Running the Program
1. Generate `prompts_with_responses.csv` based on the contents of `prompts.csv` file:
```shell
python prompt-engineering.py
```
2. Generate new graphs to `./graphs` based on the contents of `prompts_with_responses.csv` file:

# Report

The assignment report is available in the file `Report.pdf`.
