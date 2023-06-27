import numpy as np
import pandas as pd
from skimage.measure import regionprops_table

def calc_obj_props(files, masks, imgs, obj_clf_masks=None, properties=None):
    
    if properties is None:
        properties = ('label', 'area', 'area_convex', 'area_filled', 'perimeter', 'axis_major_length', 'axis_minor_length', 'bbox', 'centroid', 'eccentricity', 'intensity_mean', 'intensity_max', 'intensity_min', )
    
    if obj_clf_masks is not None:
        obj_clf_masks = np.expand_dims(obj_clf_masks, -1)
        if imgs.ndim == 3:
            imgs = np.expand_dims(imgs, -1)

    df = []
    for i in range(len(masks)):
        if obj_clf_masks is not None:

       
            intensity_image = np.concatenate((imgs[i], obj_clf_masks[i]), axis=-1)

        else:
            intensity_image = imgs[i]
        prop_df = pd.DataFrame(regionprops_table(masks[i], intensity_image=intensity_image, properties=properties))
        prop_df['circularity'] = 4 * np.pi * prop_df['area'] / (prop_df['perimeter'] * prop_df['perimeter'])
        #prop_df['filename'] = files[i]
        prop_df.insert(0, 'filename', files[i])
        df.append(prop_df)
    
    df = pd.concat(df)
    if obj_clf_masks is not None:
        obj_idx = str(intensity_image.shape[-1] - 1)
        obj_classifcation = df['intensity_mean-' + obj_idx]
        df.drop(labels=['intensity_mean-' + obj_idx, 'intensity_max-' + obj_idx, 'intensity_min-' + obj_idx], axis=1,inplace = True)
        df.insert(1, 'obj_classifcation', obj_classifcation)


    return df