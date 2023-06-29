# ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures
 Dyslexia is the most common neurological learning disability. It’s linked to genes, which 
 is why the condition runs in families.Early detection of Dyslexia will be very useful as it
 can be avoided a high rates of academic failure. So , if we predict Dyslexia as early as 
 possible then doctor can start the treatment soon. We conduct a Comparative study of different
 features for prediction analysis of Dyslexia.
 ## Summary
 Developed different machine learning approach to detect dyslexia using different feature selection method.
 Feature selection method: 1) Selected features using mutual information gain. 2) Selected phonological 
 awareness related features. we analysed different features for prediction analysis of Dyslexia for model
 improvement. 
 ## About the Dataset
 Used game dataset. In this game, there are mainly 32 questions and 3644 participants with an age range of 7 
 to 17 years old. To quantify task performance, there are 6 dependent measures – i) number of Clicks ii) number 
 of correct answers(Hits) iii) number of incorrect answers(Misses) iv) Score defined as sum of Hits per set of 
 exercises v) Accuracy, defined as the number of Hits divided by the number of Clicks (vi) Missrate, defined as
 the number of Misses divided by the number of Clicks
 Link of the dataset is : https://doi.org/10.34740/kaggle/dsv/1617514
## Data Preparation
There is no missing and duplicate value in the dataset. Droped unnecessary columns from the dataset. Transformed 
categorical features into numerical features using label encoding method.
## Exploratory Data Analysis
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/3f318cc1-76bc-4319-91c5-843838b36f57)
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/83a84642-d796-4e55-beed-789853ed3b91)
Observation : 
1) Average hits of non-dyslexic person is more than average hits of dyslexic person.
2) Average hits for 13 to 17 years old person is more than average hits for 7 to 12 years old person.
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/726752a9-abe4-4c5a-aa33-e821241ff95b)
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/f92a71ee-6a0a-47ba-a7bf-04062411a49c)
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/d6b6d3e1-38b1-4696-a0aa-c36b304ae302)
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/ccd750e5-20e0-432b-aa2b-f0c3c1330a2c)
![image](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/cb1eaf77-0325-45f4-b485-69412cbdb2e5)
Observation :
3) For dyslexic male candidate average of average accuracy is more than half of its value ( i.e, 5 with respect to 10) and for dyslexic female candidate average of average accuracy is less than half of its value.
4) For dyslexic male candidate average of average misses is more than 1 and for dyslexic female candidate average of average misses is less than 1.
5) Average of average missrate for dyslexic male candidate is almost double than the value of average of average missrate for dyslexic female candidate.
6) Average of average score for both dyslexic male and female candidates are same.
7) Average of average hits for both dyslexic male and female candidates are almost same.
## System Training and Classification
Used Extreme gradient boosting, Adaptive boosting, K-nearest neighbours and Random forest for classification.

Extreme gradient boosting for mutual information gain method:

![Screenshot (103)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/be2b2934-524c-4b25-943c-89c09c53c081)

Extreme gradient boosting for phonological aswareness related featrures:

![Screenshot (118)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/d368b489-8379-4d02-bc54-37424f1e82db)


Adaptive boosting for mutual information gain method:

![Screenshot (107)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/a928a859-83c4-499c-a78a-90e8d75ae471)

Adaptive boosting for phonological aswareness related featrures:

![Screenshot (109)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/1e7ac447-1643-429d-ac99-897c43413e30)

KNN for mutual information gain method:

![Screenshot (111)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/58ebea89-1b9a-4eb0-b66c-ad9c84494571)

KNN for phonological aswareness related featrures:

![Screenshot (113)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/32830860-af90-46a4-a837-5066049798ee)

Random Forest for mutual information gain method:

![Screenshot (117)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/09754fff-2368-4eb0-b8ca-e99701aac27c)

Random Forest for phonological aswareness related featrures:

![Screenshot (115)](https://github.com/ShyamashreeGhorai1/ComparativeStudyOnDyslexiaUsingPsycho-PhysiologicalFeatures/assets/131132617/d512afe8-f218-4348-8594-ece2165ede85)


## Conclusion
Dyslexia is a learning disability that affects about 10% of the world population. It is very important to identify dyslexic
children at an early stage. This study applied XGBoost, AdaBoost, KNN and Random Forest model to detect dyslexia using 
different feature selection methods. Objective of this study is comparative study of different features for prediction analysis
of Dyslexia. XGBoost model achieved 87 % of predictive accuracy with recall 74 % (using 1st feature selection method which is
better than 2nd one). AdaBoost model achieved 90 % of predictive accuracy with 40 % recall (using 1st feature selection method
which is better than 2nd one). KNN model achieved 90 % of predictive accuracy with recall 38 % (using 1st feature selection 
method which is better than 2nd one). Random Forest model achieved 84 % of predictive accuracy with 62 % recall (using 1st
feature selection method). Random Forest model achieved 88 % predictive accuracy with 47 % recall (using 2nd feature selection method).
 




















