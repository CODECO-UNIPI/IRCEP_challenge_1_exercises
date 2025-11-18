# Άσκηση 2 : Δημιουργία k8s KinD Cluster

## Περιγραφή

Να δημιουργήσεις ένα μικρό τοπικό Kubernetes cluster, προσθέτοντας labels σε κάθε node για πειραματισμό.

## Οδηγίες

1. Δημιούργησε ένα αρχείο ```kind-config.yaml``` με 1 control-plane και 2 workers.
2. Δημιούργησε το cluster (φτιάξε το δικό σου config file με βάση αυτό που υπάρχει ήδη στο φάκελο):
3. Στο τερματικό πληκτρολόγησε την παρακάτω εντολή:

    ```bash 
    kind create cluster --name labcluster --config kind-config.yaml
    ```

4. Έλεγξε τα nodes πληκτρολογώντας την παρακάτω εντολή:
    ```bash
    kubectl get nodes
    ```

5. Παρατήρησε αν όλα είναι σε κατάσταση Ready.


</br>

*Μπορείς να επεκτείνεις το ```kind-config.yaml``` προσθέτοντας περισσότερα labels για ρεαλιστικά σενάρια K8s.*


