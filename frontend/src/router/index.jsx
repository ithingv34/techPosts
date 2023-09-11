import Home from "@pages/Home";
import Login from "@pages/Login";
import Profile from "@pages/Profile";

const routes = [
  { path: "", element: <Login /> },
  { path: "/home", element: <Home /> },
  { path: "/profile:userId", element: <Profile /> },
];

export default routes;
