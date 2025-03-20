const MedCare = artifacts.require("MedCare");

module.exports = function(deployer) {
  deployer.deploy(MedCare);
};
