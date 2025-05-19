from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, MealRating
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def add_meal(request):
    if request.method == 'POST':
        name = request.POST['name']
        imageUrl = request.POST['imageUrl']
        countryOfOrigin = request.POST['countryOfOrigin']
        typicalMealTime = int(request.POST['typicalMealTime'])
        description = request.POST['description']

        Meal.objects.create(
            name=name,
            imageUrl=imageUrl,
            countryOfOrigin=countryOfOrigin,
            typicalMealTime=typicalMealTime,
            description=description,
            dateAdded=timezone.now()
        )
        # フォーム送信後、ランディングページへリダイレクト
        return redirect('landing')

    # POST以外の場合もランディングページにリダイレクト
    return redirect('landing')

@login_required
def landing_page(request):
    # まず全てのMealを取得
    all_meals = Meal.objects.all()
    
    # Top Rated（平均評価が4.5以上）
    high_rated = [m for m in all_meals if m.avgRating() >= 4.5]
    if not high_rated:
        # もし4.5以上の食事が一つも無い場合、全体から平均評価が高い順に3件取得
        top_rated = sorted(all_meals, key=lambda m: m.avgRating(), reverse=True)[:3]
    else:
        # 4.5以上の食事が存在する場合は、その中から最大3件
        top_rated = high_rated[:3]

    context = {
        'morning_meals': Meal.objects.filter(typicalMealTime=Meal.MORNING)[:3],
        'afternoon_meals': Meal.objects.filter(typicalMealTime=Meal.AFTERNOON)[:3],
        'evening_meals': Meal.objects.filter(typicalMealTime=Meal.EVENING)[:3],
        # 最近追加された（現在から 90 日以内）
        'recently_added': Meal.objects.filter(dateAdded__gte=timezone.now() - timezone.timedelta(days=90))[:3],
        # 上で判定したtop_ratedを格納
        'top_rated': top_rated,
    }
    return render(request, 'landing.html', context)

@login_required
def category_list(request, meal_time):
    # meal_time の値に応じたフィルタリング
    if meal_time == 4:  # Recently Added：現在から 90 日以内
        threshold = timezone.now() - timezone.timedelta(days=90)
        meals = Meal.objects.filter(dateAdded__gte=threshold)
    elif meal_time == 5:  # Top Rated：平均評価が 4.5 以上
        all_meals = Meal.objects.all()
        top_meals = [m for m in all_meals if m.avgRating() >= 4.5]
        # 該当する食事がなければ、全体から平均評価の高い食事を上位 3 件表示
        if not top_meals:
            meals = sorted(all_meals, key=lambda m: m.avgRating(), reverse=True)[:3]
        else:
            meals = top_meals
    else:
        meals = Meal.objects.filter(typicalMealTime=meal_time)

    # ソートオプション（rating, country, date）による並び替え
    sort_by = request.GET.get('sort')
    if sort_by == 'rating':
        meals = sorted(meals, key=lambda m: m.avgRating(), reverse=True)
    elif sort_by == 'country':
        meals = sorted(meals, key=lambda m: m.countryOfOrigin)
    elif sort_by == 'date':
        meals = sorted(meals, key=lambda m: m.dateAdded, reverse=True)

    category_names = {
        1: "Morning",
        2: "Afternoon",
        3: "Evening",
        4: "Recently Added",
        5: "Top Rated"
    }
    context = {'meals': meals, 'category_name': category_names.get(meal_time, '')}
    return render(request, 'category_list.html', context)

@login_required
def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    context = {'meal': meal}
    return render(request, 'meal_detail.html', context)

@login_required
def rate_meal(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'POST':
        rating = float(request.POST.get('rating'))
        MealRating.objects.create(
            meal=meal,
            rating=rating,
            dateOfRating=timezone.now()
        )
    return redirect('meal_detail', meal_id=meal_id)
