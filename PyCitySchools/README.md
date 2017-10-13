

```python
# import dependencies 
import pandas as pd
```


```python
# reading schools_complete file
schools = 'raw_data/schools_complete.csv'
schools = pd.read_csv(schools)
# print all observations of the data 
schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# District summary 
## Total schools
total_school = schools['name'].count()
total_school 
```




    15




```python
## Total students
total_student = schools['size'].sum()
total_student
```




    39170




```python
# Total budget
total_budget = schools['budget'].sum()
total_budget
```




    24649428




```python
# reading students data 
students = 'raw_data/students_complete.csv'
students = pd.read_csv(students)
students.shape
```




    (39170, 7)




```python
students.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Average math score in the district
average_math_score = students['math_score'].mean()
average_math_score
```




    78.98537145774827




```python
# Average reading score in the district 
average_reading_score = students['reading_score'].mean()
average_reading_score
```




    81.87784018381414




```python
# Passing rate in Math in the district 
math_pass_rate = len(students[students['math_score']>=70])*100/len(students)
math_pass_rate
```




    74.9808526933878




```python
# Passing rate in reading in the district 
reading_pass_rate = len(students[students['reading_score']>=70])*100/len(students)
reading_pass_rate
```




    85.80546336482001




```python
# Overall pass rate in the district
average_pass_rate = (math_pass_rate + reading_pass_rate)/2
average_pass_rate
```




    80.39315802910392




```python
# Create a new table consolodating above calculations for district summary 
district_summary = pd.DataFrame({"Total Schools": [total_school],
                                   "Total Students": [total_student],
                                   "Total Budget": [total_budget],
                                   "Average Math Score": [average_math_score],
                                   "Average Reading Score": [average_reading_score],
                                   "% Passing Math":[math_pass_rate],
                                   "% Passing Reading":[reading_pass_rate],
                                   "Overall Pass Rate": [average_pass_rate]
                                   })
district_summary = district_summary[["Total Schools", 
                                     "Total Students", 
                                     "Total Budget", 
                                     "Average Math Score", 
                                     "Average Reading Score", 
                                     "% Passing Math", 
                                     "% Passing Reading",
                                     "Overall Pass Rate"]]

district_summary = district_summary.round(2)

district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Pass Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>74.98</td>
      <td>85.81</td>
      <td>80.39</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Improve formatting before outputting spreadsheet
district_summary["% Passing Math"] = district_summary["% Passing Math"].map("{0:,.2f}%".format)
district_summary["% Passing Reading"] = district_summary["% Passing Reading"].map("{0:,.2f}%".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${0:,.0f}".format)
district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Pass Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>$24,649,428</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>80.39</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Renaming 'school name' column of schools and students so that they can be merged 
schools.rename(columns ={'name': 'School Name'}, inplace=True)
students.rename(columns = {'school': 'School Name'}, inplace=True)
```


