import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { BrowserRouter } from 'react-router'
import AuthProviderWithHistory from './auth/AuthProviderWithHistory.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <AuthProviderWithHistory>
        <App />
      </AuthProviderWithHistory>
    </BrowserRouter>
  </StrictMode>,
)

