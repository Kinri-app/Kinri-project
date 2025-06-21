# Kinri Frontend

Welcome to the **Kinri** frontend – a responsive and accessible user interface built with **React**, **TypeScript**, and **Tailwind CSS**, integrating **Auth0** for authentication. State management is handled via **Zustand**, and **Axios** is used for API requests.

## 🚀 Features

- 🔐 Auth0 authentication (login, logout, route protection)
- 🧩 Reusable UI components (`LoginButton`, `LogoutButton`, `ButtonLink`, etc.)
- 🧭 Routing with React Router
- 🧠 Global state management with Zustand
- 🌐 API communication with Axios
- 📱 Mobile navigation menu using Headless UI
- ✨ Tailwind CSS for modern and clean styles
- 🔒 Protected profile view and 401 unauthorized page

## 📦 Tech Stack

- [React](https://reactjs.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Auth0 React SDK](https://auth0.com/docs/libraries/auth0-react)
- [React Router](https://reactrouter.com/)
- [Axios](https://axios-http.com/)
- [Zustand](https://zustand-demo.pmnd.rs/)
- [Headless UI](https://headlessui.com/)

## 🔧 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kinri-frontend.git
   cd kinri-frontend
````

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Configure environment variables**

   Create a `.env` file in the root and add:

   ```
   VITE_AUTH0_DOMAIN=your-auth0-domain
   VITE_AUTH0_CLIENT_ID=your-auth0-client-id
   VITE_AUTH0_CALLBACK_URL=http://localhost:5173
   ```

4. **Run the development server**

   ```bash
   npm run dev
   ```

## 🗂 Project Structure

```
src/
├── auth/               # Auth-related components
│   ├── LoginButton.tsx
│   ├── LogoutButton.tsx
│   ├── Unauthorize.tsx
├── components/         # Shared UI components
│   ├── ButtonLink.tsx
│   └── HeaderNav/
├── pages/              # Route components
│   ├── Hero.tsx
│   ├── Profile.tsx
├── store/              # Zustand store
├── api/                # Axios API config and services
├── App.tsx             # Routing and layout
└── main.tsx            # Entry point
```

## ✅ Authenticated Routes

* `/profile`: Protected route, requires login
* Unauthorized access redirects to a **401** page

## 📄 License

This project is licensed under the MIT License.