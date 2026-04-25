"""
Central security enforcement layer.
"""

from auth.auth import authenticate
from rbac.roles import has_permission
from audit_logging.audit_logger import AuditLogger


class SecurityManager:
    def __init__(self):
        self.audit_logger = AuditLogger()

    def authorize(self, api_key: str, role: str, action: str, user="unknown"):
        if not authenticate(api_key):
            return False, "Authentication failed"

        if not has_permission(role, action):
            return False, "Permission denied"

        self.audit_logger.log(action, user)

        return True, "Access granted"