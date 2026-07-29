import react from "@vitejs/plugin-react";
import path from "node:path";
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    plugins: [react()],
    resolve: {
      alias: { "@": path.resolve(__dirname, "./src") },
    },
    server: {
      host: "0.0.0.0",
      port: 5173,
      proxy: {
        "/api": { target: env.VITE_API_BASE_URL?.replace("/api/v1", "") || "http://localhost:8000", changeOrigin: true },
        "/ws": { target: "ws://localhost:8000", ws: true, changeOrigin: true },
      },
    },
  };
});
