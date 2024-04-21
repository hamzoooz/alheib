from django.db import models


LEVEL = (
    ('p1', 'p1'),
    ('p2', 'p2'),
    ('p3', 'p3'),
    ('p4', 'p4'),
    ('p5', 'p5'),
    ('p6', 'p6'),
    ('p7', 'p7'),
    ('NURS', 'NURS'),
    ('OUT', 'OUT'),
    ('CHOICE', 'CHOICE'),
    )

dormitory = (
    ('ABUBAKAR', 'ABUBAKAR'),
    ('AISHA', 'AISHA'),
    ('ALI', 'ALI'),
    ('AANNEX HADIJAHLI', 'ANNEX HADIJAH'),
    ('FAROOQ', 'FAROOQ'),
    ('HADIJAH', 'HADIJAH'),
    ('UTHUMAN', 'UTHUMAN'),
    ('ZAHARAH', 'ZAHARAH'),
    ('HOME', 'HOME'),
    ('OUT', 'OUT'),
    
    )

sponsorship_source = (    
    ('الهيئة', 'الهيئة'),
    ('بيت الزكاة', 'بيت الزكاة'),
    )

residence_status = (    
    ('خارجي', 'خارجي'),
    ('داخلي', 'داخلي'),
    )

sponsorship_status = (    
                      
    ('CONTINUED', 'CONTINUED'),
    ('DROPPED', 'DROPPED'),
    )

system = (    
    ('P.D', 'P.D'),
    ('P.B', 'P.B'),        
    ('TEACHER', 'TEACHER'),        
    ('COM', 'COM'),        
    ('DIRECTOR IICO', 'DIRECTOR IICO'),        
    )

quran_memorization = (    
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    )


class Student(models.Model):
    name = models.CharField(blank=True, null=True , max_length=255, verbose_name="الاسم - NAME")
    arabic_name = models.CharField(blank=True, null=True , max_length=255, verbose_name="الاسم عربي")
    account_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم الحساب - ACCOUNT NO")
    account_holder_name = models.CharField(blank=True, null=True , max_length=255, verbose_name="اسم صاحب الحساب")
    orphan_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم اليتيم - ORPHAN NO")
    sponsor_no =  models.IntegerField(blank=True, null=True , verbose_name="رقم الكافل - SPONSOR'S NO")
    date_of_birth = models.DateField(blank=True, null=True , verbose_name="تاريخ الميلاد - DATE OF BIRTH")
    date_of_death = models.DateField(blank=True, null=True , verbose_name="تاريخ الوفاة - DATE OF DEATH" )
    school = models.CharField(blank=True, null=True , max_length=255, verbose_name="المدرسة - SCHOOL")
    system = models.CharField(blank=True, null=True , max_length=255, verbose_name="النظام - system" , choices=system, default='CHOICE'  )
    level = models.CharField(blank=True, null=True , max_length=255, verbose_name="المرحلة - LEVEL", choices=LEVEL, default='CHOICE' )
    
    # class_name = models.CharField(blank=True, null=True , max_length=255, verbose_name="الصف - CLASS")
    quran_memorization = models.CharField(blank=True, null=True , max_length=255, verbose_name="مقدار الحفظ من القرآن" ,  choices=quran_memorization, default='0' )
    talents = models.CharField(blank=True, null=True , max_length=255, verbose_name="المواهب")
    abilities = models.CharField(blank=True, null=True , max_length=255, verbose_name="القدرات")
    residence_status = models.CharField(blank=True, null=True , max_length=255, verbose_name="السكن داخلي / خارجي"  , choices=residence_status, default='داخلي')
    dormitory = models.CharField(blank=True, null=True , max_length=255, verbose_name="المهجع", choices=dormitory, default='ABUBAKAR', )
    sponsorship_status = models.CharField(blank=True, null=True , max_length=255,choices=sponsorship_status, default='CONTINUED', verbose_name="الكفالة مستمرة أم توقف - SPONSORSHIP CONTINUE OR STOP")
    sponsorship_source = models.CharField(blank=True, null=True , max_length=255, verbose_name="جهة الكفالة الهيئة/بيت الزكاة - SPONSORSHIP IICO OR ZAKAT" , choices=sponsorship_source, default='الهيئة', )
    last_payment = models.CharField(blank=True, null=True , max_length=255, verbose_name="آخر صرفية استلمها - LAST PAYMENT")
    date_received = models.DateField(blank=True, null=True , verbose_name="تاريخ الاستلام- DATE OF RECEIVING")
    district = models.CharField(blank=True, null=True , max_length=255, verbose_name="المحافظة - DISTRICT")
    area = models.CharField(blank=True, null=True , max_length=255, verbose_name="المنطقة - AREA")
    guardian = models.CharField(blank=True, null=True , max_length=255, verbose_name="ولي الأمر - GUARDIAN")
    phone_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم الهاتف - PHONE NO")
    whatsapp_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم الواتس - WHATSAPP")
    other_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم آخر - OTHER NO")
    attachments = models.CharField(blank=True, null=True , max_length=255, verbose_name="المرفقات - ATTACHEMENTS")
    weight = models.CharField(blank=True, null=True , max_length=255, verbose_name="الوزن")
    height = models.CharField(blank=True, null=True , max_length=255, verbose_name="الطول")
    shoe_size = models.CharField(blank=True, null=True , max_length=255, verbose_name="مقاس الحذاء")
    thobe_size = models.CharField(blank=True, null=True , max_length=255, verbose_name="مقاس الجلابية")
    guardian_id_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم هوية ولي الأمر")
    health_status = models.CharField(blank=True, null=True , max_length=255, verbose_name="الحالة الصحية")
    quarterly_evaluation = models.CharField(blank=True, null=True , max_length=255, verbose_name="التقدير الفصلي")
    educational_level = models.CharField(blank=True, null=True , max_length=255, verbose_name="المستوى التعليمي")
    registrar_notes = models.CharField(blank=True, null=True , max_length=255, verbose_name="ملاحظات المسجل")
    director_notes = models.CharField(blank=True, null=True , max_length=255, verbose_name="ملاحظات المدير")
    school_notes = models.CharField(blank=True, null=True , max_length=255, verbose_name="ملاحظات المدرسة")
    tuition_fees = models.CharField(blank=True, null=True , max_length=255, verbose_name="الرسوم الدراسية")
    paid_amount = models.CharField(blank=True, null=True , max_length=255, verbose_name="المدفوع")
    payment_date = models.DateField(blank=True, null=True , verbose_name="تاريخ الدفع")
    bank_notification_no = models.CharField(blank=True, null=True , max_length=255, verbose_name="رقم الإشعار البنكي")
    balance = models.CharField(blank=True, null=True , max_length=255, verbose_name="الباقي")
    services = models.CharField(blank=True, null=True , max_length=255, verbose_name="الخدمات")

    def __str__(self):
        return self.name
