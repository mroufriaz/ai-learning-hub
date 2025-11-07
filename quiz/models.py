from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Question(models.Model):
    text = models.TextField()
    # options stored as JSON list of strings: ["opt1","opt2","opt3","opt4"]
    options = models.JSONField()
    # index of the correct option (0-based)
    correct_index = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0)],
        help_text="0-based index of the correct option"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # short preview
        return (self.text[:80] + '...') if len(self.text) > 80 else self.text

    def clean(self):
        # Ensure correct_index less than options length
        if self.options is None or not isinstance(self.options, list) or len(self.options) == 0:
            raise ValidationError("Options must be a non-empty list.")
        if self.correct_index >= len(self.options):
            raise ValidationError("correct_index must be less than the number of options.")
