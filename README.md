# mirrord-demo

A demo setup for showcasing [mirrord](https://github.com/metalbear-co/mirrord).

### The App

The deployed application receives HTTP GET requests and returns a response with an upper 
case version of whatever was after the first `/` in the url, and an app version number.
The version number is there for changing it in the local application that you run with 
mirrord. That way you can see in the response whether you received a response from the 
deployed or the local application.

The application serves each requested string 5 times, and after that, instead of returning
the upper version of the string, it returns an error.

In order to keep track of the amount of times a string was requested, the app queries a
redis service in its same k8s namespace.

### The demo

Once the resources are deployed to the cluster, you can:

1. Run `kubectl` to show your audience the services and the external IP:
```
kubectl get svc
NAME           TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)           AGE
redis-leader   ClusterIP      10.44.6.236   <none>         6379/TCP          19d
upper          LoadBalancer   10.44.5.66    34.136.42.53   30003:30003/TCP   19d
```
2. Send a curl request to <EXTERNAL-IP>:<PORT>/<SOME-NEW-STRING>:
```
curl 34.136.42.53:30003/my-test-string
{"upper":"MY-TEST-STRING","version":"1.0"}
```
3. Run mirrord with `steal`: 
WIP
