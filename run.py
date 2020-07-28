from app import create_app
from app.config.dev import DevConfig

from app.gitlab import buildUser

if __name__ == "__main__":
    app = create_app(DevConfig)
    user = buildUser("https://gitlab.htl-villach.at/api/v4", "cgXzRS5F-5HxRcLkiQxp")
    print(user["projects"][0]["events"])
    app.run(**DevConfig.RUN_SETTING)
