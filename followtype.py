from enum import Enum


class FollowType(Enum):
    followers = 'followers'
    following = 'following'

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @staticmethod
    def argparse(s):
        try:
            return FollowType[s]
        except KeyError:
            return s