```python
# Compute average math score for each school and convert into dataframe
avg_math_perSchool = pd.DataFrame(students['math_score'].groupby(students['School Name']).mean())
avg_math_perSchool.reset_index(inplace=True)
avg_math_perSchool.rename(columns = {'math_score': 'Average Math \nScore'}, inplace=True)
avg_math_perSchool.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Average Math 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>77.048432</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.061895</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>76.711767</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.102592</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.351499</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average reading score for each school and convert into dataframe
avg_read_perSchool = pd.DataFrame(students['reading_score'].groupby(students['School Name']).mean())
avg_read_perSchool.reset_index(inplace = True)
avg_read_perSchool.rename(columns = {'reading_score': 'Average Reading \nScore'}, inplace=True)
avg_read_perSchool.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.033963</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.975780</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.158020</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.746258</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.816757</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge schools, math and reading tables and create school summary table 
schools_summary = pd.merge(pd.merge(schools, avg_math_perSchool, on='School Name'), avg_read_perSchool, on ='School Name')
schools_summary.rename(columns ={'size': 'Total Students'}, inplace=True)

# Compute per student budget in the summary table 
schools_summary['Per Student Budget']=  schools_summary['budget']/schools_summary['Total Students']
schools_summary.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>School Name</th>
      <th>type</th>
      <th>Total Students</th>
      <th>budget</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>Per Student Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>600.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>625.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
## COmpute pass rate in math and reading for each school 

# Compute total students for each school and reset index 
school_size_df = pd.DataFrame(students['name'].groupby(students['School Name']).count())
school_size_df.reset_index(inplace=True)
school_size_df.rename(columns = {'name': 'total students'}, inplace=True)

# Creating subset of dataframe who pass math score 
math_pass_df = students[students['math_score']>70]

# Compute number of students who passed math by school 
math_pass_df = pd.DataFrame(math_pass_df['name'].groupby(math_pass_df['School Name']).count())
math_pass_df.reset_index(inplace=True)

# Merge total students and number of students who passed math 
math_pass_df = pd.merge(school_size_df, math_pass_df, on = 'School Name')
math_pass_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing math for each school 
math_pass_df['% Passing Math'] = math_pass_df['number of students passed']/math_pass_df['total students']*100
math_pass_df = math_pass_df.loc[:,('School Name', '% Passing Math')]
math_pass_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>% Passing Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>64.630225</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>89.558665</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>63.750424</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>65.753925</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>89.713896</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Creating subset of dataframe who pass reading
read_pass_df = students[students['reading_score']>70]

# Compute number of students who passed reading by school 
read_pass_df = pd.DataFrame(read_pass_df['name'].groupby(read_pass_df['School Name']).count())
read_pass_df.reset_index(inplace=True)
read_pass_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Merge total students and number of students who passed reading
read_pass_df = pd.merge(school_size_df, read_pass_df, on = 'School Name')

# Compute percent passing reading for each school 
read_pass_df['% Passing Reading'] = read_pass_df['number of students passed']/read_pass_df['total students']*100
read_pass_df =read_pass_df.loc[:, ('School Name', '% Passing Reading')]
read_pass_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>% Passing Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>79.300643</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>93.864370</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>78.433367</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.510040</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>93.392371</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merging math and reading pass rate dataframe
school_pass_df = pd.merge(math_pass_df, read_pass_df, on ='School Name')

# Compute overall passing rate per school 
school_pass_df['Overall Passing Rate'] = (school_pass_df['% Passing Math']+school_pass_df['% Passing Reading'])/2
school_pass_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>71.965434</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
  </tbody>
</table>
</div>




```python
# School Summary 
schools_summary_df = pd.merge(schools_summary, school_pass_df, on ='School Name')

# Renaming variables 
schools_summary_df.rename(columns ={'type':'School Type','budget': 'Total budget'}, inplace=True)

# Deselect school id 
schools_summary_df = schools_summary_df.iloc[:,1:11]
schools_summary_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total budget</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>Per Student Budget</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>655.0</td>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>639.0</td>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>600.0</td>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>652.0</td>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>625.0</td>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>91.553134</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_summary_df.dtypes
```




    School Name                 object
    School Type                 object
    Total Students               int64
    Total budget                 int64
    Average Math \nScore       float64
    Average Reading \nScore    float64
    Per Student Budget         float64
    % Passing Math             float64
    % Passing Reading          float64
    Overall Passing Rate       float64
    dtype: object




```python
# Formating Schools Summary Table 
schools_summary_df["Average Math \nScore"] = schools_summary_df["Average Math \nScore"].map("{0:,.2f}".format)
schools_summary_df["Average Reading \nScore"] = schools_summary_df["Average Reading \nScore"].map("{0:,.2f}".format)
schools_summary_df["Total budget"] = schools_summary_df["Total budget"].map("${0:,.0f}".format)
schools_summary_df["Per Student Budget"] = schools_summary_df["Per Student Budget"].map("${0:,.2f}".format)
schools_summary_df["% Passing Math"] = schools_summary_df["% Passing Math"].map("{0:,.2f}%".format)
schools_summary_df["% Passing Reading"] = schools_summary_df["% Passing Reading"].map("{0:,.2f}%".format)
schools_summary_df["Overall Passing Rate"] = schools_summary_df["Overall Passing Rate"].map("{0:,.2f}%".format)
schools_summary_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total budget</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>Per Student Budget</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>$655.00</td>
      <td>63.32%</td>
      <td>78.81%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>$639.00</td>
      <td>63.75%</td>
      <td>78.43%</td>
      <td>71.09%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>$600.00</td>
      <td>89.89%</td>
      <td>92.62%</td>
      <td>91.25%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>$652.00</td>
      <td>64.75%</td>
      <td>78.19%</td>
      <td>71.47%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>$625.00</td>
      <td>89.71%</td>
      <td>93.39%</td>
      <td>91.55%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>$578.00</td>
      <td>90.93%</td>
      <td>93.25%</td>
      <td>92.09%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>$582.00</td>
      <td>89.56%</td>
      <td>93.86%</td>
      <td>91.71%</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>$628.00</td>
      <td>64.63%</td>
      <td>79.30%</td>
      <td>71.97%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>$581.00</td>
      <td>90.63%</td>
      <td>92.74%</td>
      <td>91.69%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>$609.00</td>
      <td>91.68%</td>
      <td>92.20%</td>
      <td>91.94%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400</td>
      <td>83.68</td>
      <td>83.95</td>
      <td>$583.00</td>
      <td>90.28%</td>
      <td>93.44%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>$637.00</td>
      <td>64.07%</td>
      <td>77.74%</td>
      <td>70.91%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>$650.00</td>
      <td>63.85%</td>
      <td>78.28%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>$644.00</td>
      <td>65.75%</td>
      <td>77.51%</td>
      <td>71.63%</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>$1,043,130</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>$638.00</td>
      <td>90.21%</td>
      <td>92.91%</td>
      <td>91.56%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a table that highlights the top 5 performing schools based on Overall Passing Rate
