import requests


class GitLabScraper:
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.headers = {"Private-Token": token}

    def _url(self, path):
        return self.api_url + path

    def get(self, path, **kwargs):
        resp = requests.get(self._url(path), headers=self.headers)

        page = resp.headers.get("X-Page")
        next_page = resp.headers.get("X-Next-Page")

        page = int(page) if page and page.isdigit() else 0
        next_page = int(next_page) if next_page and next_page.isdigit() else 0

        # print(page, next_page)

        while page < next_page:
            self.get(path, page=page + 1)

    def gen_pagegnation_get(self, path, **kwargs):
        options = {"goto_page": 0, "optional_parameter": ""}
        options.update(kwargs)

        resp = requests.get(
            self._url(
                f"{path}?page={options['goto_page']}&per_page=100&{options['optional_parameter']}"
            ),
            # self._url(f"{path}"),
            headers=self.headers,
        )

        # http://gitlab-web/api/v4/projects?membership=false
        print(
            self._url(
                f"{path}?page={options['goto_page']}&per_page=100&{options['optional_parameter']}"
            )
        )
        page = resp.headers.get("X-Page")
        next_page = resp.headers.get("X-Next-Page")

        page = int(page) if page and page.isdigit() else 0
        next_page = int(next_page) if next_page and next_page.isdigit() else 0

        # print(page, next_page, page < next_page)

        if page < next_page:
            yield from self.gen_pagegnation_get(path, goto_page=next_page)

        yield resp.json()

    def get_all_pages(self, path, **kwargs):
        g = self.gen_pagegnation_get(path, **kwargs)
        l = []
        for i in g:
            if isinstance(i, list):
                l += i
            else:
                l.append(i)
        return l

    def get_me(self):
        return self.get_all_pages("/user")

    def get_my_projects(self):
        return self.get_all_pages(f"/projects", optional_parameter="membership=true")

    def get_user_projects(self, user_id):
        return self.get_all_pages(f"/users/{user_id}/projects")

    def get_project_languages(self, project_id):
        return self.get_all_pages(f"/projects/{project_id}/languages")

    def get_project_members(self, project_id):
        return self.get_all_pages(f"/projects/{project_id}/members")

    def get_user_events(self, user_id):
        return self.get_all_pages(f"/users/{user_id}/events")

    def get_my_groups(self):
        return self.get_all_pages("/groups?membership=true")

