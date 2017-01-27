# jupyterhub_config.py
c = get_config()

# Set the log level by value or name.
c.JupyterHub.log_level = 'DEBUG'

# Enable debug-logging of the single-user server
c.Spawner.debug = True

# Enable debug-logging of the single-user server
c.LocalProcessSpawner.debug = True

# Set admins
c.Authenticator.admin_users = {'charles'}
