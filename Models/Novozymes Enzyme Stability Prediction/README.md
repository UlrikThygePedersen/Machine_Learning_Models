# Novozymes Enzyme Stability Prediction - Random Forest Regressor Approach - [Kaggle](https://www.kaggle.com/competitions/novozymes-enzyme-stability-prediction/overview)

# Description

## Goal of the Competition

Enzymes are proteins that act as catalysts in the chemical reactions of living organisms. The goal of this competition is to predict the thermostability of enzyme variants. The experimentally measured thermostability (melting temperature) data includes natural sequences, as well as engineered sequences with single or multiple mutations upon the natural sequences.

Understanding and accurately predict protein stability is a fundamental problem in biotechnology. Its applications include enzyme engineering for addressing the world’s challenges in sustainability, carbon neutrality and more. Improvements to enzyme stability could lower costs and increase the speed scientists can iterate on concepts.

## Context

Novozymes finds enzymes in nature and optimizes them for use in industry. In industry, enzymes replace chemicals and accelerate production processes. They help our customers make more from less, while saving energy and generating less waste. Enzymes are widely used in laundry and dishwashing detergents where they remove stains and enable low-temperature washing and concentrated detergents. Other enzymes improve the quality of bread, beer and wine, or increase the nutritional value of animal feed. Enzymes are also used in the production of biofuels where they turn starch or cellulose from biomass into sugars which can be fermented to ethanol. These are just a few examples as we sell enzymes to more than 40 different industries. Like enzymes, microorganisms have natural properties that can be put to use in a variety of processes. Novozymes supplies a range of microorganisms for use in agriculture, animal health and nutrition, industrial cleaning and wastewater treatment.

However, many enzymes are only marginally stable, which limits their performance under harsh application conditions. Instability also decreases the amount of protein that can be produced by the cell. Therefore, the development of efficient computational approaches to predict protein stability carries enormous technical and scientific interest. 

Computational protein stability prediction based on physics principles have made remarkable progress thanks to advanced physics-based methods such as FoldX, Rosetta, and others. Recently, many machine learning methods were proposed to predict the stability impact of mutations on protein based on the pattern of variation in natural sequences and their three dimensional structures. More and more protein structures are being solved thanks to the recent breakthrough of AlphaFold2. However, accurate prediction of protein thermal stability remains a great challenge.

In this competition, Novozymes invites you to develop a model to predict/rank the thermostability of enzyme variants based on experimental melting temperature data, which is obtained from Novozymes’s high throughput screening lab. You’ll have access to data from previous scientific publications. The available thermostability data spans from natural sequences to engineered sequences with single or multiple mutations upon the natural sequences. If successful, you'll help tackle the fundamental problem of improving protein stability, making the approach to design novel and useful proteins, like enzymes and therapeutics, more rapidly and at lower cost.

Novozymes is the world’s leading biotech powerhouse. Our growing world is faced with pressing needs, emphasizing the necessity for solutions that can ensure the health of the planet and its population. At Novozymes, we believe biotech is at the core of connecting those societal needs with the challenges and opportunities our customers face. Novozymes is the global market leader in biological solutions, producing a wide range of enzymes, microorganisms, technical and digital solutions which help our customers, amongst other things, add new features to their products and produce more from less.

Together, we find biological answers for better lives in a growing world. Let’s Rethink Tomorrow. This is Novozymes’ purpose statement. Novozymes strives to have great impact by balancing good business for our customers and our company, while spearheading environmental and social change. In 2021, Novozymes enabled savings of 60 million tons of CO2 in global transport.

# Evaluation

Submissions are evaluated on the Spearman's correlation coefficient between the ground truth and the predictions.

Submission File
Each ```seq_id``` represents a single-mutation variant of an enzyme. Your task is to rank the stability of these variants, assigning greater ranks to more stable variants. For each ```seq_id``` in the test set, you must predict the value for for the target ```tm```. The file should contain a header and have the following format:

```
seq_id,tm
31394,9.7
31395,56.3
31396,112.4
etc.
```

# Timeline

* September 21, 2022 - Start Date.

* December 27, 2022 - Entry Deadline. You must accept the competition rules before this date in order to compete.

* December 27, 2022* - Team Merger Deadline. This is the last day participants may join or merge teams.

* January 3, 2023 - Final Submission Deadline.

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.

# Data Visualization

## Jointplot of pH and tm

<!-- Machine Learning AI image -->
<p align="center">
  <img  src="jointplot.png">
</p>