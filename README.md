# Pokemon Crawler

Project started from https://docs.docker.com/compose/django/

Some useful commands:

* `docker-compose up`
* `docker-compose exec web bash`
* `docker-compose exec web python -m pip install -r requirements.txt`

## Explainer

Data can be loaded using the `crawl` management command.
```
python manage.py crawl
```
This command uses [async pokemon api wrapper](https://github.com/beastmatser/aiopokeapi). Async api calls speed up data retrieval quiet a bit. Data is saved using an async version of `update_or_create` from Django 4.1. The command can be used both for creating and updating objects.

Pokémons can be viewed in the [admin panel](http://localhost:8000/admin/app/pokemon/), see `/admin/app/pokemon/`. Only the `description` field is editable since it doesn't come from the api.

## TODO

* test crawl management command, mock api calls
* use env vars in settings (e.g. https://github.com/sloria/environs)
* add linters (isort, flake8), code formatter (black)
* add ci/cd
* pin and hash dependencies (poetry/pip-tools)
