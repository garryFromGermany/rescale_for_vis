# rescale_for_vis

The function `rescale_for_vis()` maps each number of a short list to a whole number, such that the order of the magnitudes of the differences between any two numbers is preserved. 
```
>>> from rescale import rescale_for_vis
>>> rescale_for_vis([0,-5,10,100.1])
array([1., 0., 2., 4.])
```
