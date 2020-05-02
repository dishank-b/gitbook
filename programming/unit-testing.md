# Unit Testing

The objective of Unit Testing is to isolate a section of code and verify its correctness. In procedural programming a unit may be an individual function or procedure.  
The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output. In procedural programming, a unit may be an individual program, function, procedure, etc. In object-oriented programming, the smallest unit is a method, which may belong to a base/ super class, abstract class or derived/ child class.

* Benefits:
  * **If good unit tests are written and if they are run every time any code is changed, we will be able to promptly catch any defects introduced due to the change.**
  * **Codes are more reusable. In order to make unit testing possible, codes need to be modular. This means that codes are easier to reuse.**
  * **Development is faster. How? If you do not have unit testing in place, you write your code and perform that fuzzy ‘developer test’ \(You set some breakpoints, fire up the GUI, provide a few inputs that hopefully hit your code and hope that you are all set.\) But, if you have unit testing in place, you write the test, write the code and run the test. Writing tests takes time but the time is compensated by the less amount of time it takes to run the tests.**
* **Tips:** 
  * Before fixing a defect, write a test that exposes the defect. Why? First, you will later be able to catch the defect if you do not fix it properly. Second, your test suite is now more comprehensive. Third, you will most probably be too lazy to write the test after you have already fixed the defect.

