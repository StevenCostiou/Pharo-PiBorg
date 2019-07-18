|borg|
borg := BorgApp new.
borg startBorg.
1 seconds wait.
ClyNavigationEnvironment reset.
ClySystemEnvironmentPlugin disableSlowPlugins.
TlpRemoteUIManager registerOnPort: 40423
