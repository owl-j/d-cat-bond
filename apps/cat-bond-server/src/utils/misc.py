import os

from utils.repo_path_manager import RepoPathManager


def get_path_to_dot_env():
    if os.environ is None:
        return RepoPathManager().dot_env_dev
    else:
        try:
            env = os.environ["env"]
            if env == "dev":
                return RepoPathManager().dot_env_dev
            elif env == "prod":
                return RepoPathManager().dot_env_prod
        except KeyError:
            return RepoPathManager().dot_env_dev
