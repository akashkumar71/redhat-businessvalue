import streamlit as st
import pandas as pd
#import os
import pickle
#import itertools

rf_model = pickle.load(open('random_forest_classification_model.pkl','rb'))
df_train = pd.read_pickle('df_train.pkl')

def main():
    st.title("Predicting Red Hat Business Value")

    activity_category = st.selectbox('activity_category', sorted(df_train['activity_category'].unique()))

    char_1_x = st.selectbox('char_1_x', sorted(df_train['char_1_x'].unique()))
    char_2_x = st.selectbox('char_2_x', sorted(df_train['char_2_x'].unique()))
    char_3_x = st.selectbox('char_3_x', sorted(df_train['char_3_x'].unique()))
    char_4_x = st.selectbox('char_4_x', sorted(df_train['char_4_x'].unique()))
    char_5_x = st.selectbox('char_5_x', sorted(df_train['char_5_x'].unique()))
    char_6_x = st.selectbox('char_6_x', sorted(df_train['char_6_x'].unique()))
    char_7_x = st.selectbox('char_7_x', sorted(df_train['char_7_x'].unique()))
    char_8_x = st.selectbox('char_8_x', sorted(df_train['char_8_x'].unique()))
    char_9_x = st.selectbox('char_9_x', sorted(df_train['char_9_x'].unique()))
    char_10_x = st.selectbox('char_10_x', sorted(df_train['char_10_x'].unique()))
    char_1_y = st.selectbox('char_1_y', sorted(df_train['char_1_y'].unique()))
    group_1 = st.selectbox('group_1', sorted(df_train['group_1'].unique()))

    char_2_y = st.selectbox('char_2_y', sorted(df_train['char_2_y'].unique()))
    char_3_y = st.selectbox('char_3_y', sorted(df_train['char_3_y'].unique()))
    char_4_y = st.selectbox('char_4_y', sorted(df_train['char_4_y'].unique()))
    char_5_y = st.selectbox('char_5_y', sorted(df_train['char_5_y'].unique()))
    char_6_y = st.selectbox('char_6_y', sorted(df_train['char_6_y'].unique()))
    char_7_y = st.selectbox('char_7_y', sorted(df_train['char_7_y'].unique()))
    char_8_y = st.selectbox('char_8_y', sorted(df_train['char_8_y'].unique()))
    char_9_y = st.selectbox('char_9_y', sorted(df_train['char_9_y'].unique()))
    char_10_y = st.selectbox('char_10_y', sorted(df_train['char_10_y'].unique()))
    char_11 = st.selectbox('char_11', sorted(df_train['char_11'].unique()))
    char_12 = st.selectbox('char_12', sorted(df_train['char_12'].unique()))
    char_13 = st.selectbox('char_13', sorted(df_train['char_13'].unique()))
    char_14 = st.selectbox('char_14', sorted(df_train['char_14'].unique()))
    char_15 = st.selectbox('char_15', sorted(df_train['char_15'].unique()))
    char_16 = st.selectbox('char_16', sorted(df_train['char_16'].unique()))
    char_17 = st.selectbox('char_17', sorted(df_train['char_17'].unique()))
    char_18 = st.selectbox('char_18', sorted(df_train['char_18'].unique()))
    char_19 = st.selectbox('char_19', sorted(df_train['char_19'].unique()))
    char_20 = st.selectbox('char_20', sorted(df_train['char_20'].unique()))
    char_21 = st.selectbox('char_21', sorted(df_train['char_21'].unique()))
    char_22 = st.selectbox('char_22', sorted(df_train['char_22'].unique()))
    char_23 = st.selectbox('char_23', sorted(df_train['char_23'].unique()))
    char_24 = st.selectbox('char_24', sorted(df_train['char_24'].unique()))
    char_25 = st.selectbox('char_25', sorted(df_train['char_25'].unique()))
    char_26 = st.selectbox('char_26', sorted(df_train['char_26'].unique()))
    char_27 = st.selectbox('char_27', sorted(df_train['char_27'].unique()))
    char_28 = st.selectbox('char_28', sorted(df_train['char_28'].unique()))
    char_29 = st.selectbox('char_29', sorted(df_train['char_29'].unique()))
    char_30 = st.selectbox('char_30', sorted(df_train['char_30'].unique()))
    char_31 = st.selectbox('char_31', sorted(df_train['char_31'].unique()))
    char_32 = st.selectbox('char_32', sorted(df_train['char_32'].unique()))
    char_33 = st.selectbox('char_33', sorted(df_train['char_33'].unique()))
    char_34 = st.selectbox('char_34', sorted(df_train['char_34'].unique()))
    char_35 = st.selectbox('char_35', sorted(df_train['char_35'].unique()))
    char_36 = st.selectbox('char_36', sorted(df_train['char_36'].unique()))
    char_37 = st.selectbox('char_37', sorted(df_train['char_37'].unique()))
    char_38 = st.selectbox('char_38', sorted(df_train['char_38'].unique()))




    df_model=pd.DataFrame(data=[[ activity_category,char_1_x,char_2_x,char_3_x,char_4_x,char_5_x,char_6_x,char_7_x,char_8_x,char_9_x
                                 ,char_10_x, group_1, char_1_y, char_2_y,char_3_y,char_4_y,char_5_y,char_6_y,char_7_y,char_8_y,char_9_y,char_10_y,
                                 char_11,char_12,char_13,char_14, char_15,char_16,char_17,char_18,char_19,char_20,char_21,char_22,char_23,
                                 char_24,char_25,char_26,char_27, char_28, char_29, char_30,char_31,char_32,char_33,char_34,char_35,char_36,char_37,char_38]])

    print(df_model)
    st.write(df_model.head())
    #result =''
    if st.button("Predict"):
        result = rf_model.predict(df_model)
        if result :
            st.success('The output is {}. This coustmer has business potential and is likely to give Red Hat business.'.format(result))
        else :
            st.text('This coustmer will not give business to the Red Hat.')

if __name__ == '__main__':
    main()
