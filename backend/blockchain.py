from web3 import Web3
import json

# Connect to Ganache or any other blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load the contract ABI and contract address
contract_address = '0x1A6Cbea6c0e1792e2dbe3d552FfCAE3DF034df27'
with open('build/contracts/MedCare.json') as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def send_prescription_transaction(patient_id, doctor_id, prescription_data, account):
    tx = contract.functions.storePrescription(patient_id, doctor_id, prescription_data).buildTransaction({
        'from': account,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': web3.eth.getTransactionCount(account),
    })
    signed_tx = web3.eth.account.signTransaction(tx, private_key="YourPrivateKey")
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash.hex()
