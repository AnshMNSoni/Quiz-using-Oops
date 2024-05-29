# Quiz:
from qna import question_data
from rich.console import Console
import time

def clearall():
    console = Console()
    console.clear()

def change(score1, score2):
    for t in range(3, 0, -1):
        clearall()
        print(f"Score :: {score1}/{score2}")
        print(f"Next Question in {t} sec...")
        time.sleep(1)
              
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = []
for item in question_data:
    que = Question(item['text'], item['answer'])
    question_bank.append(que)

count1 = 0
count2 = 0
for ques in question_bank:
    clearall()
    
    print(ques.text, "\n")
    user_ans = input("Type (True/False): ").capitalize()
    if (user_ans == ques.answer):
        count1 += 1
        count2 += 1
        print(f"\nHurreh! Correct")
        time.sleep(2)
        change(count1, count2)
        
    else:
        count2 += 1
        print(f"\nOops! Incorrect")
        time.sleep(2)
        change(count1, count2)