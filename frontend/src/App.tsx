import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from './routes/Routes'
import './App.css'
import Header from './components/Header';
import { useState, createContext } from "react";
import { FlashcardsProps } from './components/Flashcard';
import { User } from './types/User';

const UserContext = createContext<User>({ username: '', password: '', files: [], sets: [{ name: '', flashcards: [] }] })

function App() {
  const mockFlashcards: FlashcardsProps = {
    name: 'Test Set',
    flashcards: [
      {
        front: 'Front of card',
        back: 'Back of card'
      }
    ]
  }

  const mockUser: User = {
    username: 'testuser',
    password: 'testpassword',
    files: ['file1', 'file2'],
    sets: [mockFlashcards]
  }
  
  const [user, setUser] = useState<User>(mockUser)

  return (
    <Router>
      <UserContext.Provider value={user}>
        <Header />
        <AppRoutes />
      </UserContext.Provider>
    </Router>
  )
}

export default App
export { UserContext }