from core.repositories import PostRepository
from core.repositories import UserRepository

class UnlikePostsService:
    def execute(self, username, post_id):
        
        user_repository = UserRepository()
        post_repository = PostRepository()

        user_exist = user_repository.find_one(username)

        if (user_exist):
            user_id = user_exist[0]
            response = post_repository.unlike(
                user_id,
                post_id
            )
            return response
        else:
            return False