# <ins>Food Inflation Dashboard </ins>

An dynamic Python dashboard which allows the exploration and comparison of food inflation across the world.

- Data utilised is from: Food and Agriculture Organization of the United
Nations [https://www.fao.org/faostat/en/#home]
- Food Inflation (CPI) is measured by the change in the cost of a basket of goods measured in terms of annual growth relative to 2015 (set as the base year). 
 

![alt text](https://github.com/TanzeelN/Food-Inflation-Dashboard/blob/main/data/Demonstration_Overall.png "Dashboard")

## Dashboard Components

<ins>Inputs</ins>
- Light or Dark Mode: Change UI color scheme
- Continent & World Selection: Update geographical ccope of food inflation data 
- Year Filter: Range of years constraint.

<ins>Outputs</outputs>
- Continent Line Graph: Comapres the continent selected to the world average in the given range of years.
- Time Series Map: Animated visual display of how inflation grows to highlight regions of activity within the continent/world.
- Country Bar Chart: For the filters selected, the highest impacting countries contributing to the continent food inflation average.
  
Note: The highest impacting countries in the country bar chart is determined by the largest growth in the range of years selected.



## Usage
1) Clone github repo in your source editor
2) Execute requirements.txt
3) Run app by executing "python ./app.py"
