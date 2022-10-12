import React from "react";
import ReactDOM from "react-dom/client";

import "./index.css";
import App from "./App";
import { ChakraProvider } from "@chakra-ui/react";

const root = ReactDOM.createRoot(document.getElementById("root"));

// About StrictMode: https://reactjs.org/docs/strict-mode.html
// About ChakraProvider: https://chakra-ui.com/getting-started
//
root.render(
  <React.StrictMode>
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </React.StrictMode>,
);
