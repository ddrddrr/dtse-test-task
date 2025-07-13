# AIS Backend Developer Assignment

A service which provides a REST API for house-price predictions.  
It loads a pre-trained model (`model.joblib`) and exposes a prediction endpoint which uses it.

# Installation

1. Clone the repo `git clone https://github.com/ddrddrr/dtse-test-task`
2. Switch to the project dir `cd dtse-test-task`
3. Create an `.env` file and set the variables according to the desired mode of running
   (see `.env.example` and `.env.prod.example`)

# Running with Docker

1. Run `docker compose up`. That will fetch the latest built image for the service
   and the Caddy(proxy) image.
2. By default the proxy is listening at `http://localhost`.
   The server is not accessible from the local machine, as it runs in an isolated Docker network.
5. Try out the API(e.g., via Swagger, see #Try out the API).

# Running in development mode

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Run `uv sync --locked` to install the dependencies.
   That will automatically create the `.venv` directory and download all needed packages.
2. Highly recommended to [install direnv](https://direnv.net/#basic-installation)
   in order to easily manage .env files. If installed, don't forget
   to [hook your shell to it](https://direnv.net/docs/hook.html).
   Then you will be able to just write `direnv allow` in the project directory to load the env vars from
   the `.env` file.
3. If not using `direnv`, export the variables manually in your shell, e.g.:

```sh
DJANGO_SETTINGS_MODULE=house_prices.settings.base
DEBUG=True
```

4. In the directory where the `manage.py` script is located(`cd house_prices`) run
   `uv run manage.py migrate && uv run manage.py runserver`.
   This will initialize the database and start the development server.
5. By default the proxy is listening at `http://localhost:8000`.
5. Try out the API(e.g., via Swagger, see #Try out the API).

# Try out the API

The simplest way to test out the API is to use the endpoint with Swagger - `http://localhost/api/docs/swagger`.
Don't forget to set the port in the url for the development server.

The Swagger docs are protected by Authentication. On the default page the unauthenticated
users will see only two endpoints:
- `/api/users/login/`
- `/api/users/register/`

First, click on the **register** endpoint and then on the **Try it out** button located on the right.
Scroll down and click the **Execute** button
(the default example data will suffice, no need to provide custom email/password).
Scroll down and find the response, it should have the 201 code indicating that the user was created.

Now copy the credentials you've used in the registration step and click on the **login** endpoint. Again, click
on the **Try it out** button and paste the credentials in the request body, click **Execute**.
In the response body you will find data similar to:

```json
{
  "expiry": "2025-07-13T13:19:48.807123Z",
  "token": "d44263a1c00b5..."
}
```

Copy the token. On the top right(of the whole window) find the `Authorize` button, click it and in the **Value**
field insert `Token *your copied token*`, click `Authorize`.
Close the auth window and the prediction endpoint should appear.

Try it out, either with the predefined value or your own.

# Tech stack

- `uv` is used as the project and dependency manager.
- The service is built using **Django 5.2** and `django-rest-framework` package.
- The python version used is `3.10`(see #Notes for explanation).
- SQLite is used as the database, as this is a small project and SQLite requires little to none setup.
- Docker, Docker Compose and Caddy(proxy) are used for *Near-Production* setup.
- The CI/CD pipeline is realised via GitHub Actions.
  The code for the `test` and `build` workflows can be found under `.github/workflows` directory.
- The authentication method chosen was databased-stored tokens. Since the purpose of the API is not
  known(Web Service x Public API x Server-to-Server API), JWTs, Session Auth or API Keys were ruled out.
  Database-stored tokens allow us to use the API everywhere, albeit, not being the perfect solution for
  all use-cases.

# Notes

- The newest python version compatible with `scikit-learn==1.1.2` is 3.10. Newer
  versions fail with OpenMP/clang build error. Newer `scikit-learn` versions are not
  compatible with the bundled prediction model.
- Database is not included in the project files, as the sqlite file is created on the first
  interaction of `Django` with the database (and it shouldn't be in general).
- The model, on the other hand, is included in the repo, again, due to simplicity.
- API is not versioned, as there will be no future versions:)
- Swagger docs are served by `Django`, which is not ideal, but sufficient for this project.
- No proper protections are implemented(CORS, CSRF, etc.) as the domain of the API is not known.
- The solution is not "Production-Ready" per se, as proxy is configured to work with HTTP only
  (to enable local testing), the registration workflow does not have any verification of the user, etc. 