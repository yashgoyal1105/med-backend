require("dotenv").config();
const express = require("express");
const connectDB = require("./config/db");
const cors = require("cors");
const Hospital = require("./models/Hospital"); // Import model

const app = express();
connectDB();

app.use(cors());
app.use(express.json());

app.use("/api/auth", require("./routes/authRoutes"));
app.use("/api/hospitals", require("./routes/hospitalRoutes"));

app.listen(5000, () => console.log("Server running on port 5000 🚀"));
