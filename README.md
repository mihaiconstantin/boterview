<p align="center">
    <a href="https://boterview.mihaiconstantin.com">
        <img width="180px" src="assets/images/boterview-logo.png" alt="boterview logo"/>
    </a>
</p>

<h1 align="center">
    <sub>AI-based interview studies...<br>...as smooth as butter</sub>
</h1>

<!-- badges: start -->
<p align="center">
    <a href="https://www.repostatus.org/#wip"><img src="https://www.repostatus.org/badges/latest/wip.svg" alt="Repository status"/></a>
    <a href="https://github.com/mihaiconstantin/boterview/releases"><img src="https://img.shields.io/github/v/release/mihaiconstantin/boterview?display_name=tag&sort=semver" alt="GitHub version"/></a>
    <a href="https://boterview.mihaiconstantin.com"><img src="https://img.shields.io/badge/docs-website-brightgreen" alt="Documentation website"/></a>
    <a href="https://raw.githubusercontent.com/mihaiconstantin/boterview/main/assets/design/boterview-design.svg"><img src="https://img.shields.io/badge/design-diagram-brightgreen" alt="Software design diagram"/></a>
</p>
<!-- badges: end -->

`boterview` is a `Python` package that enables social science researchers to
easily deploy chatbot-based interviews with customizable protocols and
randomized condition assignment.

## Installation

You can install the development version of `boterview` from `GitHub`, and once
the package reaches a stable version, directly from the `PyPI` repository.

*Optional.* You may choose to create a new `Python` virtual environment.

```bash
# Create a new `Python` virtual environment called `.venv`.
python -m venv .venv

# Activate the virtual environment.
source .venv/bin/activate
```

Install the package from `GitHub`.

```bash
# Install using `pip`.
pip install boterview@git+https://github.com/mihaiconstantin/boterview
```

## Usage

To use `boterview`, you need to specify the configuration of your study in a
`Python` script. For example, suppose you are interesting in a study conducting
interviews for participants randomly assigned to one of two conditions, where
each condition has a different interview guide. For clarity, `boterview` allows
users to specify their different parts of the interview (i.e., including the
system model prompt) in separate files. You can implement the this setup as
follows:

```python
# Import packages.
import os
from boterview import Boterview


# Get the `OpenAI` API key from the environment.
openai_api_key = os.getenv("OPENAI_API_KEY")

# Specify the model settings.
model_settings = {
    "model": "gpt-4o"
}

# Create a boterview instance.
boterview = Boterview()

# Configure the study.
boterview.set_study_name(
    name = "A Study"
)

# Set the first condition (e.g., with a specific interview guide).
boterview.set_study_condition(
    name = "Condition 1",
    prompt = "path/to/prompt.txt",
    protocol = "path/to/protocol.txt",
    introduction = "path/to/introduction.txt",
    closing = "path/to/closing.txt",
    guide = "path/to/guide-condition-1.txt"
)

# Set the second condition (e.g., with a different interview guide).
boterview.set_study_condition(
    name = "Condition 1",
    prompt = "path/to/prompt.txt",
    protocol = "path/to/protocol.txt",
    introduction = "path/to/introduction.txt",
    closing = "path/to/closing.txt",
    guide = "path/to/guide-condition-2.txt"
)

# Preview a condition.
boterview.preview_condition("Condition 1")

# To be continued...
```

At this point, you can run the study using the following command:

```bash
# Run the study.
boterview run app.py
```

## Contributing

- Any contributions are welcome and greatly appreciated. Please open a [pull
  request](https://github.com/mihaiconstantin/boterview/pulls) on `GitHub`.
- To report bugs, or request new features, please open an
  [issue](https://github.com/mihaiconstantin/boterview/issues) on `GitHub`.

## License

The package source code in this repository is licensed under the [MIT
license](https://opensource.org/license/mit).
