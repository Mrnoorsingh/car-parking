#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import cv2


# In[3]:


def colors(class_names):
    np.random.seed(12)
    rand_colors=[tuple(np.random.rand(3)*255) for _ in range(len(class_names))]
    dict_color={ID:color for (ID,color) in enumerate(rand_colors) }
    return dict_color


# In[4]:


def mask(image,mask,color,alpha=0.5):
    for i in range(3):
        image[:,:,i]=np.where(mask==1,image[:,:,i]*(1-alpha)+alpha*color[i],image[:,:,i])
    return image


# In[5]:


def displayinstances(image,masks,class_ids,class_names,scores,boxes):
    color=colors(class_names)
    N=boxes.shape[0]
    if not N:
        pass
    else:
        assert  N==masks.shape[-1]==class_ids.shape[0]
   
    
    for i in range(N):
         if not np.any(boxes[i]):
            # Skip this instance. Has no bbox. Likely lost in image cropping.
             continue
         y1, x1, y2, x2 = boxes[i]   
         class_id = class_ids[i]
         score = scores[i] if scores is not None else None
         label = class_names[class_id]
         color = color[class_id]
         caption = "{} {:.3f}".format(label, score) if score else label
         mask = masks[:, :, i]
         image = apply_mask(image, mask, color)
         image = cv2.rectangle(image,(x1,y1),(x2,y2),color,2)
         image = cv2.putText(image,caption,(x1,y1),cv2.FONT_HERSHEY_PLAIN,0.5,color,2)  
    return image
          

