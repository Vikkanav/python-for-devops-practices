while kubectl get deployment/myapp | grep -q 0/1; do
    echo "Waiting for myapp to be ready..."
    sleep 10
done



# If this loop am writing only for understand, it did not execute as of now. we dont have k8s conditions now 
