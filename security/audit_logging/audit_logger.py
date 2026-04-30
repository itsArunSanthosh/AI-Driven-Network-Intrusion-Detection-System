import time

class AuditLogger:
    def log(self, action: str, user: str):
        print(f"[AUDIT] {time.time()} | {user} | {action}")