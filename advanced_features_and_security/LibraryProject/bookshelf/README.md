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
