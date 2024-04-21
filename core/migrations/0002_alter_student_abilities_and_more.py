# Generated by Django 5.0.1 on 2024-04-21 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='abilities',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='القدرات'),
        ),
        migrations.AlterField(
            model_name='student',
            name='account_holder_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم صاحب الحساب'),
        ),
        migrations.AlterField(
            model_name='student',
            name='account_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الحساب - ACCOUNT NO'),
        ),
        migrations.AlterField(
            model_name='student',
            name='arabic_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الاسم عربي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المنطقة - AREA'),
        ),
        migrations.AlterField(
            model_name='student',
            name='attachments',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المرفقات - ATTACHEMENTS'),
        ),
        migrations.AlterField(
            model_name='student',
            name='balance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الباقي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='bank_notification_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الإشعار البنكي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الصف - CLASS'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ الميلاد - DATE OF BIRTH'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_received',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ الاستلام- DATE OF RECEIVING'),
        ),
        migrations.AlterField(
            model_name='student',
            name='director_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ملاحظات المدير'),
        ),
        migrations.AlterField(
            model_name='student',
            name='district',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المحافظة - DISTRICT'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dormitory',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المهجع'),
        ),
        migrations.AlterField(
            model_name='student',
            name='educational_level',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المستوى التعليمي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ولي الأمر - GUARDIAN'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_id_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم هوية ولي الأمر'),
        ),
        migrations.AlterField(
            model_name='student',
            name='health_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الحالة الصحية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='height',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الطول'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_payment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='آخر صرفية استلمها - LAST PAYMENT'),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المرحلة - LEVEL'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الاسم - NAME'),
        ),
        migrations.AlterField(
            model_name='student',
            name='orphan_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم اليتيم - ORPHAN NO'),
        ),
        migrations.AlterField(
            model_name='student',
            name='other_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم آخر - OTHER NO'),
        ),
        migrations.AlterField(
            model_name='student',
            name='paid_amount',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المدفوع'),
        ),
        migrations.AlterField(
            model_name='student',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاريخ الدفع'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الهاتف - PHONE NO'),
        ),
        migrations.AlterField(
            model_name='student',
            name='quarterly_evaluation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='التقدير الفصلي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='quran_memorization',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مقدار الحفظ من القرآن'),
        ),
        migrations.AlterField(
            model_name='student',
            name='registrar_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ملاحظات المسجل'),
        ),
        migrations.AlterField(
            model_name='student',
            name='residence_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='السكن داخلي / خارجي'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المدرسة - SCHOOL'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ملاحظات المدرسة'),
        ),
        migrations.AlterField(
            model_name='student',
            name='services',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الخدمات'),
        ),
        migrations.AlterField(
            model_name='student',
            name='shoe_size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مقاس الحذاء'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsor_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="رقم الكافل - SPONSOR'S NO"),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsorship_source',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='جهة الكفالة الهيئة/بيت الزكاة - SPONSORSHIP IICO OR ZAKAT'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsorship_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الكفالة مستمرة أم توقف - SPONSORSHIP CONTINUE OR STOP'),
        ),
        migrations.AlterField(
            model_name='student',
            name='talents',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='المواهب'),
        ),
        migrations.AlterField(
            model_name='student',
            name='thobe_size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مقاس الجلابية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tuition_fees',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الرسوم الدراسية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='weight',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='الوزن'),
        ),
        migrations.AlterField(
            model_name='student',
            name='whatsapp_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم الواتس - WHATSAPP'),
        ),
    ]
