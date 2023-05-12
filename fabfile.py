from fabric import task, Connection, Config
import os

""" check if tomcat is running on remote host 

    example: fab2 -H '[USER@HOSTNAME]' check-tomcat

"""

@task
def check_tomcat(ctx):

    """ acquisition and release - no need to c.close """
    with Connection(
        ctx.host,
        connect_timeout=4,
        connect_kwargs={
            "key_filename": "[SSH_KEY_PATH]"
    }
    ) as c:

        c.run('systemctl is-active jamf.tomcat8.service')


""" restart tomcat on remote host 

    example: fab2 -H '[USER@HOSTNAME]' restart-tomcat

"""

@task
def restart_tomcat(ctx):
    
    cred = os.environ.get("ADM_USER_PASS")
    config = Config(overrides={'sudo': {'password': cred}})

    """ acquisition and release, no need to c.close """
    with Connection(
        ctx.host,
        config=config,
        connect_timeout=4,
        connect_kwargs={
            "key_filename": "[SSH_KEY_PATH]"
    }
    ) as c:
        
        c.sudo('systemctl restart jamf.tomcat8.service', hide='stderr')


