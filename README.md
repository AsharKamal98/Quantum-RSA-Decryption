# Quantum-RSA-Decryption
This script simulates secure communication between two parties, Alice and Bob, using
the RSA encryption scheme. It also simulates an attack by a third party, Eve, who attempts 
to break the RSA encryption using Shor's quantum factorization algorithm. Users can choose 
to simulate quantum circuits locally using the AerSimulator or execute them on IBM's cloud-
based quantum backends provided by Qiskit. The script supports circuits of up to approximately 
22 qubits, enabling the factorization of RSA-encrypted messages that use prime numbers up to 
the order of 10² with the implemented Shor’s algorithm.
