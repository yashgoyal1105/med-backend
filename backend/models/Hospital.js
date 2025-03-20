const mongoose = require("mongoose");

const hospitalSchema = new mongoose.Schema({
  name: String,
  specialization: String,
  location: {
    type: { type: String, default: "Point" },
    coordinates: [Number], // [longitude, latitude]
  },
});

hospitalSchema.index({ location: "2dsphere" });

module.exports = mongoose.model("Hospital", hospitalSchema);
