# Heds Up For Life!

## Content

- [Heds Up For Life!]
  - [Content](#content)
  - [Installation](#installation)
    - [Local installation and development](#local-installation-and-development)
      - [Running the container in production mode locally](#running-the-container-in-production-mode-locally)
        - [Changing the group of public static and media folders](#changing-the-group-of-public-static-and-media-folders)
        - [Starting the containers](#starting-the-containers)
      - [Running the Django development server locally](#running-the-django-development-server-locally)
    - [Installing Pre-commit](#installing-pre-commit)
  - [Creating a minified bundle of JS and CSS files](#creating-a-minified-bundle-of-js-and-css-files)
    - [Requirements](#requirements)

## Installation

### Local installation and development

Clone the Git repo into a local folder:

```bash
git clone git@gitlab.com:marcelhekking/hedsupforlife.git
```

#### Running the container in production mode locally

With Docker, you can start a container in production mode.

##### Changing the group of public static and media folders

The web Docker performs actions under GI 1024 (e.g., running `collectstatic`). In the Docker files, a physical volume on the host is linked with folders inside Docker. To avoid permission errors:

- Create a public folder at the project level (next to `src`)
- Create `staticfiles` and `mediafiles` folders and run the following for both folders:

```bash
mkdir -p public/staticfiles && mkdir -p public/mediafiles
```

and execute the following `make` command (<https://www.gnu.org/software/make/>):

```bash
make 1024
```

##### Starting the containers

Go to the root of the project (`hedsupforlife`) and first (only to be done once) build the dev container with:

```bash
sudo docker build -t hedsupforlife-web:latest -f Dockerfile .
```

Then start the container with:

```bash
make docker
```

and shut id down with:

```bash
make down
```

#### Running the Django development server locally

Install the frontend:

```bash
yarn install
```

Create a Python virtual environmnet will all dependencies specified in the `pyproject.toml` installed:

```bash
uv sync
```

Create a database:

```bash
createdb hedsupforlife
```

Migrate the database and install a superuser. This is the admin as specified in `base.py`.

```bash
make rebuild
```

Start the Django development server

```bash
make runserver
```

### Installing Pre-commit

Pre-commit is a Python package to check code via git hooks before it ends up in a Git repo. Before committing, you need to install pre-commit. In the correct Python virtual environment, go to the root of the project (`hedsupforlife`) and run:

```bash
pre-commit install
```

To test, you can check existing files with pre-commit:

```bash
pre-commit run --all-files
```

## Creating a minified bundle of JS and CSS files

For modifying and effectively creating CSS and JS files, `watchify` is used. Changes to CSS and JS are observed and converted into a minified bundle. This minified bundle is deployed to production.

### Requirements

The following Node.js applications must be installed:

- browserify
- watchify
- uglify-js
- browserify-css

All dependencies can be installed with the `yarn install` command in the root of the project:

```bash
cd ~/../hedsupforlife$
yarn install
```

Start watchify to create a minified bundle 'on-the-fly':

```bash
cd ~/../hedsupforlife$
yarn run watchify
```
