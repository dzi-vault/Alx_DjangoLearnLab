Blog Post Management Features

ListView shows all posts.
DetailView shows single post.
CreateView allows authenticated users to create posts.
UpdateView and DeleteView allow only the author to modify or remove posts.

Author is automatically assigned using form_valid().
Permissions are enforced using LoginRequiredMixin and UserPassesTestMixin.

Comment System

- Users can view comments under each blog post.
- Only authenticated users can add comments.
- Only the comment author can edit or delete their comment.
- Comments are linked to their respective posts.

