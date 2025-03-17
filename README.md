<p align="center">
    <a href="https://boterview.dev">
        <img width="180px" src="https://raw.githubusercontent.com/mihaiconstantin/boterview/refs/heads/main/frontend/app/src/assets/images/boterview-logo.png" alt="boterview logo"/>
    </a>
</p>

<h1 align="center">
    <sub>AI-based interview studies...<br>...as smooth as butter</sub>
</h1>

<!-- badges: start -->
<p align="center">
    <a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Repository status"/></a>
    <a href="https://github.com/mihaiconstantin/boterview/releases"><img src="https://img.shields.io/github/v/release/mihaiconstantin/boterview?display_name=tag&sort=semver" alt="GitHub version"/></a>
    <a href="https://pypi.org/project/boterview/"><img src="https://img.shields.io/pypi/v/boterview" alt="PyPI version"/></a>
    <a href="https://pypi.org/project/boterview/"><img src="https://img.shields.io/pepy/dt/boterview" alt="PyPI monthly downloads"/></a>
</p>
<!-- badges: end -->

`boterview` is a `Python` package that enables social science researchers to
easily deploy chatbot-based interviews with customizable protocols and
randomized condition assignment.

## Installation

You can install the package from the `PyPI` repository using `pip` as follows:

```bash
# Install using `pip`.
pip install boterview
```

Depending on your setup, you may consider using a `Python` virtual environment
before running the command above. For instance, you can create a new virtual
environment called `.venv` and activate it as follows:

```bash
# Create a new directory for your study.
mkdir my-study

# Move into the directory.
cd my-study

# Create a new `Python` virtual environment called `.venv`.
python -m venv .venv

# Activate the virtual environment.
source .venv/bin/activate
```

### Development Version

You may also install the development version of the package directly from the
`GitHub` repository using `pip` as follows:

```bash
# Install using `pip`.
pip install boterview@git+https://github.com/mihaiconstantin/boterview
```

## Usage

To use `boterview`, you need to specify a `TOML` configuration file for your
study, and provide several text files containing the interview-related content,
as well as the user interface content (e.g., the study instruction, consent
information and more). While all these things can be done manually, `boterview`
provides a command line interface (CLI) to help you with the process.

### Commands

To get started, you can run the command below to see all the available command
available in the `boterview` CLI.

```bash
# Show all available commands.
boterview --help
```

Boterview provides four main command groups: `generate`, `parse`, `preview`, and
`run`. For each command, please check the help message (i.e., via `--help`) to
see the available options and arguments.

### Content Generation

The `boterview generate` command can be used to generate various things related
to your study. It contains three main subcommands:

- `codes`: Used to generate participation codes for your study.
- `secret`: Used to generate a random secret required to run the study.
- `study`: Used to scaffold an example study setup.


## Data Parsing

The `boterview parse` command can be used to parse the study database. It is
used to extract the study data from the `sqlite` database and save it as a
`markdown` file.

### Condition Previewing

The `boterview preview` command can be used to preview a study condition given a
configuration file. This command prints to the console the content that
constitutes the system prompt for the bot for a given study condition.

## Running the Study

The `boterview run` command can be used to start a study based on a
configuration file. This command starts a web server that serves the study
interface and handles the chatbot interactions.

### Example

Below you can find a minimal example to get you started with `boterview`. The
commands below assume you have already installed the package.

```bash
# Scaffold a study in the current working directory with 100 participation codes, and include a secret.
boterview generate study --path . --quantity 100 --config study.toml --secret

# Preview the default condition setup.
boterview preview --config study.toml --condition "Condition 1"

# Run the study and save the data in the `boterview.db` database file.
boterview run --config study.toml --database boterview.db
```

At this point, you can access the study at
[http://localhost:8080](http://localhost:8080).

Suppose several participants have went through the study and you want to
download the data. You can do so by navigating to the `/download` endpoint. The
secret required to download the data is stored in the `study.toml` file (i.e.,
it was automatically included by the `--secret` flag used when scaffolding the
study).

Alternatively, use the `boterview parse` command against the database file,
which will extract the data and save it as a `markdown` file in the current
working directory. For example:

```bash
# Parse the study data.
boterview parse --config study.toml --database boterview.db
```

**_Note._** We are working on expanding the documentation and adding more
examples. For the time being, the instructions above should suffice to get you
started with `boterview`. We also recommend reading the comments in the study
configuration file, as well as the application interface default content. See
the *Contributing* section below for more information on how you can help.

## Contributing

- Any contributions are welcome and greatly appreciated. Please open a [pull
  request](https://github.com/mihaiconstantin/boterview/pulls) on `GitHub`.
- To report bugs, or request new features, please open an
  [issue](https://github.com/mihaiconstantin/boterview/issues) on `GitHub`.

## License

- The package source code in this repository is licensed under the [MIT
  license](https://opensource.org/license/mit).
- <p class="license-cc" xmlns:cc="https://creativecommons.org/ns#" xmlns:dct="https://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://boterview.dev">The documentation and other website materials</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://mihaiconstantin.com">Mihai Constantin</a> are licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0</a>.</p>
