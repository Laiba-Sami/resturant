import app from "./app.js";
import dotenv from "dotenv";

// Load environment variables
dotenv.config({ path: process.env.CONFIG_PATH || "./config/config.env" });

// Start server
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
