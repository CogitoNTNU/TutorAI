import { Route, Routes } from "react-router-dom";

import Page404 from "../pages/Page404.tsx";
import FlashcardsPage from "../pages/FlashcardsPage.tsx";
import ChatPage from "../pages/ChatPage.tsx";
import CompendiumPage from "../pages/CompendiumPage.tsx";
import TestPage from "../pages/TestPage.tsx";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/flashcards" element={<FlashcardsPage />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/compendium" element={<CompendiumPage />} />
      <Route path="/test" element={<TestPage />} />
      <Route path="*" element={<Page404 />} />
    </Routes>
  );
};

export default AppRoutes;
