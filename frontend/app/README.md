<p align="center">
    <a href="https://boterview.dev">
        <img width="180px" src="src/assets/images/boterview-logo.png" alt="boterview logo"/>
    </a>
</p>

<h1 align="center">
    Frontend
</h1>

This `README.md` file pertains the application frontend for the
[`boterview`](https://boterview.dev) tool. A bundled version of
this frontend is included in the `python` package, which you can install from
the `PyPI` repository using the following command:

```bash
# Install `boterview`.
pip install boterview
```

For more information on what `boterview` is and how to use it, please refer to
the [documentation](https://boterview.dev).

## Description

The application frontend is a [`React`](https://react.dev/) application that
uses the [`Vite`](https://vite.dev/) build tool. Most of the application is
written in [`TypeScript`](https://www.typescriptlang.org/).

## Development

You can start the development server by running the following command:

```bash
# Start the development server.
pnpm run dev
```

Executing the command above will start the development server on
`http://localhost:5173`. You can access the application by navigating to the
corresponding URL in your browser.

**_Note._** Parts of the content displayed in the frontend are served from the
`boterview` backend server. Therefore, it is necessary to have the backend
server running as well. To start the `boterview` backend server, you can run the
following command:

```bash
# Start the backend server.
boterview run --config <path-to-config-file> --headless
```

**_Note._** Please refer to the
[documentation](https://boterview.dev) for more information on
how to scaffold a study and quickly get started.

The `--headless` flag is used to decide whether to mount the frontend
application or not. In a production environment, the frontend is served by the
backend server. However, in a development environment, the frontend is served by
the `Vite` development server. Therefore, the `--headless` flag tells the
backend not to look for the built frontend application.

As a consequence, when running in `--headless` mode, a frontend server should be
started separately, via `pnpm run dev`. In this case, the frontend server needs
to know the URL of the backend server. By default, the backend server starts on
`http://localhost:8080`, however you can specify a different port using the
`--port` flag with the `boterview run` command. In this case, you need to adjust
the `BOTERVIEW_BACKEND_URL` environment variable in the `.env.development` file.
By default, `BOTERVIEW_BACKEND_URL=http://localhost:8080`.

If you prefer the frontend to be instead served by the backend server, you can
drop the `--headless` flag and the frontend will be mounted by the backend
server. In this case, you need to make sure that the frontend application is
built before starting the backend server. You can build the frontend application
by running the following command:

```bash
# Build the frontend application.
pnpm run build
```

## Production

In most cases you do not need to build the frontend application yourself. The
frontend is bundled with the `boterview` package and served by the backend
server. Please refer to the
[documentation](https://boterview.dev) for more information on
how to package and deploy the `boterview` application.

## License

Please refer to the main `README.md` file located in the root of this repository
for licensing information.
