# Writing Shared Scripts

Shell scripts are often used for automating otherwise trivial manual tasks. It's often the case in software development that you don't want to repeat your efforts when writing code, because code duplication can lead to fragmentation of functionality, and it's also just a bad use of your time to repeat yourself!

Instead, consider using "shared" scripts - scripts that contain shared and reusable functions and variables. For example this could include functions responsible for logging, or running a parameterized commands that may used in multiple places in different scripts in your repository.

## Writing the Header

When including your shared script into other scripts, you must ensure that functions or variables are not "imported" twice.

...

## Exporting Functions and Variables

...

### Functions

...

### Variables

...