school_sorted = schools_summary_df.sort_values('Overall Passing Rate', ascending=False)

# Selecting top five school 
top_five_school = school_sorted.iloc[0:5 :,]
top_five_school
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total budget</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>Per Student Budget</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>$578.00</td>
      <td>90.93%</td>
      <td>93.25%</td>
      <td>92.09%</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>$609.00</td>
      <td>91.68%</td>
      <td>92.20%</td>
      <td>91.94%</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400</td>
      <td>83.68</td>
      <td>83.95</td>
      <td>$583.00</td>
      <td>90.28%</td>
      <td>93.44%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>$582.00</td>
      <td>89.56%</td>
      <td>93.86%</td>
      <td>91.71%</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>$581.00</td>
      <td>90.63%</td>
      <td>92.74%</td>
      <td>91.69%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Selecting bottom five school 
bottom_five_school = school_sorted.iloc[10:15 : ,]
bottom_five_school
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total budget</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>Per Student Budget</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>$652.00</td>
      <td>64.75%</td>
      <td>78.19%</td>
      <td>71.47%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>$639.00</td>
      <td>63.75%</td>
      <td>78.43%</td>
      <td>71.09%</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>$655.00</td>
      <td>63.32%</td>
      <td>78.81%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>$650.00</td>
      <td>63.85%</td>
      <td>78.28%</td>
      <td>71.07%</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>$637.00</td>
      <td>64.07%</td>
      <td>77.74%</td>
      <td>70.91%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Math Score by Grade by School 
avg_math_perSchoolGrade = pd.DataFrame(students.groupby(['School Name','grade'])['math_score'].mean().reset_index())
avg_math_perSchoolGrade.rename(columns = {'math_score': 'Average Math \nScore', 'grade': 'Grade'}, inplace=True)
avg_math_perSchoolGrade = avg_math_perSchoolGrade.sort_values(['School Name', 'Grade'], ascending=[True, False])
avg_math_perSchoolGrade.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Grade</th>
      <th>Average Math 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Bailey High School</td>
      <td>9th</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bailey High School</td>
      <td>12th</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>11th</td>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>10th</td>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Cabrera High School</td>
      <td>9th</td>
      <td>83.094697</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading Score by Grade by School 
avg_read_perSchoolGrade = pd.DataFrame(students.groupby(['School Name','grade'])['reading_score'].mean().reset_index())
avg_read_perSchoolGrade.rename(columns = {'reading_score': 'Average Reading \nScore', 'grade': 'Grade'}, inplace=True)
avg_read_perSchoolGrade = avg_read_perSchoolGrade.sort_values(['School Name', 'Grade'], ascending=[True, False])
avg_read_perSchoolGrade.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Grade</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Bailey High School</td>
      <td>9th</td>
      <td>81.303155</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bailey High School</td>
      <td>12th</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>11th</td>
      <td>80.945643</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>10th</td>
      <td>80.907183</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Cabrera High School</td>
      <td>9th</td>
      <td>83.676136</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by School Spending
