from django.db import models

class SSCC(models.Model):
    extension_digit = models.PositiveIntegerField()
    gs1_prefix = models.CharField(max_length=9)
    serial_reference_number = models.CharField(max_length=7)
    check_digit = models.PositiveIntegerField(blank=True, null=True)

    def calculate_check_digit(self):
        even_sum = sum(int(digit) for digit in self.gs1_prefix[1:] + self.serial_reference_number[0::2])
        odd_sum = sum(int(digit) for digit in self.serial_reference_number[1::2])
        total_sum = even_sum + (odd_sum * 3)
        if total_sum % 10 == 0:
            return 0
        else:
            return 10 - (total_sum % 10)

    def save(self, *args, **kwargs):
        if self.check_digit is None:
            self.check_digit = self.calculate_check_digit()
        super().save(*args, **kwargs)
