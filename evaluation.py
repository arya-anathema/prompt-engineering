
from rouge_score import rouge_scorer, scoring
import evaluate
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np
import seaborn as sns
import sacrebleu
import os


rouge = evaluate.load("rouge")
meteor = evaluate.load("meteor")
bleu = evaluate.load("bleu")

def getRougeScore(text1,text2):
  results = rouge.compute(predictions=[text1],references=[text2])
  return results['rouge2']

def getMeteorScore(text1,text2):
  results = meteor.compute(predictions=[text1],references=[text2])
  return results['meteor']

def getBleuScore(text1,text2):
  results = bleu.compute(predictions=[text1],references=[text2])
  return results['bleu']

def calcSacreBleu(str1,str2):
  #if it is too short, return a small value
  if(len(str1.split())<4 or len(str2.split())<4):
    return 0.0000000001
  else:
    predlist = [str1]
    actulist = [[str2]]
    bleu = sacrebleu.corpus_bleu(predlist,actulist)

    return bleu.score

def getMatrix(responses,function):
    n = len(responses)

    matrix = pd.DataFrame(index=model_names, columns=model_names, dtype=float)

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix.iloc[i, j] = 1.0  # Perfect match
            else:
                ij = function(responses[i], responses[j])
                ji = function(responses[j], responses[i])
                matrix.iloc[i, j] = (ij + ji) / 2  # Symmetric average

    return matrix

def makeGraph(matrix,title,questionNumber=""):

  mask = np.triu(np.ones_like(matrix, dtype=bool))

  plt.figure(figsize=(8, 6))
  sns.heatmap(matrix, annot=True, fmt=".2f", cmap="YlGnBu", square=True, mask=mask)
  plt.title(f"{title} {questionNumber}")
  #plt.show()

  output_dir = "graphs"
  os.makedirs(output_dir, exist_ok=True)

  safe_title = title.replace(" ", "_").replace(":", "").replace("/", "_")
  filename = os.path.join(output_dir, f"{safe_title}_{questionNumber}.png")
  plt.savefig(filename, bbox_inches='tight')

def makeAllNaturalLangGraphs(responses):

  bleuSum = None
  rougeSum = None
  meteorSum = None

  for response in responses:
      num = response[0]
      the_response = response[1:]
      print(num)
      print(the_response)
      bleuMatrix = getMatrix(the_response, getBleuScore)
      rougeMatrix = getMatrix(the_response, getRougeScore)
      meteorMatrix = getMatrix(the_response, getMeteorScore)

      if bleuSum is None:
          bleuSum = np.array(bleuMatrix)
          rougeSum = np.array(rougeMatrix)
          meteorSum = np.array(meteorMatrix)
      else:
          bleuSum += bleuMatrix
          rougeSum += rougeMatrix
          meteorSum += meteorMatrix

      makeGraph(bleuMatrix, "Pairwise Bleu Score Comparison Question", num)
      makeGraph(rougeMatrix, "Pairwise Rouge Score Comparison Question", num)
      makeGraph(meteorMatrix, "Pairwise Meteor Score Comparison Question", num)



  bleuAvg = bleuSum / len(responses)
  rougeAvg = rougeSum / len(responses)
  meteorAvg = meteorSum / len(responses)

  makeGraph(bleuAvg, "Pairwise Bleu Score Comparison Average")
  makeGraph(rougeAvg, "Pairwise Rouge Score Comparison Average")
  makeGraph(meteorAvg, "Pairwise Meteor Score Comparison Average")

"""
def makeAllCodeLangGraphs(responses):

  bleu4Sum = None
  F1Sum = None

  for response in responses:
      num = response[0]
      the_response = response[1:]
      print(num)
      print(the_response)
      bleu4Matrix = getMatrix(the_response, calcSacreBleu)
      F1Matrix = getMatrix(the_response, calcF1Score)

      if bleu4Sum is None:
          bleu4Sum = np.array(bleu4Matrix)
          F1Sum = np.array(F1Matrix)
      else:
          bleu4Sum += bleu4Matrix
          F1Sum += F1Matrix

      makeGraph(bleu4Matrix, "Pairwise Bleu-4 Score Comparison Question", num)
      makeGraph(F1Matrix, "Pairwise F1 Score Comparison Question", num)



  bleu4Avg = bleu4Sum / len(responses)
  F1Avg = F1Sum / len(responses)

  makeGraph(bleu4Avg, "Pairwise Bleu-4 Score Comparison Average")
  makeGraph(F1Avg, "Pairwise F1 Score Comparison Average")
"""

df = pd.read_csv("prompts_with_responses.csv")

columns=["task_no","4o zero-shot", "4o role-play", "4.1 zero-shot", "4.1 role-play"]
model_names = ["gpt-4o zero shot" , "gpt-4o roleplaying", "gpt-4.1 zero shot", "gpt-4.1 roleplaying"]

responses = df[columns].values.tolist()

nat_lang_responses = []
code_responses = []

#1 nat lang
nat_lang_responses.append(responses[0])
#2 nat lang code
responses_2_code = ["2","def sum_range(start, end): total = 0 for i in range(start, end + 1): # Include `end` in the range total += i return total","def sum_range(start, end): total = 0 for i in range(start, end + 1): # Include the end value total += i return total","def sum_range(start, end): total = 0 for i in range(start, end + 1): total += i return total","def sum_range(start, end): return sum(range(start, end + 1))"]
code_responses.append(responses_2_code)
#3 nat lang
nat_lang_responses.append(responses[2])
#4 code
code_responses.append(responses[3])
#5 code
code_responses.append(responses[4])
#6 code
code_responses.append(responses[5])
#7 nat lang
nat_lang_responses.append(responses[6])
#8 code
code_responses.append(responses[7])
#9 code
code_responses.append(responses[8])
#10 nat lang
nat_lang_responses.append(responses[9])
#11 nat lang
nat_lang_responses.append(responses[10])
#12 code
code_responses.append(responses[11])
#13 code
code_responses.append(responses[12])
#14 code
code_responses.append(responses[13])
#15 code
code_responses.append(responses[14])
#16 code
code_responses.append(responses[15])
#17 code
code_responses.append(responses[16])
#18 nat lang code
responses_18_code = ["18","isEven(n) { return n % 2 === 0; // Returns true for even numbers and false for odd numbers }","isEven(n) { return n % 2 === 0; // Returns true for even, false for odd }","function isEven(n) { return n % 2 === 0; }","isEven(n) { return n % 2 === 0; }"]
code_responses.append(responses[17])
#19 nat lang
nat_lang_responses.append(responses[18])
#20 code
code_responses.append(responses[19])
#21 nat lang code
nat_lang_responses.append(responses[20])
#22 code
code_responses.append(responses[21])


makeAllNaturalLangGraphs(nat_lang_responses)