schools_summary_sub = schools_summary.loc[:,('School Name', 'type', 'Total Students', 'Per Student Budget')]
schools_sub_df = pd.merge(students, schools_summary_sub, on ='School Name')
schools_sub_df['Per Student Budget'].describe()
```




    count    39170.000000
    mean       629.293541
    std         25.034815
    min        578.000000
    25%        625.000000
    50%        638.000000
    75%        650.000000
    max        655.000000
    Name: Per Student Budget, dtype: float64




```python
# Creating bins based on per student budget 
bins_budget = [575, 600, 625, 650, 675]
group_labels_budget = ["575 to 600", "601 to 625", "626 to 650", "651 to 675"]
schools_sub_df['budget_group'] =pd.cut(schools_sub_df['Per Student Budget'],bins_budget,labels=group_labels_budget)
schools_sub_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>School Name</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>type</th>
      <th>Total Students</th>
      <th>Per Student Budget</th>
      <th>budget_group</th>
      <th>student_group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average math score for each spending range 
avg_math_perBudget = pd.DataFrame(schools_sub_df['math_score'].groupby(schools_sub_df['budget_group']).mean())
avg_math_perBudget.reset_index(inplace=True)
avg_math_perBudget.rename(columns = {'math_score': 'Average Math \nScore', 'budget_group':'Spending Range'}, inplace=True)
avg_math_perBudget.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>Average Math 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>83.362283</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>83.544856</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>77.469253</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>77.034693</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average reading score for each spending range 
avg_read_perBudget = pd.DataFrame(schools_sub_df['reading_score'].groupby(schools_sub_df['budget_group']).mean())
avg_read_perBudget.reset_index(inplace=True)
avg_read_perBudget.rename(columns = {'reading_score': 'Average Reading \nScore', 'budget_group':'Spending Range'}, inplace=True)
avg_read_perBudget.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>83.912412</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>83.906996</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>81.162258</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>81.030323</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_reading_perBudget = pd.merge(avg_math_perBudget, avg_read_perBudget, on ='Spending Range')
math_reading_perBudget.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>83.362283</td>
      <td>83.912412</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>83.544856</td>
      <td>83.906996</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>77.469253</td>
      <td>81.162258</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>77.034693</td>
      <td>81.030323</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute total students for each spending range and reset index 
student_size_df = pd.DataFrame(schools_sub_df['name'].groupby(schools_sub_df['budget_group']).count())
student_size_df.reset_index(inplace=True)
student_size_df.rename(columns = {'name': 'total students'}, inplace=True)

# Create subset of dataframe who pass math score
mathPass_group_df = schools_sub_df[schools_sub_df['math_score']>70]

# Compute number of students who passed math by spending range 
mathPass_group_df = pd.DataFrame(mathPass_group_df['name'].groupby(mathPass_group_df['budget_group']).count())
mathPass_group_df.reset_index(inplace=True)

# Merge total students and number of students who passed math 
mathPass_group_df = pd.merge(student_size_df, mathPass_group_df, on = 'budget_group')
mathPass_group_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing math for each spending range 
mathPass_group_df['% Passing Math'] = mathPass_group_df['number of students passed']/mathPass_group_df['total students']*100
mathPass_group_df = mathPass_group_df.loc[:,('budget_group', '% Passing Math')]
mathPass_group_df.rename(columns = {'budget_group': 'Spending Range'}, inplace=True)
mathPass_group_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>% Passing Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>90.232501</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>90.493827</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>66.356427</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>64.194915</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Creating subset of dataframe who pass math score 
readPass_group_df = schools_sub_df[schools_sub_df['reading_score']>70]

# Compute number of students who passed math for each spending range 
readPass_group_df = pd.DataFrame(readPass_group_df['name'].groupby(readPass_group_df['budget_group']).count())
readPass_group_df.reset_index(inplace=True)

# Merge total students and number of students who passed math 
readPass_group_df = pd.merge(student_size_df, readPass_group_df, on = 'budget_group')
readPass_group_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing math for each spending range 
readPass_group_df['% Passing Reading'] = readPass_group_df['number of students passed']/readPass_group_df['total students']*100
readPass_group_df = readPass_group_df.loc[:,('budget_group', '% Passing Reading')]
readPass_group_df.rename(columns={'budget_group': 'Spending Range'}, inplace=True)
readPass_group_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>% Passing Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>93.271005</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>92.921811</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>79.476708</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>78.429555</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by School Spending
mathRead_pass_df = pd.merge(mathPass_group_df,readPass_group_df, on ='Spending Range')
spendingRange_summary = pd.merge(math_reading_perBudget,mathRead_pass_df, on='Spending Range')
spendingRange_summary.rename(columns ={'reading_score':'Average Reading Score'}, inplace=True)
spendingRange_summary['Overall Passing Rate']= (spendingRange_summary['% Passing Math']+
                                                spendingRange_summary['% Passing Reading'])/2
