// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MedCare {
    struct Prescription {
        uint256 patientId;
        uint256 doctorId;
        string prescriptionData;
    }

    mapping(uint256 => Prescription) public prescriptions;

    event PrescriptionAdded(uint256 patientId, uint256 doctorId, string prescriptionData);

    function storePrescription(uint256 patientId, uint256 doctorId, string memory prescriptionData) public {
        prescriptions[patientId] = Prescription(patientId, doctorId, prescriptionData);
        emit PrescriptionAdded(patientId, doctorId, prescriptionData);
    }

    function getPrescription(uint256 patientId) public view returns (string memory) {
        return prescriptions[patientId].prescriptionData;
    }
}
