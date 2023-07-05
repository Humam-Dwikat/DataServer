from repo.repos import Repo


class TweetOperation:
    """
    handled the operation from Repo
    """
    def __init__(self, repo: Repo):
        self.repo = repo

    def get_tweet(self, index_name: str):
        """
        Get tweet from index
        """
        return self.repo.get_tweet(index_name=index_name)
