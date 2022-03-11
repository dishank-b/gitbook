# Optical Flow



* **Feature Based Methods :-**\
  **Track features such as corners, etc across all the frames. Hence they gave you apparent motion (Motion in the image).**
* **Direct or Dense Methods :-**\
  **Recover motion for each pixel of image space-temporal image brigthness variation.**\
  **Suitable for videos and image variation is small.**
  * **Lucan-Kannade Methode is used.**&#x20;
* **Optical Flow :- Optical flow is the pattern of apparent motion of image objects between two consecutive frames caused by the movemement of object or camera.**
  * **Consider a pixel I(x,y,t) in first frame (Check a new dimension, time, is added here. Earlier we were working with images only, so no need of time). It moves by distance (dx,dy) in next frame taken after dt time. So since those pixels are the same and intensity does not change, we can say,**

**I(x,y,t)=I(x+dx,y+dy,t+dt)**

*
  * **Then take taylor series approximation of right-hand side, remove common terms and divide by dt to get the following equation:**\
    &#x20;**** ![Screenshot from 2017-04-01 12:43:07.png](https://lh6.googleusercontent.com/ti6YyihXetknknZvO828Z6B20jjPMKoLzy9BSC01E6Yi3mQ5Xg1NLjQ4KnCG0o2FuySUKrCzNPlUpiNdYU5D6daIrouAl\_qKAUwgmsUANc19w-GxHXLq9Rhk4gS1T\_q9Zw4rlUN-)
  * **Above equation is called Optical Flow equation. In it, we can find fx and fy, they are image gradients. Similarly ft is the gradient along time. But (u,v) is unknown. We cannot solve this one equation with two unknown variables. So several methods are provided to solve this problem and one of them is Lucas-Kanade.**\
    ****\
    ****
  * **Lucas-Kanade method**\
    **We have seen an assumption before, that all the neighbouring pixels will have similar motion. Lucas-Kanade method takes a 3x3 patch around the point. So all the 9 points have the same motion. We can find (fx,fy,ft) for these 9 points. So now our problem becomes solving 9 equations with two unknown variables which is over-determined. A better solution is obtained with least square fit method. Below is the final solution which is two equation-two unknown problem and solve to get the solution.\[**\
    ****![Screenshot from 2017-04-01 12:44:07.png](https://lh6.googleusercontent.com/Dqj1HY2TvRKttpL1VowYW8trao6R1mMy1AJlSfjq5zDFLTmUjgOxe\_qvncaRf3bBMFVmWeus43xaJWefnh16FWgS9xuWpnflt97ECXJoMsnw6G9gwM7xSiidet0w1-qXfB7uCRtC)****\
    **( Check similarity of inverse matrix with Harris corner detector. It denotes that corners are better points to be tracked.)**\
    ****\
    ****
  * **So from user point of view, idea is simple, we give some points to track, we receive the optical flow vectors of those points. But again there are some problems. Until now, we were dealing with small motions. So it fails when there is large motion.**\
    **For Larger motion :-**&#x20;
    * **Iterative Refinement :-**\
      **This is used when linear approximation of taylor is not valid and higher order terms should also be used.**\
      ****![](https://lh5.googleusercontent.com/6glEGrbSyYO7VNqYtreKliZKtHYvUWNWw9NNeuhL4NjPcnn6DqOgQNwO-4zBFFy4AzHiqe0Ds9q3qPeaRmV8iB1dV3nYpsOatNlSCqx0tRYXm0aT45wg0cwnwP9bli8jgXm8oDF4)****\
      ****\
      ****
    * **Coarse-to-refinement**\
      **This is used when pixel motion is not small.**
      * **We use hierarchical LK here:-**
      * ![](https://lh3.googleusercontent.com/JMKLgaVkQpUtL61Xe0wWllSbEn5wbBfdcgoo3jrjyTHwOy\_86VaFhM\_mWZyNj53Zs0hge7uH8Zl7bIESCME8Msrb0dSCYs4iwkF7NkFN-c8LfjS2\_dGc9BYWNzNI40YVAMV6Ch3G)
      * ![](https://lh4.googleusercontent.com/c7tBfCj6p82GxaAxIDQDsQWOqC6rz1hBrr-kRm4Jb0V090-mvNK2ygfY5cqSNJ2RZfp9WwNyLnghuZ1Y2eBKOyHtxWwt4HeUyrUBSmh6d\_Hu3L2qKONA4CYAzF5SWdAOYbbFFgIr)
      * ![](https://lh4.googleusercontent.com/XFoBGG-RrkoNQ\_6pHbFkvrWME0gqxitBP0odh4fYNN0ySZHBjpyF5xygv9T8zO6qMFiQXj7UHP5YHxQItpOu3aiUTpZEJyknLhvsRVAn5LooztDmWxxqtfuzeQ4YES5pD-uCLr8e)
      * ![](https://lh6.googleusercontent.com/e1BUJWSjfj8fcqMLXDWHHcrFn4yRuXJTN6AXWbz0BuxFdf2Vw91hIoEX3tvLeaVBqiQ0bbuxKxS06hW4dsB6LwC9g7gVsNglABN0ReyB2MgNGo4\_\_rY2lR4o3v-rJUCgWOHpAUKb)
