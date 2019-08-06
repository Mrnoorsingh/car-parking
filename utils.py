from twilio.rest import Client
import numpy as np

def twilio():
    account_sid = 'ACc2480559020c2b645e9e735e08e8ccca'#user's unique SID
    auth_token = '4ef89947554b6eb5aeebd67443f31f52'#user's authentication token
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Parking Available",
                     from_='+18065471647',
                     to='+917888362514'
                 )
    
def ApplyMask(image,mask,color,alpha):
    for i in range(3):
        image[:,:,i]=np.where(mask==1,image[:,:,i]*(1-alpha) + alpha*color[i]*255,image[:,:,i])
    return image    

def Colors(class_names):
    np.random.seed(12)
    rand_colors=[tuple(np.random.rand(3)*255) for _ in range(len(class_names))]
    color_dict={ID:color for ID,color in enumerate(rand_colors)}
    return color_dict
