import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders repo2docker-service text", () => {
  render(<App />);
  const textElement = screen.getByText(/repo2docker-service/i);
  expect(textElement).toBeInTheDocument();
});
