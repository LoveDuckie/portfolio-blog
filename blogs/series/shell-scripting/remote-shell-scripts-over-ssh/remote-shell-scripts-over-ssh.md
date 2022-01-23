# Remote Shell Scripts over SSH

In this blog post, we will discuss what is required for executing shell scripts on a remote machine using SSH, through the execution of a script on your own machine.

## Authentication

In order for shell scripts to execute on a remote machine over SSH, you must first successfully authenticate with the remote machine. There are two popular ways to achieve this.

### Key-based Authentication

Key-based authentiication must first be configured and setup on your machine.

..

### Password Authentication

..

## Multi-line Scripts

In some instances you may find yourself needing to execute slightly more complex operations remotely. In which case, you will likely you want to use a multi-line string comprising of a script.

```bash
#!/bin/bash

ssh -q -n user@host /bin/bash "something goes here

something else here
"
```

Alternatively, you can achieve the same by using HEREDOC strings.


```bash
#!/bin/bash

ssh -q -n user@host /bin/bash <<EOF 
something goes here
something else here
EOF
```

## Storing Values from Remote Script Execution

If you want to store the resulting value from running a remote script, there are two approaches. To store data from the `STDOUT` stream (i.e. console output), you can use the following example

```bash
my_var=$(ssh -q -n user@host /bin/bash "
echo "test"
")

echo $my_var
# outputs: "test"

```

## Copying Environment Variables to Remote Machine over SSH

In the instance that your remote script requires.

```bash
scp
```

---

I hope you found this blog post useful! Let me know if you think there should be improvements by opening an issue on GitHub.

 **Follow me on Twitter:** [@TheLoveDuckie](https://twitter.com/theloveduckie)