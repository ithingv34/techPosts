import { CssBaseline } from "@mui/material";
import { useRoutes } from "react-router";
import routes from "./router";

function App() {
  const contents = useRoutes(routes);

  return <CssBaseline>{contents}</CssBaseline>;
}

export default App;
