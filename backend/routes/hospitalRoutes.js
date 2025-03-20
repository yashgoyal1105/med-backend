const express = require("express");
const Hospital = require("../models/Hospital");
const authMiddleware = require("../middleware/authMiddleware");

const router = express.Router();

// Search hospitals
router.get("/search", authMiddleware, async (req, res) => {
  const { specialization, lat, long, radius } = req.query;
  
  const hospitals = await Hospital.find({
    specialization,
    location: {
      $near: {
        $geometry: { type: "Point", coordinates: [parseFloat(long), parseFloat(lat)] },
        $maxDistance: parseFloat(radius) * 1000, // Convert KM to meters
      },
    },
  });

  res.json(hospitals);
});

module.exports = router;
