from fabric import task, Connection

""" check if tomcat is running on remote host 

    example: fab2 -H '[USER@HOSTNAME]' checkTomcat

"""

@task
def checkTomcat(ctx):

    """ acquisition and release, no need to c.close """
    with Connection(
        ctx.host,
        connect_timeout=4,
        connect_kwargs={
            "key_filename": "[SSH_KEY_PATH]"
    }
    ) as c:

        c.run('systemctl is-active jamf.tomcat8.service')


