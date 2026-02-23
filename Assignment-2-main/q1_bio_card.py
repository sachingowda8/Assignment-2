import sys
sys.stdout.reconfigure(encoding='utf-8')

name = "Sachin M"
age = 21
course = "AI and Machine Learning"
college = "SJB Institute of Technology"
email = "gowdsachin2004@gmail.com"

# just print a nice box with my details
print("╔══════════════════════════════════════════╗")
print("║         STUDENT BIO CARD                 ║")
print("╠══════════════════════════════════════════╣")
print("║  Name    :", name, " " * (28 - len(name)), "║")
print("║  Age     :", age, "years", " " * 24, "║")
print("║  Course  :", course, " " * (18 - len(course)), "║")
print("║  College :", college[:28], " " * 2, "║")
print("║  Email   :", email, " " * (18 - len(email)), "║")
print("╚══════════════════════════════════════════╝")
