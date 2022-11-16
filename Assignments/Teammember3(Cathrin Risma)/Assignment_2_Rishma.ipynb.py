{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb380b52",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c06e2ee5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e1475ba4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('/Users/alfia/Desktop/Churn_Modelling.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "566065fc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>15619304</td>\n",
       "      <td>Onio</td>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>15701354</td>\n",
       "      <td>Boni</td>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>15737888</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "2          3    15619304      Onio          502    France  Female   42   \n",
       "3          4    15701354      Boni          699    France  Female   39   \n",
       "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
       "\n",
       "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2       0.00              1          1               1   \n",
       "1       1   83807.86              1          0               1   \n",
       "2       8  159660.80              3          1               0   \n",
       "3       1       0.00              2          0               0   \n",
       "4       2  125510.82              1          1               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  \n",
       "2        113931.57       1  \n",
       "3         93826.63       0  \n",
       "4         79084.10       0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f68a6bb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.000000e+04</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.00000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569094e+07</td>\n",
       "      <td>650.528800</td>\n",
       "      <td>38.921800</td>\n",
       "      <td>5.012800</td>\n",
       "      <td>76485.889288</td>\n",
       "      <td>1.530200</td>\n",
       "      <td>0.70550</td>\n",
       "      <td>0.515100</td>\n",
       "      <td>100090.239881</td>\n",
       "      <td>0.203700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2886.89568</td>\n",
       "      <td>7.193619e+04</td>\n",
       "      <td>96.653299</td>\n",
       "      <td>10.487806</td>\n",
       "      <td>2.892174</td>\n",
       "      <td>62397.405202</td>\n",
       "      <td>0.581654</td>\n",
       "      <td>0.45584</td>\n",
       "      <td>0.499797</td>\n",
       "      <td>57510.492818</td>\n",
       "      <td>0.402769</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.556570e+07</td>\n",
       "      <td>350.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>11.580000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2500.75000</td>\n",
       "      <td>1.562853e+07</td>\n",
       "      <td>584.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>51002.110000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569074e+07</td>\n",
       "      <td>652.000000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>97198.540000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>100193.915000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7500.25000</td>\n",
       "      <td>1.575323e+07</td>\n",
       "      <td>718.000000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>127644.240000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>149388.247500</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.581569e+07</td>\n",
       "      <td>850.000000</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>250898.090000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>199992.480000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         RowNumber    CustomerId   CreditScore           Age        Tenure  \\\n",
       "count  10000.00000  1.000000e+04  10000.000000  10000.000000  10000.000000   \n",
       "mean    5000.50000  1.569094e+07    650.528800     38.921800      5.012800   \n",
       "std     2886.89568  7.193619e+04     96.653299     10.487806      2.892174   \n",
       "min        1.00000  1.556570e+07    350.000000     18.000000      0.000000   \n",
       "25%     2500.75000  1.562853e+07    584.000000     32.000000      3.000000   \n",
       "50%     5000.50000  1.569074e+07    652.000000     37.000000      5.000000   \n",
       "75%     7500.25000  1.575323e+07    718.000000     44.000000      7.000000   \n",
       "max    10000.00000  1.581569e+07    850.000000     92.000000     10.000000   \n",
       "\n",
       "             Balance  NumOfProducts    HasCrCard  IsActiveMember  \\\n",
       "count   10000.000000   10000.000000  10000.00000    10000.000000   \n",
       "mean    76485.889288       1.530200      0.70550        0.515100   \n",
       "std     62397.405202       0.581654      0.45584        0.499797   \n",
       "min         0.000000       1.000000      0.00000        0.000000   \n",
       "25%         0.000000       1.000000      0.00000        0.000000   \n",
       "50%     97198.540000       1.000000      1.00000        1.000000   \n",
       "75%    127644.240000       2.000000      1.00000        1.000000   \n",
       "max    250898.090000       4.000000      1.00000        1.000000   \n",
       "\n",
       "       EstimatedSalary        Exited  \n",
       "count     10000.000000  10000.000000  \n",
       "mean     100090.239881      0.203700  \n",
       "std       57510.492818      0.402769  \n",
       "min          11.580000      0.000000  \n",
       "25%       51002.110000      0.000000  \n",
       "50%      100193.915000      0.000000  \n",
       "75%      149388.247500      0.000000  \n",
       "max      199992.480000      1.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c8cb658a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10000 entries, 0 to 9999\n",
      "Data columns (total 14 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   RowNumber        10000 non-null  int64  \n",
      " 1   CustomerId       10000 non-null  int64  \n",
      " 2   Surname          10000 non-null  object \n",
      " 3   CreditScore      10000 non-null  int64  \n",
      " 4   Geography        10000 non-null  object \n",
      " 5   Gender           10000 non-null  object \n",
      " 6   Age              10000 non-null  int64  \n",
      " 7   Tenure           10000 non-null  int64  \n",
      " 8   Balance          10000 non-null  float64\n",
      " 9   NumOfProducts    10000 non-null  int64  \n",
      " 10  HasCrCard        10000 non-null  int64  \n",
      " 11  IsActiveMember   10000 non-null  int64  \n",
      " 12  EstimatedSalary  10000 non-null  float64\n",
      " 13  Exited           10000 non-null  int64  \n",
      "dtypes: float64(2), int64(9), object(3)\n",
      "memory usage: 1.1+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f89b251b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "\n",
       "   Tenure   Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2      0.00              1          1               1   \n",
       "1       1  83807.86              1          0               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "92327eba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='CreditScore', ylabel='Density'>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df.CreditScore)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7f325417",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age', ylabel='Density'>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df.Age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b3f66f18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Gender.value_counts().plot(kind='barh')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d9a824ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Geography.value_counts().plot(kind='barh')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f2b20234",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Tenure.value_counts().plot(kind='barh')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "eca1ecdc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='EstimatedSalary', ylabel='Density'>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(df.EstimatedSalary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a9fb05c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Geography', ylabel='Exited'>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYgAAAEGCAYAAAB/+QKOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAXQUlEQVR4nO3df7RdZX3n8feHG6NDxFolgkOIiZqWRadgMaJd0CrTgQUONTiMA9Yl46+mWKl2dTlIpx2qY7tmoFZnStE040oZZxZSHE1XRqPAUJUp+CNBkQASTSNIiBkCKvirhMh3/jj7lsPNc+89N2Tn5pL3a627zt77eZ5zvjeby+fsffZ+TqoKSZImOmS2C5AkHZgMCElSkwEhSWoyICRJTQaEJKlp3mwXsC8dfvjhtWTJktkuQ5LmjJtvvvn+qlrYantSBcSSJUvYuHHjbJchSXNGkrsna/MUkySpqdeASHJ6ks1JtiS5qNG+IsmtSW5JsjHJyUNtdyXZNN7WZ52SpD31doopyRhwOXAqsA3YkGRdVd0x1O16YF1VVZLjgKuBY4baT6mq+/uqUZI0uT6PIE4EtlTV1qraBVwFrBjuUFU/rMfm+lgAOO+HJB0g+gyIo4B7hta3ddseJ8mrk9wJfAp401BTAdcmuTnJysleJMnK7vTUxp07d+6j0iVJfQZEGtv2OEKoqrVVdQxwFvDeoaaTquoE4AzgbUl+tfUiVbW6qpZX1fKFC5tXakmS9kKfAbENOHpofRGwfbLOVXUD8IIkh3fr27vH+4C1DE5ZSZL2kz4DYgOwLMnSJPOBc4F1wx2SvDBJuuUTgPnAA0kWJDms274AOA24rcdaJUkT9HYVU1XtTnIBcA0wBqypqtuTnN+1rwLOBs5L8gjwE+Cc7oqmI4C1XXbMA66sqs/0VaskTebCCy9kx44dHHnkkVx66aWzXc5+1eud1FW1Hlg/YduqoeVLgEsa47YCx/dZmySNYseOHdx7772zXcas8E5qSVKTASFJajIgJElNBoQkqcmAkCQ1GRCSpCYDQpLUZEBIkpoMCElSkwEhSWrqdaoNSZropMtOmu0SZmT+9+dzCIdwz/fvmTO13/g7N+6T5/EIQpLUZEBIkpoMCElSkwEhSWoyICRJTQaEJKnJgJAkNRkQkqQmA0KS1GRASJKaeg2IJKcn2ZxkS5KLGu0rktya5JYkG5OcPOpYSdof6tDi0QWPUofWbJey3/U2F1OSMeBy4FRgG7AhybqqumOo2/XAuqqqJMcBVwPHjDhWknr3yEmPzHYJs6bPI4gTgS1VtbWqdgFXASuGO1TVD6tqPJYXADXqWElSv/oMiKOAe4bWt3XbHifJq5PcCXwKeNNMxkqS+tNnQKSxbY+TeFW1tqqOAc4C3juTsQBJVnafX2zcuXPn3tYqSZqgz4DYBhw9tL4I2D5Z56q6AXhBksNnMraqVlfV8qpavnDhwidetSQJ6DcgNgDLkixNMh84F1g33CHJC5OkWz4BmA88MMpYSVK/eruKqap2J7kAuAYYA9ZU1e1Jzu/aVwFnA+cleQT4CXBO96F1c2xftUqS9tTrV45W1Xpg/YRtq4aWLwEuGXWsJGn/8U5qSVKTASFJajIgJElNBoQkqcmAkCQ1GRCSpCYDQpLUZEBIkpoMCElSkwEhSWoyICRJTQaEJKnJgJAkNRkQkqQmA0KS1GRASJKaDAhJUpMBIUlqMiAkSU0GhCSpyYCQJDUZEJKkpl4DIsnpSTYn2ZLkokb765Lc2v3clOT4oba7kmxKckuSjX3WKUna07y+njjJGHA5cCqwDdiQZF1V3THU7VvAy6vqe0nOAFYDLx1qP6Wq7u+rRknS5Po8gjgR2FJVW6tqF3AVsGK4Q1XdVFXf61a/CCzqsR5J0gz0GRBHAfcMrW/rtk3mzcCnh9YLuDbJzUlWTjYoycokG5Ns3Llz5xMqWJL0mN5OMQFpbKtmx+QUBgFx8tDmk6pqe5LnANclubOqbtjjCatWMzg1xfLly5vPL0mauT6PILYBRw+tLwK2T+yU5Djgw8CKqnpgfHtVbe8e7wPWMjhlJUnaT/oMiA3AsiRLk8wHzgXWDXdIshj4BPD6qvrG0PYFSQ4bXwZOA27rsVZJ0gS9nWKqqt1JLgCuAcaANVV1e5Lzu/ZVwMXAs4EPJgHYXVXLgSOAtd22ecCVVfWZvmqVJO2pz88gqKr1wPoJ21YNLb8FeEtj3Fbg+InbJUn7j3dSS5KaDAhJUpMBIUlqMiAkSU0GhCSpyYCQJDUZEJKkJgNCktRkQEiSmgwISVKTASFJajIgJElNBoQkqcmAkCQ1GRCSpCYDQpLUZEBIkpoMCElSkwEhSWoyICRJTQaEJKmp14BIcnqSzUm2JLmo0f66JLd2PzclOX7UsZKkfvUWEEnGgMuBM4BjgdcmOXZCt28BL6+q44D3AqtnMFaS1KM+jyBOBLZU1daq2gVcBawY7lBVN1XV97rVLwKLRh0rSerXvKkak/zeVO1V9f4pmo8C7hla3wa8dIr+bwY+PdOxSVYCKwEWL148VbmSpBmYMiCAw7rHnwdeAqzr1n8duGGasWlsq2bH5BQGAXHyTMdW1Wq6U1PLly9v9pEkzdyUAVFV7wFIci1wQlX9oFt/N/CxaZ57G3D00PoiYPvETkmOAz4MnFFVD8xkrCSpP6N+BrEY2DW0vgtYMs2YDcCyJEuTzAfO5bEjEACSLAY+Aby+qr4xk7GSpH5Nd4pp3P8AvpxkLYNTPa8GPjLVgKraneQC4BpgDFhTVbcnOb9rXwVcDDwb+GASgN1VtXyysTP/9SRJe2ukgKiqP0nyaeBXuk1vrKqvjjBuPbB+wrZVQ8tvAd4y6lhJ0v4zk8tcDwUeqqr/CmxLsrSnmiRJB4CRAiLJHwHvAn6/2/QU4H/2VZQkafaNegTxauBVwI8Aqmo7j10CK0l6Eho1IHZVVdHdi5BkQX8lSZIOBKNexXR1kr8EnpnkN4E3Mbh3QdI0LrzwQnbs2MGRRx7JpZdeOtvlSCMb9Sqm9yU5FXiIwV3VF1fVdb1WJj1J7Nixg3vvvXe2y5BmbKSASHJJVb0LuK6xTZL0JDTqZxCnNradsS8LkSQdWKabzfWtwG8Dz09y61DTYcCNfRYmSZpd051iupLBFNz/CRj+VrcfVNV3e6tKkjTrpguIqqq7krxtYkOSZxkS+4dXwUiaDaMcQZwJ3MzgHojh72ko4Pk91aUhXgUjaTZM930QZ3aPzrskSQeZUedievOE9bFufiZJ0pPUqHdS/1qSsxl8LejhwBrg871VJU3h2//xF2e7hBnZ/d1nAfPY/d2751Ttiy/eNNslaJaNeif1byQ5B9gE/Bh4bVV5maskPYmNeoppGfAO4OPAXcDrkxzaY12SpFk26imm/w28raquz+C7QX+PwfdG/0JvlfXsxf9uym9MPaAcdv8PGAO+ff8P5lTdN//pebNdgqQnYNSAOLGqHoLBjRHAnyVZ119ZkqTZNuUppiQXAlTVQ0leM6H5jb1VJUmaddN9BnHu0PLvT2g7fR/XIkk6gEwXEJlkubW+5+Dk9CSbk2xJclGj/ZgkX0jycJJ3Tmi7K8mmJLck2Tjda0mS9q1p52KaZLm1/jhJxoDLGUwVvg3YkGRdVd0x1O27wNuBsyZ5mlOq6v5papQk9WC6gDg+yUMMjhb+SbdMt/60acaeCGypqq0ASa4CVgD/GBBVdR9wX5J/uTfFS3PB4U97FNjdPUpzx3RzMY09gec+CrhnaH0b8NIZjC/g2iQF/GVVrW51SrISWAmwePHivSz1wPbo/AWPe9Tc8s7jvj/bJUh7ZdTLXPdG6zOKKU9LTXBSVW1P8hzguiR3VtUNezzhIDhWAyxfvnwmzz9n/GjZabNdgqSD0KhfObo3tgFHD60vAraPOriqtneP9wFrGZyykiTtJ30GxAZgWZKlSeYzuGR2pJvrkixIctj4MnAacFtvlUqS9tDbKaaq2p3kAuAaYAxYU1W3Jzm/a1+V5EhgI/AM4NEkvwscy2DG2LWDWT2YB1xZVZ/pq1ZJ0p76/AyCqloPrJ+wbdXQ8g4Gp54megg4vs/aJElT6/MUkyRpDjMgJElNBoQkqcmAkCQ1GRCSpCYDQpLUZEBIkpoMCElSkwEhSWoyICRJTQaEJKnJgJAkNRkQkqQmA0KS1GRASJKaDAhJUpMBIUlqMiAkSU0GhCSpyYCQJDUZEJKkpl4DIsnpSTYn2ZLkokb7MUm+kOThJO+cyVhJUr96C4gkY8DlwBnAscBrkxw7odt3gbcD79uLsZKkHvV5BHEisKWqtlbVLuAqYMVwh6q6r6o2AI/MdKwkqV99BsRRwD1D69u6bft0bJKVSTYm2bhz5869KlSStKc+AyKNbbWvx1bV6qpaXlXLFy5cOHJxkqSp9RkQ24Cjh9YXAdv3w1hJ0j7QZ0BsAJYlWZpkPnAusG4/jJUk7QPz+nriqtqd5ALgGmAMWFNVtyc5v2tfleRIYCPwDODRJL8LHFtVD7XG9lWrJGlPvQUEQFWtB9ZP2LZqaHkHg9NHI42VJO0/3kktSWoyICRJTQaEJKnJgJAkNRkQkqQmA0KS1GRASJKaDAhJUpMBIUlqMiAkSU0GhCSpyYCQJDUZEJKkJgNCktRkQEiSmgwISVKTASFJajIgJElNBoQkqcmAkCQ1GRCSpKZeAyLJ6Uk2J9mS5KJGe5L8edd+a5IThtruSrIpyS1JNvZZpyRpT/P6euIkY8DlwKnANmBDknVVdcdQtzOAZd3PS4EPdY/jTqmq+/uqUZI0uT6PIE4EtlTV1qraBVwFrJjQZwXwkRr4IvDMJM/tsSZJ0oj6DIijgHuG1rd120btU8C1SW5OsrK3KiVJTb2dYgLS2FYz6HNSVW1P8hzguiR3VtUNe7zIIDxWAixevPiJ1CtJGtLnEcQ24Oih9UXA9lH7VNX4433AWganrPZQVauranlVLV+4cOE+Kl2S1GdAbACWJVmaZD5wLrBuQp91wHnd1UwvAx6squ8kWZDkMIAkC4DTgNt6rFWSNEFvp5iqaneSC4BrgDFgTVXdnuT8rn0VsB54JbAF+DHwxm74EcDaJOM1XllVn+mrVknSnvr8DIKqWs8gBIa3rRpaLuBtjXFbgeP7rE2SNDXvpJYkNRkQkqQmA0KS1GRASJKaDAhJUpMBIUlqMiAkSU0GhCSpyYCQJDUZEJKkJgNCktRkQEiSmgwISVKTASFJajIgJElNBoQkqcmAkCQ1GRCSpCYDQpLUZEBIkpoMCElSkwEhSWrqNSCSnJ5kc5ItSS5qtCfJn3fttyY5YdSxkqR+9RYQScaAy4EzgGOB1yY5dkK3M4Bl3c9K4EMzGCtJ6lGfRxAnAluqamtV7QKuAlZM6LMC+EgNfBF4ZpLnjjhWktSjeT0+91HAPUPr24CXjtDnqBHHApBkJYOjD4AfJtn8BGo+kB0O3D/bRcxE3vdvZ7uEA8mc23/8UWa7ggPJnNp/efuM9t3zJmvoMyBaFdaIfUYZO9hYtRpYPbPS5p4kG6tq+WzXob3j/pvbDtb912dAbAOOHlpfBGwfsc/8EcZKknrU52cQG4BlSZYmmQ+cC6yb0GcdcF53NdPLgAer6jsjjpUk9ai3I4iq2p3kAuAaYAxYU1W3Jzm/a18FrAdeCWwBfgy8caqxfdU6RzzpT6M9ybn/5raDcv+lqnlqX5J0kPNOaklSkwEhSWoyIPajJD9NcsvQz5LZrkl7J8kfJLm9myLmliTN+3SmeY5XOY3MvpXkiCRXJtma5OYkX0jy6tmua67yM4j9KMkPq+rpk7SFwf54dD+XpRlK8svA+4FXVNXDSQ4H5leVl2LPou5v6Cbgv3cXwZDkecCrquqyEcaPVdVPey5zTvEIYhYlWZLk60k+CHwFODrJh5Js7N6dvmeo711J3pPkK0k2JTmm2/70JH/Vbbs1ydnd9tO6d09fSfKxJM1g0l55LnB/VT0MUFX3V9X2bh9dkuTL3c8LAZL8epIvJflqkv+T5Ihu+xuS/EW3fEU3ceVN3bvffz1rv93c9c+BXePhAFBVd1fVZUnGkvxpkg3d38lvASR5RZLPJrkS2NStfz7J1Um+keQ/J3ldtz83JXlBN26yffruJGuSfK7bj2/vtr83yTvG60ryJ+NtB7Sq8mc//QA/BW7pftYCS4BHgZcN9XlW9zgGfA44rlu/C/idbvm3gQ93y5cA/2Vo/M8ymBbgBmBBt+1dwMWz/fs/WX6Ap3f78BvAB4GXD+2jP+iWzwM+ObRPxo/W3wL8Wbf8BuAvuuUrgI8xeNN2LIO5yGb9d51LP8DbgQ9M0rYS+MNu+anARmAp8ArgR8DSru0VwPcZvAl4KnAv8J6u7R3jf2tT7NN3MziKeWr3d/gA8JTub/0rXZ9DgL8Hnj3b/2bT/fR5J7X29JOqetH4SvcZxN01mKhw3L/p5peax+A/0mOBW7u2T3SPNwP/qlv+FwxuJASgqr6X5Mxu3I2Do27mA1/Y17/MwaqqfpjkxcCvAKcAfz30WcJHhx4/0C0v6vo8l8G++NYkT/03NTjFeMf4O1LtvSSXAycDu4C7geOGjsx+hsEs0ruAL1fV8D7ZUIMbdkny98C13fZNDPY3TL1PP1WDo8uHk9wHHFFVdyV5IMkvAUcAX62qB/bxr7zPGRCz70fjC0mWAu8EXtL9j/4K4GlDfR/uHn/KY/sutOe4uq6qXttLxaIG56o/B3wuySZgfGbC4X0xvnwZ8P6qWpfkFQzeZbY8PLTsTHkzdztw9vhKVb2t+3xoI/BtBkfg1wwP6PbHj3i84f3w6ND6ozz2dzfVPh0eP/y3+mEGR41HAmtG/aVmk59BHFieweA/1ge7d5BnjDDmWuCC8ZUkPwt8EThp6Bz4oUl+rod6D0pJfj7JsqFNL2LwDhXgnKHH8aO2n2FwqgIeCxLte38LPC3JW4e2Hdo9XgO8NclTAJL8XJIFT+C19mafrgVOB17S1XPA8wjiAFJVX0vyVQbvhLYCN44w7I+By5PcxuDdynuq6hNJ3gB8NMlTu35/yOCcuZ64pwOXJXkmsJvBVDErgTOBpyb5EoM3X+NHcO8GPpbkXgbhvXR/F3wwqKpKchbwgSQXAjsZvOF6F4PPd5YAX+mudtoJnPUEXu7dzHCfVtWuJJ8Fvl9z5GopL3OV9pEkdwHLq2rOfG+A9p8khzC4WvE1VfXN2a5nFJ5ikqSeZfCVyVuA6+dKOIBHEJKkSXgEIUlqMiAkSU0GhCSpyYDQQS1zYPbP4TmbpP3JgNBBq7se/m+AG6rq+VX1YgbTlizq8TXH+npuaV8zIHQw25vZP9Ntv62b3fOcbvshST6YwSy8n0yyfnzenwxmeb04yd8Br0nym93zfi3Jx5Mc2vW7IsmqJP+3m0n0zKFa/2mSzyT5ZpJLu/5vTjI+3xPd876/9381HTS8k1oHs19gcONSy5uBB6vqJd3d6DcmuRY4gcHUGsczmK1zQ5IbgJMY3Kn7i8BzgK/z+Pl2/qGqTgZI8uyq+m/d8h93rzX+fQVLgJcDLwA+Oz5dSveav8Rgnp/NSS4DrgJuTXJhVT0CvBH4rb39x5AmMiCkzoizf54MfLSbKuH/Jfk8g7l1TgY+1s3GuqObUmHYXw8t/7MuGJ7JYNqO4Xl5ru6e45tJtgLHdNuvr6oHuzrvAJ5XVfck+VvgzCRfB55SVZue+L+ENGBA6GC2N7N/vnKS55pu9tXhGUOvAM7q5t56A4PvIPjHMiaMG1+faobQfw/cCfzVNDVIM+JnEDqY7c3snzcA53SfUSwEfhX4MvB3wNndZxFH8Pj/6U90GPCd7rlfN6HtNd1zvAB4PrB5ql+gqr4EHA38Bo99F4W0T3gEoYPWXs7+uRb4ZeBrDN7dX1hVO5J8HPg14DYGs+Z+CXhwkpf+D1373Qy+hOawobbNwOcZfKnM+VX1D4OXn9LVwIuq6nuj/u7SKJyLSdpHkjy9+7a5ZzM4qjipqnbMYPwVDL6m9H/N8HU/yeCrNq+fUcHSNDyCkPadT3bfETEfeO9MwmFvdK/1ZeBrhoP64BGEJKnJD6klSU0GhCSpyYCQJDUZEJKkJgNCktT0/wEvLt1t91JsfgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(df.Geography, df.Exited)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d6eaf2d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "\n",
       "   Tenure   Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2      0.00              1          1               1   \n",
       "1       1  83807.86              1          0               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fc74471e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Geography', ylabel='Exited'>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='Geography',y='Exited',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "885a327a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Gender', ylabel='Exited'>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='Gender',y='Exited',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5325cc5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='NumOfProducts', ylabel='Exited'>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='NumOfProducts',y='Exited',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "01e64203",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='HasCrCard', ylabel='Exited'>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='HasCrCard',y='Exited',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2cecf62a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='IsActiveMember', ylabel='Exited'>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x='IsActiveMember',y='Exited',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "465aa518",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x7fbd2d94c550>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1980x1980 with 132 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0f899c2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8,5))\n",
    "sns.heatmap(df.corr(),annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "74283228",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    7963\n",
       "1    2037\n",
       "Name: Exited, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Exited.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7343059e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RowNumber          0\n",
       "CustomerId         0\n",
       "Surname            0\n",
       "CreditScore        0\n",
       "Geography          0\n",
       "Gender             0\n",
       "Age                0\n",
       "Tenure             0\n",
       "Balance            0\n",
       "NumOfProducts      0\n",
       "HasCrCard          0\n",
       "IsActiveMember     0\n",
       "EstimatedSalary    0\n",
       "Exited             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3ee5a6eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#No missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "9c38e3d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "\n",
       "   Tenure   Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2      0.00              1          1               1   \n",
       "1       1  83807.86              1          0               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8790af5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='CreditScore'>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.CreditScore)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "29ea85b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age'>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAPZElEQVR4nO3de4xc5XmA8ee1N8HGTgjYgFybdhttgLZAiI0olwoNYMpyC3W5CIuLkSj8U9kGiqoWXIMpICGBBbLUqCa0QFslApKWgoyJCVDaIjXaJVwLlFHjJqZcDSU1t9Tw9Y85s+wsG7xrD/uexc9PWq3PnD0zL7vjh7Pfjs9GKQVJ0sSbkj2AJO2sDLAkJTHAkpTEAEtSEgMsSUl6xvPBs2fPLr29vZ/RKJL0+TN79mweeOCBB0op/SP3jSvAvb29DAwMdG8ySdoJRMTs0W53CUKSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSnJuH4nnD7dmjVraDabXbu/l156CYC5c+d27T7Hoq+vj6VLl07oY0o7IwPcRc1mkyeeeY4Pd92jK/c39d23AXjlg4n7Mk19980JeyxpZ2eAu+zDXffgvf1P7Mp9TX9+HUDX7m88jynps+casCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCWZkACvWbOGNWvWTMRDSRPC57S6oWciHqTZbE7Ew0gTxue0usElCElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlqQkBliSkhhgSUpigCUpiQGWpCQGWJKSGGBJSmKAJSmJAZakJAZYkpIYYElKYoAlKYkBlrqg0WgMvY22vXjxYhqNBuecc86YPh7gzDPPpNFosHjxYgBOPfVUGo0GixYtGvU+jz/+eBqNBv39/QAsWrSIRqPBaaedBsCyZctoNBpceumlox5//fXX02g0uPHGGwG4/PLLaTQarFy5cmimVatW0Wg0uPbaawG45557aDQa3HvvvQA89NBDNBoNHn74YQAGBgY45phjGBwcHHX/5s2bWbZsGZs3bx51u9lsctJJJ9FsNkfdPxbbc8xwI2foJgMsTYCXX34ZgE2bNo35mNdee63j2LfffhuAt956a9T7/OCDDwB4//33Oz6uHZ6nnnoKgMcff3zU4++//36AoZg+9thjADz66KNDM7XDuWHDBgBuuukmAFavXg3AddddBzAU6KuuuoqPPvqIK6+8ctT9t99+O08//TR33HHHqNvXXHMN77zzDtdcc82o+8die44ZbuQM3WSApR00/Ky1W9tnnnlmV+/z6KOP7theuHBhx3b7rLntjDPO6NheuXIlq1at6rjtoosuopQCQCmFG264ga1btwKwdetWbr31VrZs2QLAli1buOWWWzr233vvvaxfv55SCuvXr6fZbHZsDw4OsnHjRgA2btzI4OBgx/6xnNFu3rx53McM12w2O2bo9llwtD+BY3HIIYeUgYGBcT/I6aefznvvvUdfX9+4j51Mms0m//uLwjsHn9WV+5v+/DoA3tv/xK7c31jMeOK7fOmL8bn/Wu2oZrPJ9OnTufvuuz8RO41NRDB16lS2bt1KT08P8+bNY9OmTUPb06ZNGwo4wMyZM3n//feH9p900klccskln/oYq1evZt26deM6Zrjzzz9/KMAAvb293HbbbeP9TyUiBksph4y8fZtnwBFxUUQMRMTA66+/Pu4HlqTRlFI6zog3btzYsT08vtA6ix6+v70M8mkefPDBcR8z3PD4jra9o3q29QGllLXAWmidAW/Pg8ydOxeAm2++eXsOnzSWL1/O4H++mj3GDvlo2pfp++ren/uv1Y5avnx59giT3o6eAR933HHbfIyFCxd2nAGP5Zjhent7P3EG3E2uAUs1tNdee3X1/iKiY7unp/Pca9q0aR3be+65Z8f2UUcd9Yl15H333bdj++STT+7YPvfcczu2zz777I7tSy+9lClTWgmaOnUqK1as6Ngeuea8atWqjv3nnXce27JkyZJxHzPcihUrPnV7RxlgaQc9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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.Age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8efd4c53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='NumOfProducts'>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.NumOfProducts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "76bee21c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='HasCrCard'>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.HasCrCard)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "e1be2aac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='IsActiveMember'>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.IsActiveMember)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "bf8f8e35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='EstimatedSalary'>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWQAAAEGCAYAAABSJ+9xAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAOgUlEQVR4nO3df5Bd5V3H8feXbFsSgfwgkMms2m1Y/EGdkaYZplVbcaxY0FaqjBbRAepMra0xbYfOwGSGwTpTW9CpuNVaqpXKRMEO9hfSYsUOOqVTm9Dwo5DIBcPINg2UKGATsITHP86z5GazP+7d7D33S/J+zdzZc8895z7ffc65nz33ufecjVIKkqThO27YBUiSGgayJCVhIEtSEgayJCVhIEtSEiP9LLx69eoyNjY2oFIk6ei0bdu275RSTplvub4CeWxsjK1bty68Kkk6BkXEI70s55CFJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCVhIEtSEgayJCXR1//UU7smJibodDrDLiO9yclJAEZHR4dcyYvD+Pg4GzduHHYZmoGBnFin02H7fQ9wYNmqYZeS2pJ9TwLw7WfdneezZN/eYZegObgHJ3dg2Sr2/8h5wy4jtaU7bgWwn3ow1VfKyTFkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUrCQJakJAxkSUqilUCemJhgYmKijaYkaVG1mV8jbTTS6XTaaEaSFl2b+eWQhSQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlYSBLUhIGsiQlMdJGI5OTk+zfv59Nmza10dxRo9PpcNz/lWGXoaPIcc88RafztK/FPnQ6HZYuXdpKW/MeIUfE2yNia0Rsffzxx9uoSZKOSfMeIZdSrgOuA9iwYcOCDtdGR0cBuPbaaxey+jFr06ZNbHt4z7DL0FHk+eNPYnzdGl+LfWjz3YRjyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUkYyJKUhIEsSUmMtNHI+Ph4G81I0qJrM79aCeSNGze20YwkLbo288shC0lKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCQMZElKwkCWpCRGhl2A5rZk316W7rh12GWktmTfEwD2Uw+W7NsLrBl2GZqFgZzY+Pj4sEt4UZicfA6A0VGDZn5r3K8SM5AT27hx47BLkNQix5AlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSMJAlKQkDWZKSiFJK7wtHPA48ssC2VgPfWeC6g2Rd/bGu/lhXf47Wul5eSjllvoX6CuQjERFbSykbWmmsD9bVH+vqj3X151ivyyELSUrCQJakJNoM5OtabKsf1tUf6+qPdfXnmK6rtTFkSdLcHLKQpCQMZEnKopQy0BvwRmAn0AEuH1AbPwB8GXgA+Cawqc6/CpgEttfbeV3rXFFr2gn8fNf8VwP31sf+lIPDOi8DbqrzvwaM9Vjbrvp824Gtdd4q4EvAg/XnyjbrAn64q0+2A08B7x5GfwGfAB4D7uua10r/ABfXNh4ELu6hrmuAHcA9wKeBFXX+GLC/q9/+ouW6WtluC6jrpq6adgHbh9Bfs2XD0PexGV8Pix2O0zpjCfAQsA54KXA3cMYA2lkLrK/TJwL/AZxRd9TLZlj+jFrLy4BX1BqX1Mf+HXgtEMAXgHPr/HdO7TjAW4GbeqxtF7B62ryrqX+cgMuBD7Vd17Rt9G3g5cPoL+D1wHoOfSEPvH9oXpAP158r6/TKeeo6Bxip0x/qqmuse7lpv18bdQ18uy2krmm1/DFw5RD6a7ZsGPo+NuPvv9AQ7PHF/lrgtq77VwBXDLLN2s5ngZ+bY0c9pA7gtlrrWmBH1/wLgY91L1OnR2jO2okeatnF4YG8E1jbtcPsbLuuruc6B/hKnR5KfzHtBdpG/3QvUx/7GHDhXHVNe+wtwJa5lmurrja225H0V13/v4DTh9Ffs2RDin1s+m3QY8ijNBtiyqN13sBExBjwKpq3DgC/GxH3RMQnImLlPHWN1umZ6n1hnVLKc8CTwMk9lFSAf4qIbRHx9jpvTSlld32u3cCpQ6hryluBv+u6P+z+gnb650j3zbfRHCVNeUVEfCMi7oiI13W13VZdg95uR9JfrwP2lFIe7JrXen9Ny4aU+9igAzlmmFcG1ljECcDNwLtLKU8BHwVOA84EdtO8bZqrrrnqXejv8pOllPXAucC7IuL1cyzbZl1ExEuBNwOfqrMy9NdcFrOOI+m3zcBzwJY6azfwg6WUVwHvBf42Ik5qsa42ttuRbM8LOfSPfuv9NUM2zGaofTboQH6UZlB9yvcD3xpEQxHxEpoO31JK+QeAUsqeUsqBUsrzwMeBs+ap69E6PVO9L6wTESPAcmDvfHWVUr5Vfz5G80HQWcCeiFhbn2stzYchrdZVnQvcVUrZU2scen9VbfTPgvbNiLgY+EXgolLfh5ZSni2lPFGnt9GMO/5QW3W1tN0W2l8jwC/TfOg1VW+r/TVTNpB1H5trPONIbzTjKQ/TDI5Pfaj3ygG0E8DfAH8yfUyqa/o9wI11+pUcOnD/MAcH7r8OvIaDA/fn1fnv4tCB+7/voa7vA07smr6T5lsn13DoBwpXt1lXV303ApcOu784fEx04P1D80HLf9J82LKyTq+ap643AvcDp0xb7pSuOtbRfONhVYt1DXy7LaSurj67Y1j9xezZkGIfO+y1cKRh2MOL/jyaTzYfAjYPqI2fonkrcA9dX/0BbqD5mso9wOem7biba007qZ+W1vkbgPvqYx/h4Fdbjqd5a9+h+bR1XQ91rasb926ar9xsrvNPBm6n+SrM7dN2oIHXVddbBjwBLO+a13p/0byV3Q18j+aI4rfa6h+aceBOvV3aQ10dmjHBqX1s6kX4K3X73g3cBbyp5bpa2W791lXnXw+8Y9qybfbXbNkw9H1sppunTktSEp6pJ0lJGMiSlISBLElJGMiSlISBLElJGMjqSUQciIjtXbfL51j2/Ig4o+v++yPiDYtQw4qIeOcC1rsqIi6r06+JiK/V3+GBiLhqnnXPjohbFliy1JeRYRegF439pZQze1z2fOAWmpMoKKVcuUg1rKC5stafH8FzfBL41VLK3RGxhOZSpIsmIkZKcz0DqW8eIeuIRMQHI+L+emGbP4qIn6C5PsY19Sj0tIi4PiIuqMvviogPRMRXI2JrRKyPiNsi4qGIeEdd5oSIuD0i7oqIeyPil2pzHwROq897TV32fRHx9dr+73fVtTkidkbEP3No6J5KcwIDpTnd+P66/FkRcWe94M2dEXFYUM+2TERcEhGfiojP01xI6oaumomILRHx5sXqcx3FBnHmnLej7wYc4NCL2v8azamhOzl4xtKK+vN64IKudV+4T3M50t+p0x+mOYPqRJrTaR+r80eAk+r0apqznILDTxk+h+afTwbNwcUtNNflnbqQ+DLgpLr+ZXWdK4H/prmuyG8Dx9f5J3HwWsdvAG6u02cDt8yzzCU0Z6dNnf7708Bn6vRymlNmR4a9Db3lvzlkoV4dNmRRL6TyDPCXEfGPNIHYi8/Vn/cCJ5RSngaejohnImIF8F3gA/XKeM/TXLJwzQzPc069faPePwE4nSbgP11K2VfrnGqPUsr7I2JLXe/Xaa5EdjZNcH4yIk6nOdX2JTO0N9cyXyql7K1t3BERfxYRp9JcWOfm4jCGeuCQhRashsxZNFfSOh/4Yo+rPlt/Pt81PXV/BLiI5oj51fWPwB6a6wVMF8AfllLOrLfxUspfTZU3R90PlVI+Cvws8OMRcTLwB8CXSyk/BrxplvbmWua705a9of4elwJ/PVstUjcDWQtWrzG7vJRyK83/5DuzPvQ0zVHqQi2nGb74XkT8DM2/l5rpeW8D3lbrICJG61HpvwJviYilEXEiTXhO1fwLETF1ndrTaYZi/qe2OVnnXzJHXfMtM+V6mj6hlPLNeZaVAL9lod4tjYjtXfe/CFwLfDYijqc5Wn1PfexG4OMR8XvABQtoawvw+YjYSjNevQOglPJERHwlIu4DvlBKeV9E/Cjw1Zqx/wv8RinlroiY+gebjwD/1vXcvwl8OCL20Vxk/qJSyoGIuJpmOOK9wL/MUlcvy1Br3RMRDwCf6f/X17HKq71JAxARy2jGyNeXUp4cdj16cXDIQlpk9SSYHcCEYax+eIQsSUl4hCxJSRjIkpSEgSxJSRjIkpSEgSxJSfw/dUy8MdPgOSUAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.EstimatedSalary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8a485726",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Tenure'>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.Tenure)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "df052c60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Balance'>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.Balance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "709f6db0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Outlier Removal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "93625f4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def outlier_credit_score(df):\n",
    "    IQR = df['CreditScore'].quantile(0.75) - df['CreditScore'].quantile(0.25)\n",
    "    \n",
    "    lower_range = df['CreditScore'].quantile(0.25) - (1.5 * IQR)\n",
    "    upper_range = df['CreditScore'].quantile(0.75) + (1.5 * IQR)\n",
    "    \n",
    "    df.loc[df['CreditScore'] <= lower_range, 'CreditScore'] = lower_range\n",
    "    df.loc[df['CreditScore'] >= upper_range, 'CreditScore'] = upper_range\n",
    "    \n",
    "outlier_credit_score(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2985b9cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='CreditScore'>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.CreditScore)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "28a5e443",
   "metadata": {},
   "outputs": [],
   "source": [
    "def outlier_NOP(df):\n",
    "    IQR = df['NumOfProducts'].quantile(0.75) - df['NumOfProducts'].quantile(0.25)\n",
    "    \n",
    "    lower_range = df['NumOfProducts'].quantile(0.25) - (1.5 * IQR)\n",
    "    upper_range = df['NumOfProducts'].quantile(0.75) + (1.5 * IQR)\n",
    "    \n",
    "    df.loc[df['NumOfProducts'] <= lower_range, 'NumOfProducts'] = lower_range\n",
    "    df.loc[df['NumOfProducts'] >= upper_range, 'NumOfProducts'] = upper_range\n",
    "    \n",
    "outlier_NOP(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1078de25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='NumOfProducts'>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.NumOfProducts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "19b7cd47",
   "metadata": {},
   "outputs": [],
   "source": [
    "def outlier_age(df):\n",
    "    IQR = df['Age'].quantile(0.75) - df['Age'].quantile(0.25)\n",
    "    \n",
    "    lower_range = df['Age'].quantile(0.25) - (1.5 * IQR)\n",
    "    upper_range = df['Age'].quantile(0.75) + (1.5 * IQR)\n",
    "    \n",
    "    df.loc[df['Age'] <= lower_range, 'Age'] = lower_range\n",
    "    df.loc[df['Age'] >= upper_range, 'Age'] = upper_range\n",
    "    \n",
    "outlier_age(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e7060c5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Age'>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df.Age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4947bce9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10000 entries, 0 to 9999\n",
      "Data columns (total 14 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   RowNumber        10000 non-null  int64  \n",
      " 1   CustomerId       10000 non-null  int64  \n",
      " 2   Surname          10000 non-null  object \n",
      " 3   CreditScore      10000 non-null  int64  \n",
      " 4   Geography        10000 non-null  object \n",
      " 5   Gender           10000 non-null  object \n",
      " 6   Age              10000 non-null  int64  \n",
      " 7   Tenure           10000 non-null  int64  \n",
      " 8   Balance          10000 non-null  float64\n",
      " 9   NumOfProducts    10000 non-null  float64\n",
      " 10  HasCrCard        10000 non-null  int64  \n",
      " 11  IsActiveMember   10000 non-null  int64  \n",
      " 12  EstimatedSalary  10000 non-null  float64\n",
      " 13  Exited           10000 non-null  int64  \n",
      "dtypes: float64(3), int64(8), object(3)\n",
      "memory usage: 1.1+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "39737687",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "\n",
       "   Tenure   Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2      0.00            1.0          1               1   \n",
       "1       1  83807.86            1.0          0               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "eca0afa8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(['CustomerId','RowNumber','Surname'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "beca1889",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CreditScore Geography  Gender  Age  Tenure   Balance  NumOfProducts  \\\n",
       "0          619    France  Female   42       2      0.00            1.0   \n",
       "1          608     Spain  Female   41       1  83807.86            1.0   \n",
       "\n",
       "   HasCrCard  IsActiveMember  EstimatedSalary  Exited  \n",
       "0          1               1        101348.88       1  \n",
       "1          0               1        112542.58       0  "
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "aa87e2c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "le_geo = LabelEncoder()\n",
    "le_gen = LabelEncoder()\n",
    "df['Sex']=le_gen.fit_transform(df.Gender)\n",
    "df['Country']=le_geo.fit_transform(df.Geography)\n",
    "df.drop(['Geography','Gender'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "7410b2eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>619</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>608</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CreditScore  Age  Tenure   Balance  NumOfProducts  HasCrCard  \\\n",
       "0          619   42       2      0.00            1.0          1   \n",
       "1          608   41       1  83807.86            1.0          0   \n",
       "\n",
       "   IsActiveMember  EstimatedSalary  Exited  Sex  Country  \n",
       "0               1        101348.88       1    0        0  \n",
       "1               1        112542.58       0    0        2  "
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e472b261",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=df.drop('Exited',axis=1)\n",
    "y=df.Exited"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "17379553",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>619</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>608</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>502</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>699</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>850</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>771</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>96270.64</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>516</td>\n",
       "      <td>35</td>\n",
       "      <td>10</td>\n",
       "      <td>57369.61</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101699.77</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>709</td>\n",
       "      <td>36</td>\n",
       "      <td>7</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>42085.58</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>772</td>\n",
       "      <td>42</td>\n",
       "      <td>3</td>\n",
       "      <td>75075.31</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>92888.52</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>792</td>\n",
       "      <td>28</td>\n",
       "      <td>4</td>\n",
       "      <td>130142.79</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38190.78</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10000 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      CreditScore  Age  Tenure    Balance  NumOfProducts  HasCrCard  \\\n",
       "0             619   42       2       0.00            1.0          1   \n",
       "1             608   41       1   83807.86            1.0          0   \n",
       "2             502   42       8  159660.80            3.0          1   \n",
       "3             699   39       1       0.00            2.0          0   \n",
       "4             850   43       2  125510.82            1.0          1   \n",
       "...           ...  ...     ...        ...            ...        ...   \n",
       "9995          771   39       5       0.00            2.0          1   \n",
       "9996          516   35      10   57369.61            1.0          1   \n",
       "9997          709   36       7       0.00            1.0          0   \n",
       "9998          772   42       3   75075.31            2.0          1   \n",
       "9999          792   28       4  130142.79            1.0          1   \n",
       "\n",
       "      IsActiveMember  EstimatedSalary  Sex  Country  \n",
       "0                  1        101348.88    0        0  \n",
       "1                  1        112542.58    0        2  \n",
       "2                  0        113931.57    0        0  \n",
       "3                  0         93826.63    0        0  \n",
       "4                  1         79084.10    0        2  \n",
       "...              ...              ...  ...      ...  \n",
       "9995               0         96270.64    1        0  \n",
       "9996               1        101699.77    1        0  \n",
       "9997               1         42085.58    0        0  \n",
       "9998               0         92888.52    1        1  \n",
       "9999               0         38190.78    0        0  \n",
       "\n",
       "[10000 rows x 10 columns]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c5d67f7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "sc=StandardScaler()\n",
    "X = sc.fit_transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "81139fa7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,\n",
    "                                              random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e510a805",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((8000, 10), (2000, 10), (8000,), (2000,))"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape, x_test.shape, y_train.shape, y_test.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}