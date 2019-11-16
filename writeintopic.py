import stegano
from stegano import lsb

secretmessage = "ich mag dich"
newphoto = "after.png"
templatephoto = "before.png"

secret = lsb.hide(templatephoto, secretmessage)
secret.save(newphoto)
clear_message = lsb.reveal(newphoto)
print(clear_message)