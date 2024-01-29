from django.shortcuts import render
from main.models import profile
import requests
# Create your views here.
def quizmain(request):
    prof = profile.objects.get(user=request.user)
    api_url = 'https://opentdb.com/api.php?amount=5&type=multiple'
    response = requests.get(api_url)
    if response.status_code == 200:
        questions_data = response.json()['results']

        # Format the questions data to match the structure in the frontend
        questions = []
        for q_data in questions_data:
            question = {
                'id': q_data['type'],  # Use a unique identifier based on the API response
                'question': q_data['question'],
                'options': [q_data['correct_answer']] + q_data['incorrect_answers'],
                'correct': q_data['correct_answer']
            }
            questions.append(question)

       # print(questions)
        return render(request, 'quiz.html', {'questions': questions, 'header_user': prof})

