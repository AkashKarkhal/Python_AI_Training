log_msg = ["INFO", "DEBUG", "WARNING", "ERROR", "INFO", "CRITICAL", "WARNING"]

for logs in log_msg:

    if logs == "CRITICAL":
        break

    if logs == "INFO":
        continue

    if logs == "WARNING" or logs == "ERROR":
        print(logs)