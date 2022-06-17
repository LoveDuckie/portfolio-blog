

function Test-Command
{
    param([Parameter(HelpMessage="",DefaultValue="")][string]$PythonCommandName)

}

function Test-PythonInstalled
{
    param([Parameter(HelpMessage="",DefaultValue="")]$PythonCommandName)
}

Write-Host "Checking Python installation"

if (!(Test-PythonInstalled))
{
    Write-Error "Python is not installed on this machine" -ErrorAction Stop
}