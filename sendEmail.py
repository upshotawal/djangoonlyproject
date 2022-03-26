def send_message(service, user_id, message):
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
   #  print "Message Id: %s" % message['id']
   #  return message
   # except errors.HttpError, error:
   # print 'An error occurred: %s' % error
