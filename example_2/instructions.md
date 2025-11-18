# Οδηγίες

## 1. Δημιουργία αρχείου ρυθμίσεων cluster

Δημιούργησε ένα αρχείο ρυθμίσεων cluster, π.χ. **kind-config.yaml**,  
με το περιεχόμενο που αναφέρεται στο αντίστοιχο αρχείο του repository.

---

## 2. Δημιουργία cluster

Τρέξε την εντολή:

```bash
kind create cluster --name <your-cluster-name> --config kind-config.yaml
```

## 3. Έλεγχος ότι το cluster δημιουργήθηκε σωστά

```
kubectl get nodes

```

## 4. Αναμενόμενη έξοδος


```
NAME                        STATUS   ROLES           AGE   VERSION
mycluster-control-plane     Ready    control-plane   1m    v1.30.x
mycluster-worker            Ready    <none>          1m    v1.30.x
mycluster-worker2           Ready    <none>          1m    v1.30.x
mycluster-worker3           Ready    <none>          1m    v1.30.x

```