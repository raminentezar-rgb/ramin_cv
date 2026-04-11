from django.core.management.base import BaseCommand
from portfolio.models import Category, Project, Skill, Experience
from datetime import date

class Command(BaseCommand):
    help = 'Seed initial data for Ramin Entezar portfolio with full alignment across all sections'

    def handle(self, *args, **kwargs):
        # Clear existing data to ensure exact match
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        
        # Categories for Services
        bot_cat, _ = Category.objects.get_or_create(name="Bot Development", icon="fas fa-robot")
        web_cat, _ = Category.objects.get_or_create(name="Web Applications", icon="fas fa-code")
        soft_cat, _ = Category.objects.get_or_create(name="Software Dev", icon="fas fa-laptop-code")
        mkt_cat, _ = Category.objects.get_or_create(name="Marketing & Content", icon="fas fa-bullhorn")
        mobile_cat, _ = Category.objects.get_or_create(name="Mobile Dev", icon="fas fa-mobile-screen-button")

        # 6 Core Services/Projects
        services = [
            {
                'title': "Omnichannel Bot Development",
                'cat': bot_cat,
                'desc': "Intelligent bots for Telegram, WhatsApp, and Instagram tailored for all business sectors and industries.",
                'slug': "omnichannel-bots"
            },
            {
                'title': "Infinite Desktop Solutions",
                'cat': soft_cat,
                'desc': "High-performance, intelligent desktop applications with unlimited functional capabilities for complex tasks.",
                'slug': "desktop-apps"
            },
            {
                'title': "Smart Full-Stack Web Development",
                'cat': web_cat,
                'desc': "Modern, world-class full-stack web solutions built with the smartest and most cutting-edge global methods.",
                'slug': "fullstack-web"
            },
            {
                'title': "Strategic SEO & Digital Marketing",
                'cat': mkt_cat,
                'desc': "Comprehensive SEO strategies and digital marketing services to maximize online visibility and growth.",
                'slug': "seo-marketing"
            },
            {
                'title': "AI-Powered Content Production",
                'cat': mkt_cat,
                'desc': "Advanced audio, video, and text content creation using the latest global technologies for all platforms.",
                'slug': "content-production"
            },
            {
                'title': "Cross-Platform Mobile Apps",
                'cat': mobile_cat,
                'desc': "Premium mobile application development for both Android and iOS, delivering seamless user experiences.",
                'slug': "mobile-apps"
            }
        ]

        for s in services:
            Project.objects.create(
                title=s['title'],
                category=s['cat'],
                description=s['desc'],
                slug=s['slug'],
            )

        # Updated Skills
        skills_data = [
            ('Bot & API Integration', 95, 'Bot Development'),
            ('Instagram/WA Automation', 90, 'Bot Development'),
            ('Intelligent Desktop software', 88, 'Software Dev'),
            ('Performance Optimization', 85, 'Software Dev'),
            ('Full-Stack Web Dev', 92, 'Web Applications'),
            ('Modern Web Architecture', 90, 'Web Applications'),
            ('Digital Marketing & SEO', 85, 'Marketing & Content'),
            ('Strategic Growth', 80, 'Marketing & Content'),
            ('AI Content Generation', 88, 'Marketing & Content'),
            ('Multimedia Production', 82, 'Marketing & Content'),
            ('iOS & Android Development', 90, 'Mobile Dev'),
            ('Cross-Platform Experience', 85, 'Mobile Dev')
        ]
        
        for name, prof, cat in skills_data:
            Skill.objects.create(name=name, proficiency=prof, category=cat)

        # Updated Professional Journey Milestones
        experiences = [
            {
                'title': "Lead AI & Automation Specialist",
                'company': "Avrasya Üniversitesi (Consultancy)",
                'start': date(2023, 1, 1),
                'current': True,
                'desc': "Leading the development of AI-driven automation systems, including advanced Telegram/WhatsApp bots and intelligent content production workflows for university operations."
            },
            {
                'title': "Senior Full-Stack & Desktop Developer",
                'company': "Tech-Innovate Solutions",
                'start': date(2021, 6, 1),
                'end': date(2022, 12, 31),
                'current': False,
                'desc': "Engineered high-performance desktop applications and modern full-stack websites. Focused on performance optimization and scalable architecture using Django and Python."
            },
            {
                'title': "Digital Strategy & SEO Lead",
                'company': "Global Growth Media",
                'start': date(2019, 3, 1),
                'end': date(2021, 5, 30),
                'current': False,
                'desc': "Managed comprehensive SEO campaigns and digital marketing strategies. Developed cross-platform mobile apps to enhance client online presence and engagement."
            }
        ]

        for e in experiences:
            Experience.objects.create(
                job_title=e['title'],
                company=e['company'],
                start_date=e['start'],
                end_date=e.get('end'),
                is_current=e['current'],
                description=e['desc']
            )

        self.stdout.write(self.style.SUCCESS('Successfully updated all sections (Services, Skills, Experience)'))
