
import { Route, Routes } from 'react-router'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import HeaderNav from './components/HeaderNav'
import UserProfile from './auth/pages/UserProfile'


function App() {
  return (
    <main className='h-full'>
      <HeaderNav />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </main>
  )
}

export default App
