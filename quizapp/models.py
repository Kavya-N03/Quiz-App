from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text
    
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    answer_text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text