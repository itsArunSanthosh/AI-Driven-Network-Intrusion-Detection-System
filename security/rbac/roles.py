"""
Role-Based Access Control (RBAC).
"""

ROLE_PERMISSIONS = {
    "admin": ["read", "write", "delete"],
    "analyst": ["read", "write"],
    "viewer": ["read"]
}

def has_permission(role: str, action: str) -> bool:
    return action in ROLE_PERMISSIONS.get(role, [])