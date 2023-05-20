import json
import sys
import urllib.request

apipath = 'http://identi.ca/api'
username = input('Your username: ')
password = input('Your password: ')

print("Getting a list of subscribers...")
### Basic HTTP authentication taken from ur1.ca/govf

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of ``None``.
password_mgr.add_password(None, apipath, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
followers = json.loads(opener.open(apipath + '/statuses/followers.json').read())

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)
###
print("""Done fetching followers. Now type <option><enter> for the name prompted.
Options:
y -> block
f -> force unsubscribe (block, then unblock)
n -> don't block
q -> quit script""")

for follower in followers:
    i = follower['id']
    name = follower['name']
    b = input(name+'? (y/f/n/q) ')
    if b.strip() == 'y' or b.strip() == 'f':
        if urllib.request.urlopen(apipath + '/blocks/create/' + str(i) + '.json', b''):
            if b.strip() == 'f':
                if urllib.request.urlopen(apipath + '/blocks/destroy/' + str(i) + '.json', b''):
                    print("force unsubscribed " + follower['name'] + '.')
            else:
                print("blocked " + follower['name'] + '.')
    if b.strip() == 'q':
        break
