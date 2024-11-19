# errorsalert.py
# The send_email function is defined here to enable you to run
# the code, but of course it doesn't send an actual email.
def send_email(*a):
    print(*a)


alert_system = "console"  # other value can be "email"
error_severity = "critical"  # other values: "medium" or "low"
error_message = "Something terrible happened!"

if alert_system == "console":  # outer
    print(error_message)  # 1
elif alert_system == "email":
    if error_severity == "critical":  # inner
        send_email("admin@example.com", error_message)  # 2
    elif error_severity == "medium":
        send_email("support.1@example.com", error_message)  # 3
    else:
        send_email("support.2@example.com", error_message)  # 4
