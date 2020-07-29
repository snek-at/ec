import json

from app.gitlab.scraper import GitLabScraper


def buildUser(url, token):
    gls = GitLabScraper(url, token)

    user = gls.get_me()[0]

    user["projects"] = gls.get_my_projects()
    user["groups"] = gls.get_my_groups()
    user["events"] = gls.get_user_events(user["id"])

    for project in user["projects"]:
        project["members"] = gls.get_project_members(project["id"])
        project["languages"] = gls.get_project_languages(project["id"])
        project["events"] = [
            event for event in user["events"] if event["project_id"] == project["id"]
        ]

    return user
