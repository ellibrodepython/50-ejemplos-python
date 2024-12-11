# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install qiskit qiskit_ibm_runtime
# 2. Ejecuta el script: python 05_computacion_cuantica.py
# 3. Crea una cuenta en https://quantum.ibm.com
# 4. Obtén un token de acceso en https://quantum-computing.ibm.com/account
# 5. Cambia token="TU_TOKEN" por tu token de acceso

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService

q = QuantumRegister(64)
c = ClassicalRegister(64)
circ = QuantumCircuit(q, c)
circ.h(q)
circ.measure(q, c)

service = QiskitRuntimeService(channel="ibm_quantum", token="TU_TOKEN")
backend = service.backend('ibm_kyiv')
qc_basis = transpile(circ, backend)
job = backend.run(qc_basis, shots=4)

counts = job.result().to_dict()["results"][0]["data"]["counts"]
priv_key = ''.join(counts.keys()).replace('0x', '')
print(f"Clave privada: {priv_key}")