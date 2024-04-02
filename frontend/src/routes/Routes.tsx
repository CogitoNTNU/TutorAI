import { Route, Routes } from "react-router-dom";

// Pages
import Login from "../pages/Login.tsx";
import Signup from "../pages/Signup.tsx";
import Page404 from "../pages/Page404.tsx";
// import Upload from "../components/Upload.tsx";
import PDFtoFlashcard from "../pages/PDFtoFlashcard.tsx";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Login/>} />
      {/* <Route path="/create-flashcards" element={<Upload/>} /> */}
      <Route path="/pdf-to-flashcards" element={<PDFtoFlashcard />} />
      <Route path="/login" element={<Login/>} />
      <Route path="/signup" element={<Signup/>} />
      <Route path="*" element={<Page404 />} />
    </Routes>
  );
};

export default AppRoutes;