spendingRange_summary.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>83.362283</td>
      <td>83.912412</td>
      <td>90.232501</td>
      <td>93.271005</td>
      <td>91.751753</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>83.544856</td>
      <td>83.906996</td>
      <td>90.493827</td>
      <td>92.921811</td>
      <td>91.707819</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>77.469253</td>
      <td>81.162258</td>
      <td>66.356427</td>
      <td>79.476708</td>
      <td>72.916568</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>77.034693</td>
      <td>81.030323</td>
      <td>64.194915</td>
      <td>78.429555</td>
      <td>71.312235</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Formating summary table based on school spending (per student) 
spendingRange_summary["Average Math \nScore"] = spendingRange_summary["Average Math \nScore"].map("{0:,.2f}".format)
spendingRange_summary["Average Reading \nScore"] = spendingRange_summary["Average Reading \nScore"].map("{0:,.2f}".format)
spendingRange_summary["% Passing Math"] = spendingRange_summary["% Passing Math"].map("{0:,.2f}%".format)
spendingRange_summary["% Passing Reading"] = spendingRange_summary["% Passing Reading"].map("{0:,.2f}%".format)
spendingRange_summary["Overall Passing Rate"] = spendingRange_summary["Overall Passing Rate"].map("{0:,.2f}%".format)
spendingRange_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>575 to 600</td>
      <td>83.36</td>
      <td>83.91</td>
      <td>90.23%</td>
      <td>93.27%</td>
      <td>91.75%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601 to 625</td>
      <td>83.54</td>
      <td>83.91</td>
      <td>90.49%</td>
      <td>92.92%</td>
      <td>91.71%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>626 to 650</td>
      <td>77.47</td>
      <td>81.16</td>
      <td>66.36%</td>
      <td>79.48%</td>
      <td>72.92%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>651 to 675</td>
      <td>77.03</td>
      <td>81.03</td>
      <td>64.19%</td>
      <td>78.43%</td>
      <td>71.31%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Analyze total students to find reasonable bins for school size 
schools_sub_df['Total Students'].describe()
```




    count    39170.000000
    mean      3332.957110
    std       1323.914069
    min        427.000000
    25%       1858.000000
    50%       2949.000000
    75%       4635.000000
    max       4976.000000
    Name: Total Students, dtype: float64




```python
# Create bins for school size 
bins_size = [400, 1000, 3000, 5000]
group_labels_size = ["Small (<1000)", "Medium (1000 to 3000)", "Large (>3000)"]
schools_sub_df['student_group'] =pd.cut(schools_sub_df['Total Students'],bins_size,labels=group_labels_size)
schools_sub_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>School Name</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>type</th>
      <th>Total Students</th>
      <th>Per Student Budget</th>
      <th>budget_group</th>
      <th>student_group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>District</td>
      <td>2917</td>
      <td>655.0</td>
      <td>651 to 675</td>
      <td>Medium (1000 to 3000)</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average math score for each school size 
avg_math_perSize = pd.DataFrame(schools_sub_df['math_score'].groupby(schools_sub_df['student_group']).mean())
avg_math_perSize.reset_index(inplace=True)
avg_math_perSize.rename(columns = {'math_score': 'Average Math \nScore', 'student_group':'School Size'}, inplace=True)
avg_math_perSize.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Math 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>83.828654</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>80.450902</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>77.070764</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average reading score for each school size 
avg_read_perSize = pd.DataFrame(schools_sub_df['reading_score'].groupby(schools_sub_df['student_group']).mean())
avg_read_perSize.reset_index(inplace=True)
avg_read_perSize.rename(columns = {'reading_score': 'Average Reading \nScore', 'student_group':'School Size'}, inplace=True)
avg_read_perSize.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>83.974082</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>82.626481</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>80.928365</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge math and reading score table for school size 
math_reading_perSize = pd.merge(avg_math_perSize, avg_read_perSize, on ='School Size')
math_reading_perSize.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>83.828654</td>
      <td>83.974082</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>80.450902</td>
      <td>82.626481</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>77.070764</td>
      <td>80.928365</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute total students for each size of school and reset index 
