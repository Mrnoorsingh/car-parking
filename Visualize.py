import cv2
import numpy as np
from utils import ApplyMask,Colors
from mrcnn.utils import compute_overlaps

def DisplayInstances(image,boxes,masks,class_ids,class_names,scores):
    N=boxes.shape[0]
    if not N:
        pass
    else:
        assert N==masks.shape[-1]==class_ids.shape[0]
        
    mask_color=Colors(class_names)
    for i in range(N):
        
        if not np.any(boxes[i]): 
            # Skip this instance. Has no bbox. Likely lost in image cropping or label is not required vehicle
             continue
                
        class_id = class_ids[i]       
        label = class_names[class_id]       
        if label=="car" or  label=="bus":     
            
            y1, x1, y2, x2 = boxes[i]
            score = scores[i] if scores is not None else None
            color=mask_color[class_id]
            caption = "{} {:.3f}".format(label, score) if score else label
            mask = masks[:, :, i]
            image =ApplyMask(image, mask, color,alpha=0.5)
            image = cv2.rectangle(image,(x1,y1),(x2,y2),color,2)
            image = cv2.putText(image,caption,(x1,y1),cv2.FONT_HERSHEY_PLAIN,0.5,color,2)
    return image


def Park(box1,box2):
    overlaps=compute_overlaps(box1,box2)
    filter_boxes=[box1[i] for i in range(len(box1)) if np.any(overlaps[i,:]>0.9)]
    return np.array(filter_boxes)
