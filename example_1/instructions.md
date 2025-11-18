# Οδηγίες

1. Άνοιξε ένα terminal και γράψε:

    ```bash
    mkdir my-docker-app
    cd my-docker-app
    mkdir src
    ```

2. Φτιάξε το αρχείο Dockerfile (στον φάκελο **src**, δημιούργησε ένα αρχείο με όνομα **Dockerfile**)  
   και γράψε ό,τι αναφέρεται στο αρχείο Dockerfile του παρόντος φακέλου.

---

3. Δημιούργησε το Docker image, εκτελώντας την εντολή:

    ```bash
    docker build -t my-hello-image .
    ```

---

4. Τρέξε το container από το image:

    ```bash
    docker run my-hello-image
    ```


---

### (Προαιρετικά) Δες τα images σου:

    (Εκτέλεσε στο terminal)

    ```bash
    docker images
    ```


5. Θα δεις στο τερματικό:

    ```bash
    Hello from my custom Docker image!
    ```

</br>

**(Προαιρετικά) Δες τα images σου:**



</br>

```
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
my-hello-image    latest    a1b2c3d4e5f6   1 minute ago     120MB
```