studentSize_df = pd.DataFrame(schools_sub_df['name'].groupby(schools_sub_df['student_group']).count())
studentSize_df.reset_index(inplace=True)
studentSize_df.rename(columns = {'name': 'total students'}, inplace=True)

# Creating subset of dataframe who pass math score 
mathPass_size_df = schools_sub_df[schools_sub_df['math_score']>70]

# Compute number of students who passed math by size of school 
mathPass_size_df = pd.DataFrame(mathPass_size_df['name'].groupby(mathPass_size_df['student_group']).count())
mathPass_size_df.reset_index(inplace=True)

# Merge total students and number of students who passed math 
mathPass_size_df = pd.merge(studentSize_df, mathPass_size_df, on = 'student_group')
mathPass_size_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing math for each school size
mathPass_size_df['% Passing Math'] = mathPass_size_df['number of students passed']/mathPass_size_df['total students']*100
mathPass_size_df = mathPass_size_df.loc[:,('student_group', '% Passing Math')]
mathPass_size_df.rename(columns ={'student_group': 'School Size'}, inplace= True)
mathPass_size_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>% Passing Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>91.360691</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>78.660484</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>64.335093</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Creating subset of dataframe who pass reading score 
readPass_size_df = schools_sub_df[schools_sub_df['reading_score']>70]

# Compute number of students who passed reading by school size
readPass_size_df = pd.DataFrame(readPass_size_df['name'].groupby(readPass_size_df['student_group']).count())
readPass_size_df.reset_index(inplace=True)

# Merge total students and number of students who passed reading 
readPass_size_df = pd.merge(studentSize_df, readPass_size_df, on = 'student_group')
readPass_size_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing reading for each school size
readPass_size_df['% Passing Reading'] = readPass_size_df['number of students passed']/readPass_size_df['total students']*100
readPass_size_df = readPass_size_df.loc[:,('student_group', '% Passing Reading')]
readPass_size_df.rename(columns ={'student_group': 'School Size'}, inplace= True)
readPass_size_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>% Passing Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>92.368611</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>86.609995</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>78.417070</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create summary table based on school size 
mathRead_pass_size = pd.merge(mathPass_size_df,readPass_size_df, on ='School Size' )
schoolSize_summary = pd.merge(math_reading_perSize, mathRead_pass_size, on = 'School Size')
schoolSize_summary['Overall Passing Rate'] = (schoolSize_summary['% Passing Math']+
                                                schoolSize_summary['% Passing Reading'])/2
schoolSize_summary.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>83.828654</td>
      <td>83.974082</td>
      <td>91.360691</td>
      <td>92.368611</td>
      <td>91.864651</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>80.450902</td>
      <td>82.626481</td>
      <td>78.660484</td>
      <td>86.609995</td>
      <td>82.635240</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>77.070764</td>
      <td>80.928365</td>
      <td>64.335093</td>
      <td>78.417070</td>
      <td>71.376082</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Formating summary table for school size 
schoolSize_summary["Average Math \nScore"] = schoolSize_summary["Average Math \nScore"].map("{0:,.2f}".format)
schoolSize_summary["Average Reading \nScore"] = schoolSize_summary["Average Reading \nScore"].map("{0:,.2f}".format)
schoolSize_summary["% Passing Math"] = schoolSize_summary["% Passing Math"].map("{0:,.2f}%".format)
schoolSize_summary["% Passing Reading"] = schoolSize_summary["% Passing Reading"].map("{0:,.2f}%".format)
schoolSize_summary["Overall Passing Rate"] = schoolSize_summary["Overall Passing Rate"].map("{0:,.2f}%".format)
schoolSize_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1000)</td>
      <td>83.83</td>
      <td>83.97</td>
      <td>91.36%</td>
      <td>92.37%</td>
      <td>91.86%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1000 to 3000)</td>
      <td>80.45</td>
      <td>82.63</td>
      <td>78.66%</td>
      <td>86.61%</td>
      <td>82.64%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3000)</td>
      <td>77.07</td>
      <td>80.93</td>
      <td>64.34%</td>
      <td>78.42%</td>
      <td>71.38%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average math score for each school type 
