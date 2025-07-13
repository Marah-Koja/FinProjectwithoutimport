import csv
from django.core.management.base import BaseCommand
from applications.models import Applications  # عدّل المسار حسب تطبيقك

class Command(BaseCommand):
    help = "Import application sentiment data from CSV"

    def handle(self, *args, **kwargs):
        file_path = 'app_sentiment_summary_roberta.csv'  # تأكد من المسار
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                app_id = row['app_id']
                total_comments = int(row['total_comments']) if row['total_comments'] else 0
                positive = float(row['positive %']) if row['positive %'] else 0.0
                negative = float(row['negative %']) if row['negative %'] else 0.0
                neutral = float(row['neutral %']) if row['neutral %'] else 0.0
                avg_rating = float(row['avg_rating']) if row['avg_rating'] else 0.0
                quality_score = float(row['app_quality_score']) if row['app_quality_score'] else 0.0

                # إنشاء أو تحديث السجل
                app, created = Applications.objects.update_or_create(
                    name=app_id,  # أو field فريد آخر مثل app_id إذا موجود
                    defaults={
                        'total_comments': total_comments,
                        'positive_percent': positive,
                        'negative_percent': negative,
                        'neutral_percent': neutral,
                        'avg_rating': avg_rating,
                        'app_quality_score': quality_score,
                    }
                )
                self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} {app_id}"))

        self.stdout.write(self.style.SUCCESS("✅ استيراد البيانات تم بنجاح"))