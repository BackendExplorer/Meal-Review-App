from django.db import models
from django.utils import timezone

class Meal(models.Model):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    MEAL_TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl = models.URLField(max_length=200)
    countryOfOrigin = models.CharField(max_length=50)
    typicalMealTime = models.IntegerField(choices=MEAL_TIME_CHOICES)
    dateAdded = models.DateTimeField(default=timezone.now)

    def avgRating(self):
        ratings = self.mealrating_set.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 2)
        return 0.0

    def numberOfVotes(self):
        return self.mealrating_set.count()

class MealRating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    rating = models.FloatField()
    dateOfRating = models.DateTimeField(default=timezone.now)
