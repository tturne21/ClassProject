# EV Market Analysis in the U.S.
Authors: Tiana T., Daniel L., Drew P., Jason M., Joshua J., Matthew C., Tatiana S.

Please review our full analysis in our [Code Folder](./Code/) as well as our [presentation slides](./Savvy%20Coders%20Class%20Project%20December%202023.pptx).

## Overview
This project aims to explore the current state and potential growth of the electric vehicle (EV) market in the United States. Through data analytics, it focuses on two main objectives:

1. Investment Trends in EVs: Analyzing the increasing investment in EVs within the U.S. and comparing the country's position globally.

2. Identifying Key Regions for EV Charging Infrastructure: Pinpointing areas or regions in need of, or lacking, EV charging infrastructure for strategic investment decisions at the state and city levels.

Using data-driven analysis, this project seeks to provide actionable insights for stakeholders and investors in the evolving landscape of the U.S. EV market.

## Project Objectives
1. Assessing Investment Trends in EVs:
    - Investigate the investment trends in EVs within the U.S.
    - Compare the U.S. EV market with the global market to understand its standing and potential growth. 
2. Identifying Key Regions for EV Charging Infrastructure:
    - Determine areas or regions lacking adequate EV charging infrastructure or exhibiting high demand.
    - State-wise analysis:
        - Preferred State for Investment: Reasons and justifications.
        - State to Avoid for Investment: Reasons and justifications.
    - City-wise analysis:
        - Preferred City for Investment: Reasons and justifications.
        - City to Avoid for Investment: Reasons and justifications.
    - Consideration of Other Geographical Features impacting EV market growth.

## Data Sources
The analysis in this project was conducted using a combination of datasets obtained from various sources, including those provided by our instructor and external sources:

1. EV Registration Count by State: Dataset providing the count of registered electric vehicles per state.
2. Alternative Fuel Stations: Data detailing the locations and information about alternative fuel stations.
3. IEA Global EV 2030 Projections Data (2023): Dataset from the International Energy Agency (IEA) containing global projections for electric vehicles in 2030 as of 2023.
4. Motor Vehicle Registration Counts by State: Dataset presenting the count of registered motor vehicles per state.
5. State Populations: Data containing population statistics at the state level.
6. City-Level Data: Dataset with specific information at the city level. Obtained from [SimpleMaps](https://simplemaps.com/data/us-cities).
7. State-Level Data: Additional dataset offering comprehensive data at the state level.

The combination of these instructor-provided datasets and externally sourced data from SimpleMaps facilitated a comprehensive analysis of the EV market and charging infrastructure across various geographical levels within the United States.

## Methodology
### Tools Used
#### Excel
- Utilized to create pivot tables, graphs, and tables for analyzing IEA global US sales, US versus world data, and sales by county.
- Used for combining datasets to analyze total motor vehicle counts, EV registration counts, state populations, and ratios between EV counts and motor vehicle registrations.
#### Python
- Employed for data cleaning and manipulation of datasets to extract relevant information for analysis.
#### SQL
- Used for executing simple queries to extract specific insights from the datasets.
#### Tableau
- Leveraged for visualizing city-level data, state-level data, and alternative fuel station information.
- Enabled the creation of visual representations such as percent of EV registrations by state, ratio of EV charging stations to EV registrations, comparison of EV registrations versus charging station ratios, number of charging stations per capita, and city population maps.
### Data Processing Steps
- Excel: Pivot tables, graphs, and data merging for comprehensive analysis of EV registration counts, motor vehicle totals, state populations, and their ratios.
- Python: Data cleaning and extraction of relevant information from datasets.
- SQL: Executing queries for specific insights.
- Tableau: Visual representation and exploration of city-level and state-level data along with alternative fuel station analysis.

These tools and methods were strategically employed to cleanse, merge, and analyze the datasets, enabling comprehensive insights into the EV market and charging infrastructure across various geographical levels within the United States.

## Analysis and Findings
### EV Sales Trends
- US EV Sales: Show an increasing trend.

![graph1](./Images/Screenshot%202023-12-10%20140913.png)
- Global EV Sales: Increasing at a higher rate compared to the US.

![graph2](./Images/Screenshot%202023-12-10%20141008.png)
- China's Position: Leads in EV sales globally, with the USA following as the second-largest market.

![graph3](./Images/Screenshot%202023-12-10%20141128.png)
### State-Level Analysis
- California: Boasts the highest number of EVs per vehicle registered in the US.
- New Jersey: Reports the fewest charging stations per EV.
- California: Stands out as having both the highest number of EVs per vehicle registered and being among the fewest in charging stations per EV, making it a top recommendation for investment.
- North Dakota: Shows the third-lowest number of EVs per vehicle registered and the highest number of charging stations per EV, indicating it's advisable to avoid investment.

![graph4](./Images/Screenshot%202023-12-10%20141853.png) ![graph5](./Images/Screenshot%202023-12-10%20141916.png)
### City-Level Analysis
- California's Demand: Exhibits the highest demand considering both EVs per vehicle registered and charging stations per EV.
- San Buenaventura: Reports zero charging stations per capita.
- Santa Clara: Records the highest number of charging stations per capita.
- San Buenaventura, CA: Among cities with populations over 100K, reports the fewest EV charging stations per capita.
- Santa Clara: Leads in the number of charging stations per capita among cities with populations over 100K.

![graph6](./Images/Screenshot%202023-12-10%20141952.png)

These insights provide a comprehensive overview of the varying EV market and charging infrastructure scenarios across different states and cities in the US, guiding investment recommendations and highlighting areas with high demand and potential for improvement..

## Conclusion
The analysis conducted on the EV market in the United States reveals dynamic trends and varying infrastructure scenarios across states and cities. While US EV sales are on the rise, the global market, particularly led by China, is growing at a faster pace. California emerges as a frontrunner with the highest EVs per vehicle registered, indicating its strong market penetration. However, disparities exist in charging infrastructure, with New Jersey having the fewest charging stations per EV and North Dakota presenting a different dynamic, making it advisable to avoid investment.

### Recommendations
- Investment Strategy:
    - State-level: California stands out as a prime state for investment due to its high EV adoption despite a comparatively lower number of charging stations per EV.
    - City-level: Santa Clara exhibits a robust charging infrastructure, while San Buenaventura faces a notable lack of charging stations per capita.
### Next Steps
- Charging Station Types:
    - Recommendation: Assess the demand in different regions to determine the most beneficial mix of charging station types (e.g., fast charging, standard charging) based on consumer needs and vehicle preferences.
- Pricing and Rate Structures:
    - Recommendation: Conduct a pricing and rate structure analysis to optimize the charging station economics. Evaluate factors such as usage patterns, peak demand times, and regional variations to design sustainable and attractive pricing models for EV charging.

These next steps aim to further optimize the EV market infrastructure by tailoring charging station types and developing pricing structures that align with consumer needs while ensuring economic viability for stakeholders.

## For More Information
Please review our full analysis in our [Code Folder](./Code/) as well as our [presentation slides](./Savvy%20Coders%20Class%20Project%20December%202023.pptx).

## Repository Structure

```
├── Code
│   ├── EV Charging Station Investment.twbx
│   ├── EV_project_class.ipynb
│   ├── IEA_Global_EV_2030_Projections_Data_2023_Question_1.xlsx
│   ├── Ratio_Totals.csv
│   └── Ratios_and_Populations.xlsx
├── Data
├── README.md
└── Savvy Coders Class Project December 2023.pptx

```