import os
import github

gh = None


def get_repos_for_org(organization):
    all_repos = gh.get_user().get_repos()
    for repo in all_repos:
        if repo.archived:
            continue

        if repo.owner.login != organization:
            continue

        yield repo


if __name__ == '__main__':
    gh = github.Github(os.environ["PAT"])

    repos = get_repos_for_org("crossgovernmentservices")
    for repo in repos:
        repo.edit(archived=True)
        is_archived = "{}archived".format("not " if not repo.archived else "")
        print("{} is {}".format(repo.clone_url, is_archived))
