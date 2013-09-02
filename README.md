# Endpoints on non-default Module

This is a sample app in Python and Java to track [Issue 9916][1].

It has 2 modules: default and api.
The goal is to route `/_ah/api` and `/_ah/spi` requests to api Module.

1. Clone the repo: `git clone git@github.com:crhym3/endpoints-nondefmod.git`
2. Allocate a new app ID on appspot.com
3. Deploy the app
    ```
    # Python
    cd endpoints-nondefmod/python
    appcfg.py --oauth2 -A <appID> update app.yaml api.yaml
    appcfg.py --oauth2 -A <appID> update_dispatch .

    # Java
    cd endpoints-nondefmod/java
    mvn install
    cd ear
    mvn appengine:update -Dappengine.appId=<appID>
    ```
4. Try accessing a discovery doc on
    ```
    https://appID.appspot.com/_ah/api/discovery/v1/apis
    ```
    If it works then Cloud Endpoints feature on non-default Module is supported.


[1]: https://code.google.com/p/googleappengine/issues/detail?id=9916
