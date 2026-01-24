"""
Permissions and Groups:
- Custom permissions on Book model:
  can_view, can_create, can_edit, can_delete
- Groups created via Django admin:
  Viewers: can_view
  Editors: can_view, can_create, can_edit
  Admins: all permissions
- Views protected using permission_required decorators
"""

# Security Measures Implemented

1. DEBUG turned off in production.
2. XSS and content sniffing protections enabled.
3. Cookies are secure (HTTPS only).
4. All forms include CSRF tokens.
5. ORM is used for queries to prevent SQL injection.
6. Optional CSP header implemented for XSS protection.
