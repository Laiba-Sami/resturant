import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig({
  base: './',
  plugins: [react()],
  server: {
    host: '0.0.0.0',   // ✅ Required for Docker to expose Vite
    port: 5173,         // Optional (for clarity)
  }
})
