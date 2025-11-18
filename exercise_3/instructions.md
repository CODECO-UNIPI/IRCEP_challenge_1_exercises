# Άσκηση 3 : Docker and K8s KinD Cluster

## Περιγραφή:
Να κάνετε deployment την containerized εφαρμογή που υλοποιήσατε στην Άσκηση 1, στο KinD cluster που δημιουργήσατε στην Άσκηση 2.

## Οδηγίες

1. δημιουργήσετε ή να τροποποιήσετε τα απαραίτητα YAML manifests (Deployment που υπάρχει ήδη στο φάκελο) 

2.  Κάνεις apply το ```deployment.yaml``` αρχείο, πληκτρολογώντας στο τερματικό:

    ```bash
    kubectl apply -f deployment.yaml
    ```

3. Στη συνέχεια, ελέγξτε ότι το Pod έχει δημιουργηθεί: 

    ```bash
    kubectl get pods
    ```

4. Επιτυχής εκτέλεση όταν:
    a. Εμφανίζεται ένα Pod με όνομα που ξεκινά με my-python-app-*
    b. Η στήλη STATUS δείχνει Running or Terminating
    c. Δεν υπάρχουν CrashLoopBackOff, ImagePullBackOff ή Error
