# Workflow for combining cellpose segmentations with cell classification

This repositry contains three python notebooks which postprocess [cellpose](https://www.cellpose.org/) segmentation results:
1. segment_cells_cellpose.ipynb - Very simple notebook to batch process cellpose. Can also run in [command line](https://cellpose.readthedocs.io/en/latest/command.html#) (recommended).
2. train_cell_classifer.ipynb - Streamlines the process of training an object classifier using cellpose segmentations and the [napari-accelerated-pixel-and-object-classification (APOC)](https://github.com/haesleinhuepf/napari-accelerated-pixel-and-object-classification) plugin.
3. calculate_cell_properties.ipynb - Calculates per cell properties from cellpose segmentations and (optionally) runs cell classification using a classfier trained with train_cell_classifer.ipynb.

If these notebooks are useful please cite our publication alongside APOC and cellpose:

Montague et al. in preperation (2023).

Any questions please contain [Jeremy Pike](j.a.pike@bham.ac.uk) and/or [Steve Thomas](s.thomas@bham.ac.uk).
