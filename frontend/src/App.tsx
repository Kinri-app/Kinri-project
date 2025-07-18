import { Route, Routes } from 'react-router'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import HeaderNav from './components/HeaderNav'
import UserProfile from './auth/pages/UserProfile'
import ChatPage from "./chat/pages/ChatPage.tsx";
import FlashcardPage from './flashcards/pages/FlashcardPage.tsx'
import AssessmentPage from './assessments/pages/AssessmentPage.tsx'


function App() {
    return (
        <main className='h-full'>
            <HeaderNav />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/profile" element={<UserProfile />} />
                <Route path="/assessments" element={<AssessmentPage />} />
                <Route path="/flashcards" element={<FlashcardPage />} />
                <Route path="/chat" element={<ChatPage />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </main>
    )
}

export default App
