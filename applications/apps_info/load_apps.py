from .models import Applications

apps_data = [
    {
        "name": "MyFitnessPal",
        "package_id": "com.myfitnesspal.android",
        "description": (
            " هو تطبيق للصحة والتغذية يساعدك على تتبع عاداتك الغذائية، "
            "مراقبة النظام الغذائي وتحقيق أهدافك الصحية. يحتوي على قاعدة بيانات ضخمة "
            "مع خيارات تسجيل الطعام عبر المسح الضوئي للباركود."
        ),
        "image_path": "app_images/myfitnesspal.jpg",
        "rating": 4.6,
    },
    {
        "name": "Headspace",
        "package_id": "com.getsomeheadspace.android",
        "description": (
            " هو تطبيق للصحة النفسية والتأمل اليومي يساعدك على الاسترخاء، "
            "خفض التوتر وتحسين التركيز. يقدم جلسات توجيه بالصوت لتخفيف القلق وتحسين النوم."
        ),
        "image_path": "app_images/headspace.jpg",
        "rating": 4.5,
    },
    {
        "name": "Fitbit",
        "package_id": "com.fitbit.FitbitMobile",
        "description": (
            " تطبيق لتتبع النشاط والصحة، يسجل عدد الخطوات، نبض القلب، "
            "التمارين والنوم، ويعرض تحليلات شاملة ويرتبط بأجهزة Fitbit الأخرى."
        ),
        "image_path": "app_images/fitbit.jpg",
        "rating": 4.2,
    },
    {
        "name": "Nike Training Club",
        "package_id": "com.nike.ntc",
        "description": (
            " هو تطبيق تمارين متنوع من ، يقدم خطط تمارين "
            "منتظمة بدون معدات، وجهود موجهة من مدربين معتمدين."
        ),
        "image_path": "app_images/nike.jpg",
        "rating": 4.4,
    },
    {
        "name": "Medisafe",
        "package_id": "com.medisafe.android.client",
        "description": (
            " هو تذكير ذكي للدواء يساعدك على متابعة الأدوية والمواعيد، "
            "ويقدم تنبيهات لضمان الجرعة الصحيحة في الوقت المناسب."
        ),
        "image_path": "app_images/medisafe.jpg",
        "rating": 4.7,
    },
    {
        "name": "Glucose Buddy",
        "package_id": "com.skyhealth.glucosebuddyfree",
        "description": (
            " هو تطبيق لإدارة السكري يساعد على تسجيل مستوى السكر في الدم، "
            "الطعام، الأدوية والنشاط لتعقب وتحسين الصحة."
        ),
        "image_path": "app_images/glucosebuddy.jpg",
        "rating": 4.1,
    },
    {
        "name": "Blood Pressure Monitor",
        "package_id": "bloodpressuremonitor.bloodpressureapp.bpmonitor",
        "description": (
            " يساعد على تتبع ضغط الدم، تسجيل قراءاتك اليومية، "
            "وتوليد تقارير سهلة الفهم."
        ),
        "image_path": "app_images/bpmonitor.jpg",
        "rating": 4.3,
    },
    {
        "name": "Lasting",
        "package_id": "com.lasting.connect",
        "description": (
            "هو تطبيق لعلاقات الأزواج يقدم جلسات افتراضية ونصائح حساسة "
            "لتقوية العلاقة والتواصل بشكل أفضل."
        ),
        "image_path": "app_images/lasting.jpg",
        "rating": 4.5,
    },
    {
        "name": "BetterHelp",
        "package_id": "com.betterhelp",
        "description": (
            " هو منصة علاج اونلاين تتيح للمستخدمين التواصل مع معالجين "
            "مرخصين عبر المراسلة أو المكالمات."
        ),
        "image_path": "app_images/betterhelp.jpg",
        "rating": 4.6,
    },
    {
        "name": "Calm",
        "package_id": "com.calm.android",
        "description": (
            " هو تطبيق تأمل ونوم مشهور يقدم قصص النوم، تمارين التنفس التعليمية، "
            "ومقاطع صوتية للاسترخاء."
        ),
        "image_path": "app_images/calm.jpg",
        "rating": 4.7,
    },
    {
        "name": "Moodfit",
        "package_id": "com.robleridge.Moodfit",
        "description": (
            " هو تطبيق لتحسين الصحة النفسية يساعدك "
            "على تتبع مزاجك، ضغطك واضطرابات النوم، ويقدم إرشادات لتحسين الحالة."
                      ),
        "image_path": "app_images/moodfit.jpg",
        "rating": 4.4,
    },
    {
        "name": "Clue",
        "package_id": "com.clue.android",
        "description": (
            " هو تطبيق لتتبع الدورة الشهرية يقدم تنبؤات دقيقة للدورة، "
            "صحّة الإنجاب والنشاط البدني الخاص بالمرحلة."
        ),
        "image_path": "app_images/clue.jpg",
        "rating": 4.3,
    },
    {
        "name": "Flo",
        "package_id": "com.cube.arc.fa",
        "description": (
            " هو تقويم للخصوبة والدورة الشهرية يقدم نصائح للحمل، تتبع الأعراض، "
            "وتذكيرات يومية."
        ),
        "image_path": "app_images/flo.jpg",
        "rating": 4.8,
    },
    {
        "name": "Ada",
        "package_id": "com.ada.app",
        "description": (
            " هو تطبيق مدعوم بالذكاء الاصطناعي لفحص الأعراض، يساعدك على "
            "فهم حالتك الصحية وتوجيهك لاتخاذ الخطوات الصحيحة."
        ),
        "image_path": "app_images/ada.jpg",
        "rating": 4.6,
    },
    {
        "name": "Healow",
        "package_id": "com.ecw.healow",
        "description": (
            " هو تطبيق لإدارة السجلات الطبية، المواعيد والوصفات، "
            "يساعدك على متابعة صحتك مع مقدمي الرعاية."
        ),
        "image_path": "app_images/healow.jpg",
        "rating": 4.2,
    },
]

for app in apps_data:
    App.objects.get_or_create(**app)