# Changelog

## boterview 1.1.0

### Added
- Add functionality to reconstruct the message history and repopulate the chat
  interface based on the conversations stored in the database. This feature
  makes the interview more robust to interruptions (e.g., page reloads). Fixes
  #24.

### Changed
- Update default paths in template to `/interface` for UI content files, and
  `/interview` for interview files.
- Update `pyproject.toml` to exclude `CNAME` from source distribution build.
- Disable automatic scrolling to message in the chat window. This behavior was
  added after a recent update to `chainlit` (i.e., see [this
  issue](https://github.com/Chainlit/chainlit/issues/1992)).
- Various improvements to the frontend application.

### Fixed
- Fix participants getting reassigned to a new condition each time the chat page
  was reloaded. Closes #24.
- Fix issue with cookie names not being parsed correctly in Safari due to extra
  whitespace. Closes #18.
- Fix issue with hardcoded `localhost` URL. Now, the application can be served
  from any domain. The recommended way is to serve the static files from the
  same domain as the backend. However, one can also serve the static files from
  a different domain, in which case a reverse proxy should be used to prevent
  any `CORS` issues. In development, the `vite` server for the frontend is
  configured to proxy requests to the backend (i.e., the backend URL is provided
  to the frontend server via the `.env.development` file located at
  `/frontend/app/.env.development`). Closes #17.

## boterview 1.0.3

### Added
- Add `markdown` support in `PageContent` component. When the UI content is not
  provided as `HTML`, the component will render the content as `markdown`
  paragraphs, with support for various formatting options. The processing is
  done using the `react-markdown` library.

### Changed
- Update default UI content to feature `markdown` formatting for the
  introduction and consent pages.
- Update default system prompt to ensure the LLM does not copy the interview
  document to the chat.

## boterview 1.0.2

### Changed
- Update badges in `README.md`.
- Update heading capitalization in `CHANGELOG.md`.

## boterview 1.0.1

### Changed
- Update build artifacts to exclude unnecessary `assets/` directory.
- Update logo path in `README.md` to use use the `GitHub` raw link.
- Remove the `CC` license images from the `README.md` file do to rendering
  issues on `PyPI`.

## boterview 1.0.0

### Added
- Add service classes (i.e., `Boterview`, `Study`, `Counter`, `Prompt`,
  `Condition`, `Interview`, `Guide`, `Introduction`, `Protocol`, and `Question`)
  to manage study logic, participant assignment, and configuration.
- Add `React` frontend, including various components, pages, and hooks.
- Integrate `chainlit` lifecycle chat events (i.e., start, stop, message, and
  authentication) using an `OpenAI` async client.
- Add package CLI commands to:
  - generate a new study, application secret, and participation codes
  - parse study data to `markdown`
  - preview study conditions
  - run the study server
- Implement backend in `FastAPI`, including several API routes for participant
  authentication, consent, chat handling, and UI content retrieval.
- Add several database models for `Participant`, `Conversation`, and
  `Configuration`.
- Add several payload models for API request and response handling.
- Add helper functions for general utilities.
- Add helper functions for creating and decoding `JWT` tokens, as well as for
  parsing cookies to support secure authentication flows.
- Add helper functions to manage `chainlit` events, such as retrieving message
  history, sending stop messages, and determining when a conversation should
  end.
- Add helper functions for common database operations.
- Add context managers to ensure several objects are properly initialized when
  shared across the application.
- Add several services to manage core application logic, configuration, and
  study data.
- Add `hatch` build hook to prepare frontend assets for packaging.
- Add `pyproject.toml` build configuration to manage frontend assets and ensure
  proper packaging.
- Add `chainlit` configuration file with sensible defaults.
- Add `chainlit` styling overrides, theme, favicon, and translation files.
- Add option to intercept `chainlit` custom action events.

### Changed
- Refactored core services (`Study`, `Boterview`, `Configuration`, etc.) into
  dedicated modules under `services/` (previously under `backend/`).
- Improved error handling, updated documentation, and optimized configuration
  handling.

### Fixed
- Ensure the template `TOML` generation uses `POSIX` path separators.

### Security
- Implement `JWT` authentication and token handling.
- Add `HTML` sanitization for UI content provided by users via the study files.
- Implement route protections to prevent study participants from skipping
  verification and consent steps.
