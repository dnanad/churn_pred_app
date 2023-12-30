import pickle
import pandas as pd
import streamlit as st

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


def load_pickles(model_pickle_path):
    model_pickle_opener = open(model_pickle_path, "rb")
    model = pickle.load(model_pickle_opener)

    # label_encoder_opener = open(label_encoder_pickle_path, "rb")
    # label_encoder_dict = pickle.load(label_encoder_opener)

    return model
    # , label_encoder_dict


def make_predictions(data, model):
    prediction = model.predict(data)

    return prediction


def generate_predictions(test_df):
    model_pickle_path = "./churn_prediction_model.pkl"
    # label_encoder_pickle_path = "./churn_prediction_label_encoders.pkl"

    model = load_pickles(model_pickle_path)
    # label_encoder_dict = load_pickles(label_encoder_pickle_path)
    # processed_df = pre_process_data(test_df, label_encoder_dict)
    prediction = make_predictions(test_df, model)
    return prediction


if __name__ == "__main__":
    # make an application
    st.title("Customer Churn Prediction")
    st.write("Enter customer data.")

    # read in the data
    gender = st.selectbox("Select customer's gender:", ["Female", "Male"])
    senior_citizen_input = st.selectbox(
        "Is the customera senior citizen?", ["No", "Yes"]
    )
    if senior_citizen_input == "Yes":
        senior_citizen_input = 1
    else:
        senior_citizen_input = 0

    partner = st.selectbox("Does the customer have a partner? :", ["No", "Yes"])
    dependents = st.selectbox("Does the customer have dependents? :", ["Yes", "No"])
    tenure = st.slider(
        "How many months has the customer been with the company? :",
        min_value=0,
        max_value=72,
        value=24,
    )
    phone_service = st.selectbox(
        "Does the customer have phone service? :", ["No", "Yes"]
    )
    multiple_lines = st.selectbox(
        "Does the customer have multiple lines? :", ["No", "Yes", "No phone service"]
    )
    internet_service = st.selectbox(
        "What type of internet service does the customer have? :",
        ["No", "DSL", "Fiber optic"],
    )
    online_security = st.selectbox(
        "Does the customer have online security? :",
        ["No", "Yes", "No internet service"],
    )
    online_backup = st.selectbox(
        "Does the customer have online backup? :", ["No", "Yes", "No internet service"]
    )
    device_protection = st.selectbox(
        "Does the customer have device protection? :",
        ["No", "Yes", "No internet service"],
    )
    tech_support = st.selectbox(
        "Does the customer have tech support? :", ["No", "Yes", "No internet service"]
    )
    streaming_tv = st.selectbox(
        "Does the customer have streaming TV? :", ["No", "Yes", "No internet service"]
    )
    streaming_movies = st.selectbox(
        "Does the customer have streaming movies? :",
        ["No", "Yes", "No internet service"],
    )
    contract = st.selectbox(
        "What kind of contract does the customer have? :",
        ["Month-to-month", "Two year", "One year"],
    )
    paperless_billing = st.selectbox(
        "Does the customer have paperless billing? :", ["No", "Yes"]
    )
    payment_method = st.selectbox(
        "What is the customer's payment method? :",
        [
            "Mailed check",
            "Credit card (automatic)",
            "Bank transfer (automatic)",
            "Electronic check",
        ],
    )

    monthly_charges = st.slider(
        "What is the customer's monthly charge? :", min_value=0, max_value=118, value=50
    )
    total_charges = st.slider(
        "What is the total charge of the customer? :",
        min_value=0,
        max_value=8600,
        value=2000,
    )
    input_dict = {
        "gender": gender,
        "SeniorCitizen": senior_citizen_input,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }
    input_data = pd.DataFrame([input_dict])

    # generate the prediction for the customer
    if st.button("Predict Churn"):
        pred = generate_predictions(input_data)
        if bool(pred):
            st.erro("Customer will churn!")
        else:
            st.success("Customer will not churn!")
    # pred = generate_predictions(data_to_check)
    # print(pred)


# data_to_check = pd.read_csv("./data/single_row_to_check.csv")
#     # read in the data
#     holdout_customer_data = pd.read_csv("./data/holdout_data.csv")
#     holdout_customers_without_label = holdout_customer_data.drop(
#         columns="Churn")

#     st.text("Enter customer data")
#     chosen_customer = st.selectbox("Select the customer you are speaking to:",
#                                    holdout_customers_without_label.loc[:, 'customerID'])
#     chosen_customer_data = (holdout_customers_without_label.loc,
#                             holdout_customers_without_label.loc[:, 'customerID'])

#     # visualize test data
#     st.table(data_to_check)
