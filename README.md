# Important to know #
* In a Python request you will pass headers into the requests via the ```headers = {} ``` line
* To pass the body of a request you will use ``` data = {} ``` 
* Parameters can be set via ``` params = {} ```

# Script Background #
We formerly had a jupyter notebook that we did this in but we have since shuttered that product so I recreated our API exploration notebook locally. This allows us to very easily spin up cycles to explore various endpoints as well as easily authenticate to the API.

This template can be copied or expanded within a single file to house authentication and exploration within a single file, but that is up to you and your workflow. You can also opt to have it save the output to a named file or omit those lines if it is not needed to refer back to the logs.
