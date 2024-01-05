import { Route, Routes } from "react-router-dom";

// Pages
import Login from "../pages/Login.tsx";
import Signup from "../pages/Signup.tsx";
import Page404 from "../pages/Page404.tsx";
import Upload from "../pages/Upload.tsx";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Login/>} />
      <Route path="/upload" element={<Upload/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<Signup/>} />
      <Route path="*" element={<Page404 />} />
    </Routes>
  );
};

export default AppRoutes;
