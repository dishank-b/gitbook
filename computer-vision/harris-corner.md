# Harris Corner

**Detect Corner using a Matrix which composed of intensity gradient at pixels as it elements. Then a value is calculated using eigen values of that Matrix and If that value is greater than certain threshold then that pixel is considered as a corner.**\
&#x20;![](https://lh4.googleusercontent.com/vG46dUS8klY-kvf2o3X1oARAsA6exkUd9D3-hPJ6ikAepn1txYC8o9czn70nxJG7eEYYUeLmflNCq2oEMeBm1yB7sIP7bEky4LJW9-JUy-LrHASPVkVK\_36om69JSdT8Q8RNJlBe)  ![](https://lh5.googleusercontent.com/b8dLhjaGeSHpw5tSzivxV9c\_nv3YFPimsaMKyD5sRMyOHEmiesqcBcFTEH4H1rhSEGj5zjv4F07PZwg4f-QAmYX\_07Mv8GF6Uw9\_tGFs\_4XZlYunmRXYfyMIbtfnK1NJyticIGmF)\
**Note:- Harris Corner is not scale invarient. Therefore we have to tweak this method to make it scale invarient using windows of different size for same image of different size. For this we have to find the scale factor of two different image.**\
**Shi-Tomasi used  R =** ![](https://lh5.googleusercontent.com/PIe5-ZmKkksnp2N3HLx5VBxIbaGmx0i5MkHIZ1oWDEviHwO3xePWc1GQuVJHsnsM29FlJFLnDr9tVq289CzkFl22qE3tUL-NThAcu8wxQ2ab\_1yaWtfczJJ4TrBHucOcdXCYS9\_8)**, which worked better than normal harris corner.**
