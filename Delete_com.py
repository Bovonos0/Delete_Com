import amino
import aminos
client=aminos.ClientSid()
#تسجيل
print ("By Bovonos")

print ("Git Hub: https://github.com/Bovonos0")

sid=input("sid: ")

client.sssid(sid=sid)

#رابط المنتدى

comlink=input("Community Link: ")

cominfo=client.get_from_code(comlink)
comId=cominfo.path[1:cominfo.path.index('/')]

subclient=amino.SubClient(comId=comId,profile=client.profile)


clientx=amino.acm.ACM(profile=client.profile, comId=comId)

email=input("Your Email: ")
password=input("Your Password: ")

clientx.delete_community(email=email,  password=password, verificationCode=None)

print ("Done")

