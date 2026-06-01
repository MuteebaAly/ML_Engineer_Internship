
# import libraries

# In[ ]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os



# Load iris dataset
# 

# In[ ]:


#---- if downloaded datset is given then  we can load dataset from pandas like this -----
#data=pd.read_csv("file path")

#seaborn directly create a dataframe in the backend
df=sns.load_dataset('iris')
print(df)


# show shape

# In[ ]:
df.shape
# show column names

# In[ ]:
df.columns
# show few rows

# In[ ]:
df.head()
#Also put the number of rows in parameter
#df.head(10)


# Show the structure of the data

# In[ ]:


df.info()


# show the maths statistical summary

# In[ ]:


df.describe()


# Visualize the dataset by using scatter plot that show the relationships between petal_Length and petal_width

# In[ ]:


sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", palette="Set1")

plt.title("Iris Dataset: Petal Length vs Petal Width")
plt.xlabel("petal_length(cm)")
plt.ylabel("petal_width(cm)")
plt.show()


# Scatterpot >>> show the relationship between sepal_length and sepal_width

# In[ ]:


sns.scatterplot(data=df, x="sepal_length", y="sepal_width",hue="species",palette="dark")
plt.xlabel("sepal_length(cm)")
plt.ylabel("sepal_width(cm)")
plt.title("Iris Dataset: Sepal Length vs sepal Width")
plt.show()


# Histplot of petal length >>> shows that how much flowers is present in the dataset in specific range

# In[ ]:


sns.histplot(data=df,x="petal_length")

plt.xlabel("Petal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Overall Distribution of Petal Lengths in Iris Dataset")
plt.show()

#its shows that k kitny flowers hai jinki length in ranges mai hai pooray dataset mai sai


# Histogram of Petal_length of Every Species >>> shows that in every specie how much flower have petal_length is in specific range
# 

# In[ ]:


sns.histplot(data=df,x="petal_length",hue="species")

plt.xlabel("Petal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Species Distribution of Petal Length in Iris Dataset")
plt.show()

#ye mujhy bataraha hai k har species mai kitny flowers hai jinki length in ranges mai hai


# Histogram of Petal_width  >>> shows that in all dataset how much flower have petal_width is in specific range
# 

# In[ ]:


sns.histplot(data=df,x="petal_width")

plt.xlabel("Petal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Overall Distribution of Petal Width in Iris Dataset")
plt.show()

#ye mujhy bataraha hai k sarey datset  mai kitny flowers hai jinki width in ranges mai hai


# Histogram of Petal_width of Every Species >>> shows that in every specie how much flower have petal_width is in specific range
# 

# In[ ]:


sns.histplot(data=df,x="petal_width",hue="species")

plt.xlabel("Petal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Species Distribution of Petal width in Iris Dataset")
plt.show()

#ye mujhy bataraha hai k har species mai kitny flowers hai jinki width in ranges mai hai


# Histogram of sepal_length >>> shows that in all dataset  how much flowers have sepal_length in specific range

# In[ ]:


sns.histplot(data=df,x="sepal_length")

plt.xlabel("sepal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Overall Distribution of sepal_length in Iris Dataset")
plt.show()

#ye mujhy bataraha hai ky pooray datasets mai sai kitny flowers hai jinki sepal_length in ranges mai hai


# Histogram of sepal_length of every specie >>> shows that in every specie how much flowers have sepal_length in specific range

# In[ ]:


sns.histplot(data=df,x="sepal_length",hue="species")

plt.xlabel("sepal_length(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Specie Distribution of sepal_length in Iris Dataset")
plt.show()


# Histogram of sepal_width >>> shows that in all dataset  how much flowers have sepal_width in specific range

# In[ ]:


sns.histplot(data=df,x="sepal_width")

plt.xlabel("sepal_width(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Overall Distribution of sepal_width in Iris Dataset")
plt.show()


# Histogram of sepal_width of every specie >>> shows that in every specie how much flowers have sepal_width in specific range

# In[ ]:


sns.histplot(data=df,x="sepal_width",hue="species")

plt.xlabel("sepal_width(cm)")
plt.ylabel("Numbers Of flowers")
plt.title("Specie Distribution of sepal_width in Iris Dataset")
plt.show()


# BoxPlot of all outlier

# In[ ]:


sns.boxplot(data=df, palette="Set2")


plt.title("Box Plot of All Numerical Features in Iris Dataset")
plt.xlabel("all species")
plt.ylabel("lenght in cm")
plt.show()

#after showing graph outliers are detect  only in the sepal width column


# Boxplot of petal_length of every specie

# In[ ]:


sns.boxplot(data=df, x="species", y="petal_length", palette="Set2")

plt.title("Box Plot of Petal Length for Each Species")
plt.xlabel("Flower Species")
plt.ylabel("Petal Length (cm)")
plt.show()


#In this outliers are detected in the setosa and versicolor in the petal length column


# In[ ]:


sns.boxplot(data=df, x="species", y="sepal_length", palette="Set2")

plt.title("Box Plot of sepal Length for Each Species")
plt.xlabel("Flower Species")
plt.ylabel("sepal Length (cm)")
plt.show()


#In this outliers are detected in the virginica in the sepal length column


# In[ ]:


sns.boxplot(data=df, x="species", y="petal_width", palette="Set2")

plt.title("Box Plot of Petal width for Each Species")
plt.xlabel("Flower Species")
plt.ylabel("Petal Width (cm)")
plt.show()


#In this outliers are detected only in the setosa  petal width column


# In[ ]:


sns.boxplot(data=df, x="species", y="sepal_width", palette="Set2")

plt.title("Box Plot of sepal width for Each Species")
plt.xlabel("Flower Species")
plt.ylabel("Sepal Width (cm)")
plt.show()


#In this outliers are detected o in the setosa and virginica sepal_width column

