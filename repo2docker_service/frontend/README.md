# A React + Chakra based frontend UI

This frontend project provides repo2docker-service with a basic UI to consume
its REST API.

The tool [Create React App][] bootstrapped this project, and now its
[`react-scripts`][] is used to develop, test, and build the static frontend
application (.html, .js, .css). With `react-scripts` we are indirectly provided
with common tooling like [Webpack][], [Babel][], etc.

We rely on [Chakra][] to provide React components to construct our UI.

## Development scripts

After installing [node][] and running `npm install` in this folder, you can run
the scripts below.

### `npm start`

Runs the app in the development mode. Open
[http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes. You may also see any lint errors in
the console.

### `npm test`

Runs the test runner in the interactive watch mode.

See documentation about [running tests][] for more information.

### `npm run build`

Builds the app for production to the `build` folder. The build is minified and
the filenames include the hashes.

See documentation about [deployment][] for more information.

[create react app]: https://create-react-app.dev/docs/getting-started/
[deployment]: https://create-react-app.dev/docs/deployment/
[node]: https://nodejs.org/en/
[running tests]: https://create-react-app.dev/docs/running-tests/
[react-scripts]: https://github.com/facebook/create-react-app/tree/main/packages/react-scripts
[babel]: https://babeljs.io/
[webpack]: https://webpack.js.org/
[chakra]: https://chakra-ui.com/
