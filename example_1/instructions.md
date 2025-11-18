# Οδηγίες

1. Άνοιξε ένα terminal και γράψε:

    </br>

    ```bash
    mkdir my-docker-app
    cd my-docker-app
    ```

    </br>

2. Φτιάξε το αρχείο Dockerfile (στον ίδιο φάκελο, δημιούργησε ένα αρχείο  με όνομα Dockerfile) και γράψε ότι αναφέρεται στο αρχείο Dockerfile του παρόντος φακέλου.

</br>

3. Δημιούργησε το Docker image, εκτελώντας την εντολή:

    ```bash
    docker build -t my-hello-image .
    ```

</br>

4. Τρέξε το container από το image:

    ```bash
    docker run my-hello-image
    ```

</br>

5. Θα δεις στο τερματικό:

    ```bash
    Hello from my custom Docker image!
    ```

</br>

**(Προαιρετικά) Δες τα images σου:**

</br>

    
    Hello from my custom Docker image!
    

</br>

Θα δείς κάτι σαν:

</br>

```
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
my-hello-image    latest    a1b2c3d4e5f6   1 minute ago     120MB
```