import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from './routes/Routes'
import './App.css'
import Header from './components/Header';
import { useState, createContext } from "react";
import { FlashcardsProps } from './components/Flashcard';
import { User } from './types/User';

// const UserContext = createContext<User>({ username: '', password: '', files: [], sets: [{ name: '', flashcards: [] }] })
const UserContext = createContext<{
  user: User;
  setUser: (user: User) => void;
}>({
  user: {
    username: '',
    password: '',
    files: [''],
    sets: [
      {
        name: '',
        flashcards: [
          {
            front: '',
            back: ''
          }
        ]
      }
    ]
  },
  setUser: (user: User) => {
    console.log('Setting user:', user); // TODO: remove this line
  }
});

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
    files: ['testfile1.pdf', 'testfile2.pdf'],
    sets: [mockFlashcards]
  }
  
  const [user, setUser] = useState<User>(mockUser)
  const value = { user, setUser }

  return (
    <Router>
      <UserContext.Provider value={value}>
        <Header />
        <AppRoutes />
      </UserContext.Provider>
    </Router>
  )
}

export default App
export { UserContext }