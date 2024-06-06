def rol_Log(Log, request_user, rol):
    header = f'Selected role: {rol}'
    body = f'A role change has been made.'
    
    new_log = Log(user=request_user, header=header, body=body)
    new_log.save()