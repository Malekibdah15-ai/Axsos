from django.shortcuts import render, redirect
import random
from time import strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'post':
        location = request.post['location']
        gold_earned = 0
        color = 'green'
    if location == 'farm':
        gold_earned = random.randint(10, 20)
    elif location == 'cave':
        gold_earned = random.randint(5, 10)
    elif location == 'house':
        gold_earned = random.randint(2, 5)
    elif location == 'quest':
            gold_earned = random.randint(-50, 50)
            if gold_earned < 0:
                color = 'red'
    
    request.session['gold'] += gold_earned
    
           
    if gold_earned >= 0:
        message = f"Earned {gold_earned} golds from the {location}! ({strftime('%Y-%m-%d %H:%M:%S')})"
    else:
        message = f"Lost {abs(gold_earned)} golds on a {location}! ({strftime('%Y-%m-%d %H:%M:%S')})"
    
           
    activities = request.session['activities']
    activities.insert(0, {'message': message, 'color': color})
    request.session['activities'] = activities
    
    return redirect('/')  