avg_math_perType = pd.DataFrame(schools_sub_df['math_score'].groupby(schools_sub_df['type']).mean())
avg_math_perType.reset_index(inplace=True)
avg_math_perType.rename(columns = {'math_score': 'Average Math \nScore', 'type':'School Type'}, inplace=True)
avg_math_perType.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.406183</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>76.987026</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute average reading score for each school type 
avg_read_perType = pd.DataFrame(schools_sub_df['reading_score'].groupby(schools_sub_df['type']).mean())
avg_read_perType.reset_index(inplace=True)
avg_read_perType.rename(columns = {'reading_score': 'Average Reading \nScore', 'type':'School Type'}, inplace=True)
avg_read_perType.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.902821</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>80.962485</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_reading_perType = pd.merge(avg_math_perType, avg_read_perType, on ='School Type')
math_reading_perType.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.406183</td>
      <td>83.902821</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>76.987026</td>
      <td>80.962485</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Compute total students for each school type and reset index 
studentType_df = pd.DataFrame(schools_sub_df['name'].groupby(schools_sub_df['type']).count())
studentType_df.reset_index(inplace=True)
studentType_df.rename(columns = {'name': 'total students'}, inplace=True)

# Creating subset of dataframe who pass math score 
mathPass_type_df = schools_sub_df[schools_sub_df['math_score']>70]

# Compute number of students who passed math by school type
mathPass_type_df = pd.DataFrame(mathPass_type_df['name'].groupby(mathPass_type_df['type']).count())
mathPass_type_df.reset_index(inplace=True)

# Merge total students and number of students who passed math 
mathPass_type_df = pd.merge(studentType_df, mathPass_type_df, on = 'type')
mathPass_type_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing math for each school type
mathPass_type_df['% Passing Math'] = mathPass_type_df['number of students passed']/mathPass_type_df['total students']*100
mathPass_type_df = mathPass_type_df.loc[:,('type', '% Passing Math')]
mathPass_type_df.rename(columns ={'type': 'School Type'}, inplace= True)
mathPass_type_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>% Passing Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>90.282106</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>64.305308</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Creating subset of dataframe who pass reading score 
readPass_type_df = schools_sub_df[schools_sub_df['reading_score']>70]

# Compute number of students who passed reading by school type
readPass_type_df = pd.DataFrame(readPass_type_df['name'].groupby(readPass_type_df['type']).count())
readPass_type_df.reset_index(inplace=True)

# Merge total students and number of students who passed reading 
readPass_type_df = pd.merge(studentType_df, readPass_type_df, on = 'type')
readPass_type_df.rename(columns = {'name': 'number of students passed'}, inplace=True)

# Compute percent passing reading for each school 
readPass_type_df['% Passing Reading'] = readPass_type_df['number of students passed']/readPass_type_df['total students']*100
readPass_type_df = readPass_type_df.loc[:,('type', '% Passing Reading')]
readPass_type_df.rename(columns ={'type': 'School Type'}, inplace= True)
readPass_type_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>% Passing Reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>93.152370</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>78.369662</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create summary table for school type 
mathRead_pass_type = pd.merge(mathPass_type_df,readPass_type_df, on ='School Type' )
schoolType_summary = pd.merge(math_reading_perType, mathRead_pass_type, on = 'School Type')
schoolType_summary['Overall Passing Rate'] = (schoolType_summary['% Passing Math']+
                                                schoolType_summary['% Passing Reading'])/2
schoolType_summary.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.406183</td>
      <td>83.902821</td>
      <td>90.282106</td>
      <td>93.152370</td>
      <td>91.717238</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>76.987026</td>
      <td>80.962485</td>
      <td>64.305308</td>
      <td>78.369662</td>
      <td>71.337485</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Formating summary table for school size 
schoolType_summary["Average Math \nScore"] = schoolType_summary["Average Math \nScore"].map("{0:,.2f}".format)
schoolType_summary["Average Reading \nScore"] = schoolType_summary["Average Reading \nScore"].map("{0:,.2f}".format)
schoolType_summary["% Passing Math"] = schoolType_summary["% Passing Math"].map("{0:,.2f}%".format)
schoolType_summary["% Passing Reading"] = schoolType_summary["% Passing Reading"].map("{0:,.2f}%".format)
schoolType_summary["Overall Passing Rate"] = schoolType_summary["Overall Passing Rate"].map("{0:,.2f}%".format)
schoolType_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math 
Score</th>
      <th>Average Reading 
Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.41</td>
      <td>83.90</td>
      <td>90.28%</td>
      <td>93.15%</td>
      <td>91.72%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>76.99</td>
      <td>80.96</td>
      <td>64.31%</td>
      <td>78.37%</td>
      <td>71.34%</td>
    </tr>
  </tbody>
</table>
</div>


