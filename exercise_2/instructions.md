# Οδηγίες

Δημιούργησε ένα αρχείο ρυθμίσεων cluster. Φτιάξε ένα αρχείο π.χ. kind-config.yaml με το  περιεχόμενο που αναφερεται στο kind-config.yaml

---

## Δημιούργησε το cluster τρέξε την εντολή:

kind create cluster --name <your-cluster-name> --config kind-config.yaml

---

##  Έλεγξε ότι το cluster δημιουργήθηκε σωστά τρέξε την εντολή:

kubectl get nodes
