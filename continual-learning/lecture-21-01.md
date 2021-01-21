# Lecture - 21/01

## IRM: Invarient Risk Minimization

### Motivation: Failures of ML

Learning features to classify images which are actually not right ti classify.  
Ex: While training cow detector, mostly images are with green background. So network might learn green bg as feature. Now if you input cow in some other bg, it might not classify. Basically spurious features should not learned for classification. 

This is related to correlation vs Causation. 

Basically shape and color of cow is real causation of labelling the image as cow. Whereas, green bg is not the cause but have a correlation with cow label.  



