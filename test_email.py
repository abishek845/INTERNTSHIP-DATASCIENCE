import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("21bit101@americancollege.edu.in", "uhmy kiqa fzqz euaz")
    server.sendmail("21bit101@americancollege.edu.in", "strokerboy3@gmail.com", "Test Email: Fire Alert System Works!")
    print("✅ Email sent successfully!")
    server.quit()
except Exception as e:
    print("❌ Error:", e)
